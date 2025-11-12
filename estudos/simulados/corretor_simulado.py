#!/usr/bin/env python3
"""
Corretor de Simulados - MP-SE 2025
Corrige simulados e gera relatórios detalhados de desempenho
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple
from collections import defaultdict


class CorretorSimulado:
    """Classe para corrigir simulados e gerar análises"""

    def __init__(self):
        self.resultado = {}

    def carregar_simulado(self, caminho_simulado: str) -> Dict:
        """Carrega simulado de arquivo JSON"""
        with open(caminho_simulado, 'r', encoding='utf-8') as f:
            return json.load(f)

    def carregar_respostas(self, caminho_respostas: str = None) -> Dict[int, str]:
        """
        Carrega respostas do usuário

        Args:
            caminho_respostas: Caminho para arquivo com respostas

        Returns:
            Dicionário {número_questão: resposta}
        """
        if caminho_respostas and Path(caminho_respostas).exists():
            with open(caminho_respostas, 'r', encoding='utf-8') as f:
                return json.load(f)

        # Se não foi fornecido arquivo, pedir respostas interativamente
        return self._pedir_respostas_interativo()

    def _pedir_respostas_interativo(self) -> Dict[int, str]:
        """Solicita respostas do usuário via terminal"""
        print("\n📝 Digite suas respostas (formato: a, b, c, d ou e)")
        print("Digite 'x' para questão não respondida")
        print("Digite 'fim' quando terminar\n")

        respostas = {}
        questao = 1

        while True:
            try:
                resposta = input(f"Questão {questao:02d}: ").strip().lower()

                if resposta == 'fim':
                    break

                if resposta in ['a', 'b', 'c', 'd', 'e', 'x']:
                    respostas[questao] = resposta if resposta != 'x' else None
                    questao += 1
                else:
                    print("❌ Resposta inválida! Use a, b, c, d, e ou x")

            except KeyboardInterrupt:
                print("\n\n⚠️  Correção cancelada")
                return {}

        return respostas

    def corrigir(
        self,
        simulado: Dict,
        respostas_usuario: Dict[int, str],
        tempo_gasto_minutos: int = None
    ) -> Dict:
        """
        Corrige o simulado e gera relatório

        Args:
            simulado: Dicionário com o simulado
            respostas_usuario: Dicionário com respostas do usuário
            tempo_gasto_minutos: Tempo gasto em minutos

        Returns:
            Dicionário com resultado detalhado
        """
        questoes = simulado["questoes"]
        total_questoes = len(questoes)

        # Inicializar contadores
        acertos = 0
        erros = 0
        brancos = 0
        detalhes = []
        erros_por_area = defaultdict(int)
        acertos_por_area = defaultdict(int)
        total_por_area = defaultdict(int)

        # Corrigir cada questão
        for q in questoes:
            num = q["numero"]
            gabarito = q["gabarito"].lower()
            area = q["area"]
            resposta_usuario = respostas_usuario.get(num, "").lower() if respostas_usuario.get(num) else None

            total_por_area[area] += 1

            if resposta_usuario is None or resposta_usuario == "":
                brancos += 1
                status = "branco"
            elif resposta_usuario == gabarito:
                acertos += 1
                acertos_por_area[area] += 1
                status = "acerto"
            else:
                erros += 1
                erros_por_area[area] += 1
                status = "erro"

            detalhes.append({
                "numero": num,
                "area": area,
                "gabarito": gabarito,
                "resposta_usuario": resposta_usuario,
                "status": status,
                "enunciado": q["enunciado"][:100] + "..." if len(q["enunciado"]) > 100 else q["enunciado"]
            })

        # Calcular estatísticas gerais
        percentual_acertos = (acertos / total_questoes) * 100
        percentual_erros = (erros / total_questoes) * 100
        percentual_brancos = (brancos / total_questoes) * 100

        # Calcular desempenho por área
        desempenho_por_area = {}
        for area in total_por_area:
            total = total_por_area[area]
            acertos_area = acertos_por_area.get(area, 0)
            percentual = (acertos_area / total) * 100 if total > 0 else 0

            desempenho_por_area[area] = {
                "total": total,
                "acertos": acertos_area,
                "erros": erros_por_area.get(area, 0),
                "percentual": round(percentual, 2),
                "status": self._classificar_desempenho(percentual)
            }

        # Identificar áreas problemáticas
        areas_revisar = [
            area for area, stats in desempenho_por_area.items()
            if stats["percentual"] < 70
        ]

        # Calcular tempo médio por questão
        tempo_medio_questao = None
        if tempo_gasto_minutos:
            tempo_medio_questao = round(tempo_gasto_minutos / total_questoes, 2)

        # Montar resultado
        resultado = {
            "metadata": {
                "data_correcao": datetime.now().isoformat(),
                "tipo_simulado": simulado["metadata"]["tipo"],
                "area_simulado": simulado["metadata"]["area"],
                "tempo_gasto_minutos": tempo_gasto_minutos,
                "tempo_medio_por_questao": tempo_medio_questao
            },
            "estatisticas_gerais": {
                "total_questoes": total_questoes,
                "acertos": acertos,
                "erros": erros,
                "brancos": brancos,
                "percentual_acertos": round(percentual_acertos, 2),
                "percentual_erros": round(percentual_erros, 2),
                "percentual_brancos": round(percentual_brancos, 2),
                "classificacao": self._classificar_desempenho(percentual_acertos)
            },
            "desempenho_por_area": desempenho_por_area,
            "areas_para_revisar": areas_revisar,
            "detalhes_questoes": detalhes,
            "aprovado_60": percentual_acertos >= 60,
            "aprovado_70": percentual_acertos >= 70,
        }

        self.resultado = resultado
        return resultado

    def _classificar_desempenho(self, percentual: float) -> str:
        """Classifica o desempenho baseado no percentual"""
        if percentual >= 90:
            return "Excelente"
        elif percentual >= 75:
            return "Bom"
        elif percentual >= 60:
            return "Regular"
        else:
            return "Insuficiente"

    def gerar_relatorio_texto(self, resultado: Dict = None) -> str:
        """
        Gera relatório em formato texto

        Args:
            resultado: Dicionário com resultado (usa self.resultado se None)

        Returns:
            String com relatório formatado
        """
        if resultado is None:
            resultado = self.resultado

        stats = resultado["estatisticas_gerais"]
        meta = resultado["metadata"]

        relatorio = []
        relatorio.append("=" * 70)
        relatorio.append("RELATÓRIO DE CORREÇÃO - SIMULADO MP-SE 2025")
        relatorio.append("=" * 70)
        relatorio.append("")

        # Informações gerais
        relatorio.append(f"📅 Data da correção: {meta['data_correcao'][:10]}")
        relatorio.append(f"📝 Tipo de simulado: {meta['tipo_simulado'].title()}")
        relatorio.append(f"📚 Área: {meta['area_simulado'].title()}")

        if meta.get('tempo_gasto_minutos'):
            relatorio.append(f"⏱️  Tempo gasto: {meta['tempo_gasto_minutos']} minutos")
            relatorio.append(f"⏱️  Tempo médio/questão: {meta['tempo_medio_por_questao']:.1f} minutos")

        relatorio.append("")
        relatorio.append("-" * 70)
        relatorio.append("📊 ESTATÍSTICAS GERAIS")
        relatorio.append("-" * 70)
        relatorio.append("")

        # Estatísticas gerais
        relatorio.append(f"Total de questões:     {stats['total_questoes']}")
        relatorio.append(f"✅ Acertos:            {stats['acertos']} ({stats['percentual_acertos']:.1f}%)")
        relatorio.append(f"❌ Erros:              {stats['erros']} ({stats['percentual_erros']:.1f}%)")
        relatorio.append(f"⚪ Em branco:          {stats['brancos']} ({stats['percentual_brancos']:.1f}%)")
        relatorio.append("")
        relatorio.append(f"🎯 Classificação:      {stats['classificacao']}")
        relatorio.append(f"{'✅' if resultado['aprovado_60'] else '❌'} Nota mínima 60%:    {'SIM' if resultado['aprovado_60'] else 'NÃO'}")
        relatorio.append(f"{'✅' if resultado['aprovado_70'] else '❌'} Nota mínima 70%:    {'SIM' if resultado['aprovado_70'] else 'NÃO'}")

        relatorio.append("")
        relatorio.append("-" * 70)
        relatorio.append("📈 DESEMPENHO POR ÁREA")
        relatorio.append("-" * 70)
        relatorio.append("")

        # Desempenho por área
        for area, stats_area in sorted(
            resultado["desempenho_por_area"].items(),
            key=lambda x: x[1]["percentual"],
            reverse=True
        ):
            emoji = self._get_emoji_desempenho(stats_area["percentual"])
            relatorio.append(
                f"{emoji} {area.replace('_', ' ').title():25s} "
                f"{stats_area['acertos']}/{stats_area['total']} "
                f"({stats_area['percentual']:.1f}%) - {stats_area['status']}"
            )

        # Áreas para revisar
        if resultado["areas_para_revisar"]:
            relatorio.append("")
            relatorio.append("-" * 70)
            relatorio.append("⚠️  ÁREAS PRIORITÁRIAS PARA REVISÃO (< 70%)")
            relatorio.append("-" * 70)
            relatorio.append("")

            for area in resultado["areas_para_revisar"]:
                stats_area = resultado["desempenho_por_area"][area]
                relatorio.append(
                    f"   • {area.replace('_', ' ').title()} - "
                    f"{stats_area['percentual']:.1f}% de acerto"
                )

        # Questões erradas
        erros = [q for q in resultado["detalhes_questoes"] if q["status"] == "erro"]
        if erros:
            relatorio.append("")
            relatorio.append("-" * 70)
            relatorio.append(f"❌ QUESTÕES ERRADAS ({len(erros)} questões)")
            relatorio.append("-" * 70)
            relatorio.append("")

            for q in erros:
                relatorio.append(f"Questão {q['numero']:02d} ({q['area'].replace('_', ' ').title()})")
                relatorio.append(f"   Gabarito: {q['gabarito'].upper()}  |  Sua resposta: {q['resposta_usuario'].upper() if q['resposta_usuario'] else 'N/A'}")
                relatorio.append(f"   {q['enunciado']}")
                relatorio.append("")

        relatorio.append("=" * 70)
        relatorio.append("💡 RECOMENDAÇÕES")
        relatorio.append("=" * 70)
        relatorio.append("")

        # Gerar recomendações
        recomendacoes = self._gerar_recomendacoes(resultado)
        for rec in recomendacoes:
            relatorio.append(f"• {rec}")

        relatorio.append("")
        relatorio.append("=" * 70)
        relatorio.append("Continue estudando! Você consegue! 🚀")
        relatorio.append("=" * 70)

        return "\n".join(relatorio)

    def _get_emoji_desempenho(self, percentual: float) -> str:
        """Retorna emoji baseado no percentual"""
        if percentual >= 90:
            return "🌟"
        elif percentual >= 75:
            return "✅"
        elif percentual >= 60:
            return "⚠️ "
        else:
            return "❌"

    def _gerar_recomendacoes(self, resultado: Dict) -> List[str]:
        """Gera recomendações personalizadas baseadas no resultado"""
        recomendacoes = []
        stats = resultado["estatisticas_gerais"]
        percentual = stats["percentual_acertos"]

        # Recomendações gerais
        if percentual < 60:
            recomendacoes.append("Seu desempenho está abaixo do esperado. Intensifique os estudos!")
            recomendacoes.append("Revise todo o conteúdo programático e resolva mais exercícios")
        elif percentual < 75:
            recomendacoes.append("Bom desempenho, mas há espaço para melhorar!")
            recomendacoes.append("Foque nas áreas com desempenho < 70%")
        elif percentual < 90:
            recomendacoes.append("Ótimo desempenho! Continue assim!")
            recomendacoes.append("Faça simulados regulares para manter o ritmo")
        else:
            recomendacoes.append("Excelente! Você está muito bem preparado!")
            recomendacoes.append("Mantenha a consistência e faça revisões leves")

        # Recomendações sobre tempo
        if resultado["metadata"].get("tempo_medio_por_questao"):
            tempo = resultado["metadata"]["tempo_medio_por_questao"]
            if tempo > 5:
                recomendacoes.append(f"Você está gastando muito tempo por questão ({tempo:.1f} min). Treine velocidade!")
            elif tempo < 3:
                recomendacoes.append("Você está resolvendo muito rápido. Cuidado com erros de desatenção!")

        # Recomendações por área
        areas_problematicas = resultado["areas_para_revisar"]
        if areas_problematicas:
            if len(areas_problematicas) <= 2:
                recomendacoes.append(f"Priorize revisão em: {', '.join([a.replace('_', ' ').title() for a in areas_problematicas])}")
            else:
                recomendacoes.append(f"Muitas áreas precisam de atenção ({len(areas_problematicas)}). Crie um plano de estudos focado")

        # Questões em branco
        if stats["percentual_brancos"] > 10:
            recomendacoes.append(f"Você deixou {stats['brancos']} questões em branco. Tente responder todas!")
            recomendacoes.append("Elimine alternativas erradas e chute entre as restantes")

        return recomendacoes

    def salvar_resultado(self, caminho_saida: str = None) -> str:
        """
        Salva resultado em arquivo JSON

        Args:
            caminho_saida: Caminho do arquivo de saída

        Returns:
            Caminho do arquivo salvo
        """
        if caminho_saida is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            caminho_saida = f"resultado_{timestamp}.json"

        caminho = Path(__file__).parent / caminho_saida

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(self.resultado, f, ensure_ascii=False, indent=2)

        return str(caminho)


def main():
    """Função principal para executar via linha de comando"""
    import argparse

    parser = argparse.ArgumentParser(description='Corretor de Simulados MP-SE')
    parser.add_argument('simulado', help='Caminho para arquivo do simulado (JSON)')
    parser.add_argument('--respostas', help='Caminho para arquivo de respostas (JSON)')
    parser.add_argument('--tempo', type=int, help='Tempo gasto em minutos')
    parser.add_argument('--salvar', action='store_true', help='Salvar resultado em arquivo')

    args = parser.parse_args()

    # Criar corretor
    corretor = CorretorSimulado()

    print("📖 Carregando simulado...")
    simulado = corretor.carregar_simulado(args.simulado)

    print("📝 Carregando respostas...")
    respostas = corretor.carregar_respostas(args.respostas)

    if not respostas:
        print("❌ Nenhuma resposta fornecida. Encerrando.")
        return

    print("🔍 Corrigindo simulado...")
    resultado = corretor.corrigir(simulado, respostas, args.tempo)

    # Gerar e exibir relatório
    print("\n" + corretor.gerar_relatorio_texto(resultado))

    # Salvar resultado
    if args.salvar:
        caminho = corretor.salvar_resultado()
        print(f"\n✅ Resultado salvo em: {caminho}")


if __name__ == "__main__":
    main()
