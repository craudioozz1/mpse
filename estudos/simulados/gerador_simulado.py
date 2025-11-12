#!/usr/bin/env python3
"""
Gerador de Simulados - MP-SE 2025
Gera simulados personalizados baseados em banco de questões
"""

import json
import random
from datetime import datetime
from pathlib import Path
from typing import List, Dict

class GeradorSimulado:
    """Classe para gerar simulados do concurso MP-SE"""

    def __init__(self, banco_questoes_path: str = "banco_questoes.json"):
        """
        Inicializa o gerador

        Args:
            banco_questoes_path: Caminho para o arquivo JSON com questões
        """
        self.banco_questoes_path = Path(banco_questoes_path)
        self.questoes = self._carregar_questoes()

        # Distribuição de questões por área (baseado no conteúdo programático)
        self.distribuicao_completa = {
            "programacao": 15,  # C#, JS, TS, POO
            "arquitetura": 12,  # Arquitetura, padrões, SOLID
            "banco_dados": 10,  # SQL, PostgreSQL, SQL Server
            "engenharia_software": 8,  # CMMI, Scrum, UML, BPMN
            "devops": 6,  # Git, Docker, CI/CD
            "seguranca": 6,  # LGPD, OWASP, criptografia
            "governanca": 5,  # ITIL, COBIT, PMBOK
            "cloud": 4,  # AWS, Azure, GCP
            "ia": 2,  # ML, DL, Python
            "acessibilidade": 2  # WCAG, e-MAG
        }

    def _carregar_questoes(self) -> List[Dict]:
        """Carrega questões do arquivo JSON"""
        if not self.banco_questoes_path.exists():
            print(f"⚠️  Banco de questões não encontrado em {self.banco_questoes_path}")
            print("Criando banco de questões vazio...")
            return []

        with open(self.banco_questoes_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def gerar_simulado(
        self,
        tipo: str = "completo",
        area: str = None,
        num_questoes: int = None
    ) -> Dict:
        """
        Gera um simulado

        Args:
            tipo: "completo" (70q), "parcial" (30q), "tematico" (15q)
            area: Área específica para simulado temático
            num_questoes: Número de questões (sobrescreve tipo)

        Returns:
            Dicionário com o simulado gerado
        """
        # Definir número de questões
        if num_questoes is None:
            num_questoes = {
                "completo": 70,
                "parcial": 30,
                "tematico": 15
            }.get(tipo, 70)

        # Gerar simulado baseado no tipo
        if tipo == "tematico" and area:
            questoes_selecionadas = self._selecionar_questoes_area(area, num_questoes)
        else:
            questoes_selecionadas = self._selecionar_questoes_distribuidas(num_questoes)

        # Embaralhar questões
        random.shuffle(questoes_selecionadas)

        # Criar estrutura do simulado
        simulado = {
            "metadata": {
                "tipo": tipo,
                "area": area if tipo == "tematico" else "geral",
                "num_questoes": num_questoes,
                "data_geracao": datetime.now().isoformat(),
                "duracao_sugerida_minutos": num_questoes * 4  # 4 min por questão
            },
            "questoes": [
                {
                    "numero": i + 1,
                    "id_questao": q.get("id", f"Q{i+1}"),
                    "area": q.get("area", "geral"),
                    "enunciado": q.get("enunciado", ""),
                    "alternativas": q.get("alternativas", []),
                    "gabarito": q.get("gabarito", ""),
                    "dificuldade": q.get("dificuldade", "media"),
                    "tags": q.get("tags", [])
                }
                for i, q in enumerate(questoes_selecionadas)
            ],
            "respostas_usuario": {},
            "resultado": None
        }

        return simulado

    def _selecionar_questoes_area(self, area: str, num: int) -> List[Dict]:
        """Seleciona questões de uma área específica"""
        questoes_area = [q for q in self.questoes if q.get("area") == area]

        if len(questoes_area) < num:
            print(f"⚠️  Apenas {len(questoes_area)} questões disponíveis para {area}")
            return questoes_area

        return random.sample(questoes_area, num)

    def _selecionar_questoes_distribuidas(self, num_total: int) -> List[Dict]:
        """Seleciona questões distribuídas proporcionalmente por área"""
        questoes_selecionadas = []

        # Calcular proporção
        total_distribuicao = sum(self.distribuicao_completa.values())

        for area, num_ideal in self.distribuicao_completa.items():
            # Calcular quantas questões desta área
            num_area = int((num_ideal / total_distribuicao) * num_total)

            # Selecionar questões
            questoes_area = [q for q in self.questoes if q.get("area") == area]

            if len(questoes_area) >= num_area:
                questoes_selecionadas.extend(random.sample(questoes_area, num_area))
            else:
                questoes_selecionadas.extend(questoes_area)

        # Se não atingiu o número total, preencher com questões aleatórias
        while len(questoes_selecionadas) < num_total and len(self.questoes) > 0:
            questao_extra = random.choice(self.questoes)
            if questao_extra not in questoes_selecionadas:
                questoes_selecionadas.append(questao_extra)

        return questoes_selecionadas[:num_total]

    def salvar_simulado(self, simulado: Dict, nome_arquivo: str = None) -> str:
        """
        Salva simulado em arquivo JSON

        Args:
            simulado: Dicionário com o simulado
            nome_arquivo: Nome do arquivo (opcional)

        Returns:
            Caminho do arquivo salvo
        """
        if nome_arquivo is None:
            tipo = simulado["metadata"]["tipo"]
            data = datetime.now().strftime("%Y%m%d_%H%M%S")
            area = simulado["metadata"].get("area", "geral")
            nome_arquivo = f"simulado_{tipo}_{area}_{data}.json"

        caminho = Path(__file__).parent / nome_arquivo

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(simulado, f, ensure_ascii=False, indent=2)

        return str(caminho)

    def gerar_folha_respostas(self, simulado: Dict, formato: str = "txt") -> str:
        """
        Gera folha de respostas para impressão

        Args:
            simulado: Dicionário com o simulado
            formato: "txt" ou "md"

        Returns:
            String com a folha de respostas formatada
        """
        num_questoes = simulado["metadata"]["num_questoes"]
        tipo = simulado["metadata"]["tipo"]

        if formato == "md":
            folha = f"# Folha de Respostas - Simulado {tipo.title()}\n\n"
            folha += f"**Data:** {datetime.now().strftime('%d/%m/%Y')}\n"
            folha += f"**Total de questões:** {num_questoes}\n\n"
            folha += "| Q | Resposta | Q | Resposta | Q | Resposta | Q | Resposta |\n"
            folha += "|---|----------|---|----------|---|----------|---|---------|\n"

            for i in range(0, num_questoes, 4):
                linha = ""
                for j in range(4):
                    q_num = i + j + 1
                    if q_num <= num_questoes:
                        linha += f"| {q_num:02d} | ___ "
                    else:
                        linha += "| | "
                linha += "|\n"
                folha += linha
        else:
            folha = f"{'='*60}\n"
            folha += f"FOLHA DE RESPOSTAS - SIMULADO {tipo.upper()}\n"
            folha += f"Data: {datetime.now().strftime('%d/%m/%Y')}\n"
            folha += f"Total de questões: {num_questoes}\n"
            folha += f"{'='*60}\n\n"

            for i in range(num_questoes):
                q_num = i + 1
                folha += f"Questão {q_num:02d}: _____    "
                if (i + 1) % 4 == 0:
                    folha += "\n"

            folha += f"\n\n{'='*60}\n"

        return folha

    def criar_banco_questoes_exemplo(self):
        """Cria um banco de questões exemplo para demonstração"""
        questoes_exemplo = [
            {
                "id": "Q001",
                "area": "programacao",
                "enunciado": "Qual dos princípios SOLID estabelece que uma classe deve ter apenas uma razão para mudar?",
                "alternativas": [
                    "a) Open/Closed Principle",
                    "b) Single Responsibility Principle",
                    "c) Liskov Substitution Principle",
                    "d) Interface Segregation Principle",
                    "e) Dependency Inversion Principle"
                ],
                "gabarito": "b",
                "dificuldade": "facil",
                "tags": ["SOLID", "POO", "design"]
            },
            {
                "id": "Q002",
                "area": "arquitetura",
                "enunciado": "O padrão de projeto Singleton tem como objetivo:",
                "alternativas": [
                    "a) Permitir a criação de famílias de objetos relacionados",
                    "b) Garantir que uma classe tenha apenas uma instância",
                    "c) Separar a abstração da implementação",
                    "d) Adicionar responsabilidades a objetos dinamicamente",
                    "e) Fornecer uma interface para criar objetos"
                ],
                "gabarito": "b",
                "dificuldade": "facil",
                "tags": ["design_patterns", "criacional", "singleton"]
            },
            {
                "id": "Q003",
                "area": "banco_dados",
                "enunciado": "Em normalização de banco de dados, a Segunda Forma Normal (2FN) estabelece que:",
                "alternativas": [
                    "a) Não devem existir atributos multivalorados",
                    "b) Todos os atributos não-chave devem depender da chave primária completa",
                    "c) Não devem existir dependências transitivas",
                    "d) Toda chave candidata deve ser única",
                    "e) Não devem existir valores nulos"
                ],
                "gabarito": "b",
                "dificuldade": "media",
                "tags": ["normalizacao", "modelagem", "2FN"]
            }
        ]

        with open(self.banco_questoes_path, 'w', encoding='utf-8') as f:
            json.dump(questoes_exemplo, f, ensure_ascii=False, indent=2)

        print(f"✅ Banco de questões exemplo criado em {self.banco_questoes_path}")


def main():
    """Função principal para executar via linha de comando"""
    import argparse

    parser = argparse.ArgumentParser(description='Gerador de Simulados MP-SE')
    parser.add_argument('--tipo', choices=['completo', 'parcial', 'tematico'],
                       default='completo', help='Tipo de simulado')
    parser.add_argument('--area', type=str, help='Área para simulado temático')
    parser.add_argument('--questoes', type=int, help='Número de questões')
    parser.add_argument('--criar-banco', action='store_true',
                       help='Criar banco de questões exemplo')

    args = parser.parse_args()

    gerador = GeradorSimulado()

    if args.criar_banco:
        gerador.criar_banco_questoes_exemplo()
        return

    # Gerar simulado
    print(f"🎯 Gerando simulado {args.tipo}...")
    simulado = gerador.gerar_simulado(
        tipo=args.tipo,
        area=args.area,
        num_questoes=args.questoes
    )

    # Salvar simulado
    caminho = gerador.salvar_simulado(simulado)
    print(f"✅ Simulado salvo em: {caminho}")

    # Gerar folha de respostas
    folha = gerador.gerar_folha_respostas(simulado, formato="txt")
    caminho_folha = caminho.replace('.json', '_folha_respostas.txt')
    with open(caminho_folha, 'w', encoding='utf-8') as f:
        f.write(folha)
    print(f"✅ Folha de respostas salva em: {caminho_folha}")

    print(f"\n📊 Resumo do simulado:")
    print(f"   Tipo: {simulado['metadata']['tipo']}")
    print(f"   Área: {simulado['metadata']['area']}")
    print(f"   Questões: {simulado['metadata']['num_questoes']}")
    print(f"   Duração sugerida: {simulado['metadata']['duracao_sugerida_minutos']} minutos")


if __name__ == "__main__":
    main()
