# Guia Rápido - Sistema de Preparação MP-SE 2025

## 🎯 Visão Geral

Este repositório contém um **sistema completo de preparação** para o concurso MP-SE 2025, incluindo:

- ✅ Metodologia de estudos estruturada
- ✅ Sistema automatizado de simulados
- ✅ Templates para organização de materiais
- ✅ Ferramentas de acompanhamento de progresso
- ✅ Conteúdo programático completo e detalhado

---

## 📚 Documentos Principais

### 1. Informações do Concurso
- **[CONCURSO_MP_SE_2025.md](./CONCURSO_MP_SE_2025.md)** - Informações gerais, cronograma, vagas

### 2. Conteúdo Programático
- **[CONTEUDO_PROGRAMATICO_ANALISTA_TI_DESENVOLVIMENTO.md](./CONTEUDO_PROGRAMATICO_ANALISTA_TI_DESENVOLVIMENTO.md)** - Conteúdo completo e detalhado

### 3. Metodologia de Estudos
- **[METODOLOGIA_PREPARACAO.md](./METODOLOGIA_PREPARACAO.md)** - Guia completo de como estudar

### 4. Sistema de Estudos
- **[estudos/README.md](./estudos/README.md)** - Instruções do sistema de estudos

---

## 🚀 Como Começar

### Passo 1: Entenda o Concurso
```bash
# Leia as informações do concurso
cat CONCURSO_MP_SE_2025.md
```

### Passo 2: Conheça o Conteúdo
```bash
# Leia o conteúdo programático completo
cat CONTEUDO_PROGRAMATICO_ANALISTA_TI_DESENVOLVIMENTO.md
```

### Passo 3: Estude a Metodologia
```bash
# Leia a metodologia de preparação
cat METODOLOGIA_PREPARACAO.md
```

### Passo 4: Configure Seu Ambiente de Estudos
```bash
# Entre no diretório de estudos
cd estudos/

# Leia o README
cat README.md
```

---

## 🎓 Como Usar o Sistema de Simulados

### 1. Gerar um Simulado

```bash
cd estudos/simulados/

# Simulado completo (70 questões - como a prova real)
python3 gerador_simulado.py --tipo completo

# Simulado parcial (30 questões)
python3 gerador_simulado.py --tipo parcial

# Simulado temático de uma área específica (20 questões)
python3 gerador_simulado.py --tipo tematico --area programacao --questoes 20
```

**Áreas disponíveis:**
- `programacao` - C#, JavaScript, TypeScript, POO
- `arquitetura` - Padrões de projeto, SOLID, Clean Architecture
- `banco_dados` - SQL, PostgreSQL, SQL Server
- `engenharia_software` - Scrum, UML, BPMN
- `devops` - Git, Docker, CI/CD
- `seguranca` - LGPD, OWASP, Criptografia
- `governanca` - ITIL, COBIT, PMBOK
- `cloud` - AWS, Azure, GCP
- `ia` - Machine Learning, Deep Learning
- `acessibilidade` - WCAG, e-MAG

### 2. Resolver o Simulado

Após gerar, você receberá:
- **Arquivo JSON** com o simulado
- **Folha de respostas** para preencher

Resolva as questões e anote suas respostas na folha.

### 3. Corrigir o Simulado

```bash
# Correção interativa (digite respostas no terminal)
python3 corretor_simulado.py simulado_completo_geral_20251112.json --tempo 240

# Com arquivo de respostas JSON
python3 corretor_simulado.py simulado_completo_geral_20251112.json \
    --respostas minhas_respostas.json \
    --tempo 240 \
    --salvar
```

Você receberá um relatório completo com:
- ✅ Estatísticas gerais (acertos, erros, % de acerto)
- 📊 Desempenho por área
- ❌ Questões erradas com explicações
- 💡 Recomendações personalizadas

---

## 📝 Como Organizar Seus Estudos

### Estrutura Recomendada

```
1. SEGUNDA-FEIRA
   └── Manhã: Estudo teórico de Programação (3h)
   └── Tarde: Exercícios práticos (2h)
   └── Noite: Revisão e flashcards (1h)

2. TERÇA-FEIRA
   └── Manhã: Estudo teórico de Arquitetura (3h)
   └── Tarde: Questões FCC (2h)
   └── Noite: Revisão (1h)

3. QUARTA-FEIRA
   └── Manhã: Banco de Dados (3h)
   └── Tarde: Prática SQL (2h)
   └── Noite: Revisão (1h)

4. QUINTA-FEIRA
   └── Manhã: Engenharia de Software (3h)
   └── Tarde: Questões mistas (2h)
   └── Noite: Revisão (1h)

5. SEXTA-FEIRA
   └── Manhã: Revisão da semana (2h)
   └── Tarde: Simulado temático (2h)
   └── Noite: Correção e análise (1h)

6. SÁBADO
   └── Manhã: Tópicos difíceis (3h)
   └── Tarde: DevOps e Segurança (2h)

7. DOMINGO
   └── Manhã: Revisão leve (1h)
   └── Tarde: Descanso
   └── Noite: Planejamento próxima semana (30min)
```

---

## 📊 Templates Disponíveis

### 1. Material de Estudo
Arquivo: `estudos/materiais/template_material.md`

**Exemplo criado:**
- `estudos/materiais/arquitetura/ARQ_01_solid_srp.md`

### 2. Banco de Questões
Arquivo: `estudos/simulados/banco_questoes.json`

Adicione suas próprias questões seguindo o formato:
```json
{
  "id": "Q999",
  "area": "programacao",
  "enunciado": "Qual o conceito de...",
  "alternativas": [
    "a) Opção 1",
    "b) Opção 2",
    "c) Opção 3",
    "d) Opção 4",
    "e) Opção 5"
  ],
  "gabarito": "c",
  "dificuldade": "media",
  "tags": ["tag1", "tag2"]
}
```

---

## 🎯 Metas e Acompanhamento

### Metas Semanais

| Semana | Cobertura | Questões | Simulados | Taxa Acerto |
|--------|-----------|----------|-----------|-------------|
| 1-4 | 70% | 200+ | 4 temáticos | > 60% |
| 5-8 | 100% | 300+ | 2 parciais | > 70% |
| 9-10 | 100% | 400+ | 2 completos | > 75% |
| 11-12 | Revisão | 200+ | 3 completos | > 80% |

### Como Acompanhar

```bash
# Criar arquivo de log diário
echo "2025-11-12 | Programação | 3h | 25q | 80%" >> estudos/progresso/log_diario.txt

# Registrar simulado
# Automático via corretor_simulado.py --salvar
```

---

## 🛠️ Ferramentas e Scripts

### Gerador de Simulados
- **Arquivo:** `estudos/simulados/gerador_simulado.py`
- **Função:** Gera simulados personalizados

### Corretor de Simulados
- **Arquivo:** `estudos/simulados/corretor_simulado.py`
- **Função:** Corrige e gera relatórios detalhados

### Banco de Questões
- **Arquivo:** `estudos/simulados/banco_questoes.json`
- **Função:** Armazena todas as questões
- **Atual:** 20 questões exemplo

---

## 📚 Recursos Externos

### Plataformas de Questões
- [QConcursos](https://www.qconcursos.com/)
- [TEC Concursos](https://www.tecconcursos.com.br/)
- [Estratégia Questões](https://www.estrategiaconcursos.com.br/questoes/)

### Cursos
- **Estratégia Concursos** - Curso MP-SE específico
- **Gran Cursos** - Pacote completo
- **Udemy** - Cursos de tecnologia

### Documentação
- [Microsoft Docs](https://docs.microsoft.com/) - C#, .NET
- [MDN Web Docs](https://developer.mozilla.org/) - JavaScript
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

### Prática de Código
- [HackerRank](https://www.hackerrank.com/)
- [LeetCode](https://leetcode.com/)
- [Exercism](https://exercism.org/)

---

## ⚡ Comandos Rápidos

```bash
# Gerar simulado completo
cd estudos/simulados && python3 gerador_simulado.py --tipo completo

# Gerar simulado de programação (20 questões)
python3 gerador_simulado.py --tipo tematico --area programacao --questoes 20

# Corrigir simulado
python3 corretor_simulado.py simulado_XXX.json --tempo 120

# Ver estrutura de estudos
cd estudos && cat README.md

# Ver metodologia
cd .. && cat METODOLOGIA_PREPARACAO.md
```

---

## 📞 Próximos Passos

1. **[✓] Ler este guia** - Você está aqui!
2. **[ ] Ler a metodologia completa** - `METODOLOGIA_PREPARACAO.md`
3. **[ ] Ver conteúdo programático** - `CONTEUDO_PROGRAMATICO_ANALISTA_TI_DESENVOLVIMENTO.md`
4. **[ ] Criar seu plano de estudos** - Baseado na metodologia
5. **[ ] Gerar primeiro simulado** - Para avaliar nível atual
6. **[ ] Começar os estudos** - Foco e disciplina!

---

## 🎓 Dicas Finais

### ✅ Faça
- Estude todos os dias (consistência > intensidade)
- Resolva MUITAS questões (mínimo 20-30/dia)
- Faça simulados semanais
- Revise seus erros
- Durma bem (7-8h)

### ❌ Evite
- Estudar cansado
- Pular revisões
- Só teoria (prática é essencial)
- Comparar-se com outros
- Procrastinar

---

## 💪 Motivação

> **"O sucesso é a soma de pequenos esforços repetidos dia após dia."**
> — Robert Collier

**Você tem todas as ferramentas. Agora é só executar!** 🚀

---

## 📅 Informações Importantes

- **Data das Provas:** 11 de janeiro de 2026
- **Banca:** Fundação Carlos Chagas (FCC)
- **Vagas:** 28 + Cadastro Reserva
- **Salário:** Até R$ 12.378,05

---

**BOA SORTE E BONS ESTUDOS!** 📚✨

---

*Criado em: 12/11/2025*
*Versão: 1.0*
