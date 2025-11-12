# Metodologia de Preparação - MP-SE 2025
## Analista do Ministério Público - Tecnologia da Informação: Desenvolvimento

**Data das Provas:** 11 de janeiro de 2026
**Banca:** Fundação Carlos Chagas (FCC)

---

## 📚 Índice

1. [Visão Geral da Metodologia](#visão-geral-da-metodologia)
2. [Ciclo de Estudos](#ciclo-de-estudos)
3. [Sistema de Simulados](#sistema-de-simulados)
4. [Organização dos Materiais](#organização-dos-materiais)
5. [Técnicas de Estudo](#técnicas-de-estudo)
6. [Acompanhamento de Progresso](#acompanhamento-de-progresso)
7. [Revisão Espaçada](#revisão-espaçada)
8. [Cronograma Semanal](#cronograma-semanal)

---

## 1. Visão Geral da Metodologia

### 🎯 Objetivos da Metodologia

1. **Maximizar a retenção** de conhecimento através de revisão espaçada
2. **Identificar pontos fracos** através de simulados regulares
3. **Organizar materiais** de forma eficiente e acessível
4. **Medir progresso** de forma objetiva e contínua
5. **Otimizar o tempo** de estudo focando nas áreas prioritárias

### 🔄 Princípios Fundamentais

#### Ciclo PDCA Adaptado para Concursos
- **Plan (Planejar):** Definir tópicos e tempo de estudo
- **Do (Fazer):** Estudar o conteúdo e fazer exercícios
- **Check (Verificar):** Realizar simulados e avaliar desempenho
- **Act (Agir):** Revisar pontos fracos e ajustar estratégia

#### Pirâmide de Aprendizagem
- **Leitura:** 10% de retenção
- **Audiovisual:** 20% de retenção
- **Demonstração:** 30% de retenção
- **Discussão:** 50% de retenção
- **Prática:** 75% de retenção
- **Ensinar outros:** 90% de retenção

**Aplicação:** Priorizar prática (exercícios e projetos) e síntese (resumos e mapas mentais)

---

## 2. Ciclo de Estudos

### 📅 Estrutura do Ciclo (7 dias)

#### Modelo de Ciclo Completo

```
Dia 1-2: ESTUDO TEÓRICO + EXERCÍCIOS
├── Manhã: Leitura e resumos (3h)
├── Tarde: Exercícios básicos (2h)
└── Noite: Revisão do dia (1h)

Dia 3-4: APROFUNDAMENTO + PRÁTICA
├── Manhã: Conceitos avançados (3h)
├── Tarde: Projetos práticos (2h)
└── Noite: Exercícios FCC (1h)

Dia 5: SIMULADO PARCIAL
├── Manhã: Simulado (20-30 questões) (2h)
├── Tarde: Correção comentada (2h)
└── Noite: Revisão de erros (1h)

Dia 6: REVISÃO DIRECIONADA
├── Manhã: Revisar tópicos com > 30% de erro (3h)
├── Tarde: Exercícios dos tópicos fracos (2h)
└── Noite: Resumos e mapas mentais (1h)

Dia 7: DESCANSO ATIVO
├── Manhã: Revisão leve (1h)
├── Tarde: Lazer / Descanso
└── Noite: Planejamento próximo ciclo (30min)
```

### 🔢 Distribuição de Tempo por Área

Com base no peso de cada área no conteúdo programático:

| Área | Peso | Horas/Semana |
|------|------|--------------|
| **Programação e POO** | Alto | 8h |
| **Arquitetura de Software** | Alto | 7h |
| **Banco de Dados** | Alto | 6h |
| **Engenharia de Software** | Alto | 5h |
| **DevOps e CI/CD** | Médio | 4h |
| **Segurança da Informação** | Médio | 4h |
| **Governança de TI** | Médio | 3h |
| **Cloud Computing** | Médio | 3h |
| **Inteligência Artificial** | Baixo | 2h |
| **Acessibilidade Digital** | Baixo | 2h |
| **Simulados e Revisão** | - | 6h |
| **TOTAL** | - | **50h/semana** |

**Ajuste conforme seu tempo disponível:** Se tiver menos horas, reduza proporcionalmente mantendo as prioridades.

---

## 3. Sistema de Simulados

### 🎯 Tipos de Simulados

#### 3.1 Simulado Temático (Semanal)
- **Objetivo:** Avaliar aprendizado de um tema específico
- **Questões:** 15-20 questões
- **Duração:** 30-40 minutos
- **Frequência:** 1-2 por semana
- **Quando:** Após concluir estudo de um módulo

#### 3.2 Simulado Parcial (Quinzenal)
- **Objetivo:** Avaliar múltiplas áreas
- **Questões:** 30-35 questões
- **Duração:** 1h30min
- **Frequência:** 1 a cada 2 semanas
- **Quando:** Após completar 2-3 módulos

#### 3.3 Simulado Completo (Mensal)
- **Objetivo:** Simular prova real
- **Questões:** 70 questões (como a prova)
- **Duração:** 5 horas (incluindo redação)
- **Frequência:** 1 por mês
- **Quando:** Último domingo de cada mês

### 📊 Sistema de Pontuação e Análise

#### Métricas a Acompanhar

```python
# Fórmula de Aproveitamento
Aproveitamento = (Acertos / Total) × 100

# Classificação de Desempenho
- Excelente: 90-100%
- Bom: 75-89%
- Regular: 60-74%
- Insuficiente: < 60%

# Meta de Aprovação (FCC geralmente usa ~60%)
Meta Mínima: 60%
Meta Ideal: 75%
Meta Excelência: 85%
```

#### Análise Detalhada

Para cada simulado, registrar:

1. **Pontuação Geral**
   - Total de acertos
   - Percentual de acerto
   - Tempo gasto

2. **Análise por Área**
   - Acertos por disciplina
   - Disciplinas com < 60%
   - Disciplinas com > 80%

3. **Análise de Erros**
   - Tipo de erro:
     - Falta de conhecimento
     - Interpretação errada
     - Desatenção
     - Tempo insuficiente

4. **Plano de Ação**
   - Tópicos para revisar
   - Exercícios adicionais necessários
   - Ajuste no cronograma

### 🛠️ Ferramentas Desenvolvidas

#### Gerador de Simulados (`estudos/simulados/gerador_simulado.py`)
- Gera simulados automaticamente
- Baseado em banco de questões
- Distribui questões por área conforme peso
- Gera gabarito e folha de respostas

#### Corretor de Simulados (`estudos/simulados/corretor_simulado.py`)
- Corrige simulados automaticamente
- Gera relatório de desempenho
- Identifica pontos fracos
- Sugere revisões

#### Analisador de Progresso (`estudos/progresso/analisador.py`)
- Acompanha evolução ao longo do tempo
- Gera gráficos de desempenho
- Identifica tendências
- Calcula probabilidade de aprovação

---

## 4. Organização dos Materiais

### 📁 Estrutura de Diretórios

```
estudos/
├── materiais/                  # Materiais de estudo organizados por área
│   ├── engenharia-software/
│   ├── programacao/
│   ├── arquitetura/
│   ├── devops/
│   ├── seguranca/
│   ├── banco-dados/
│   ├── cloud/
│   ├── ia/
│   ├── governanca/
│   └── acessibilidade/
├── questoes/                   # Banco de questões
│   ├── resolvidas/            # Questões já resolvidas com anotações
│   ├── para-revisar/          # Questões marcadas para revisão
│   └── favoritas/             # Questões importantes
├── simulados/                  # Simulados realizados
│   ├── gerador_simulado.py    # Script gerador
│   ├── corretor_simulado.py   # Script corretor
│   └── [data]_simulado_[n].json
├── revisao/                    # Materiais de revisão
│   ├── flashcards/
│   ├── mapas-mentais/
│   └── resumos/
└── progresso/                  # Acompanhamento
    ├── analisador.py
    ├── relatorios/
    └── estatisticas.json
```

### 📝 Template de Material de Estudo

Para cada tópico, criar arquivo seguindo este template:

```markdown
# [ÁREA] - [Tópico Específico]

## 🎯 Objetivos de Aprendizagem
- [ ] Objetivo 1
- [ ] Objetivo 2

## 📖 Resumo Teórico
[Conceitos principais em bullets]

## 💡 Conceitos Chave
- **Conceito 1:** Definição e explicação
- **Conceito 2:** Definição e explicação

## 🔍 Exemplos Práticos
```código ou exemplo```

## ⚠️ Pegadinhas Comuns
- Pegadinha 1
- Pegadinha 2

## 📊 Como Cai na FCC
[Padrão de questões da banca]

## ✅ Checklist de Domínio
- [ ] Entendo o conceito teórico
- [ ] Consigo explicar para outra pessoa
- [ ] Acerto > 80% das questões do tema
- [ ] Consigo aplicar em exemplos práticos

## 🔗 Recursos Adicionais
- Link 1
- Link 2

## 📝 Notas Pessoais
[Suas anotações]

---
**Última revisão:** [Data]
**Nível de domínio:** [Iniciante/Intermediário/Avançado]
**Próxima revisão:** [Data]
```

### 🗂️ Sistema de Nomenclatura

#### Para Arquivos de Estudo
```
[ÁREA]_[número]_[tópico].md

Exemplos:
- ARQ_01_clean_architecture.md
- PROG_05_design_patterns_gof.md
- BD_03_normalizacao.md
```

#### Para Questões
```
Q_[fonte]_[ano]_[área]_[número].md

Exemplos:
- Q_FCC_2024_PROG_001.md
- Q_FCC_2023_ARQ_015.md
```

#### Para Simulados
```
SIM_[tipo]_[data]_[área].json

Exemplos:
- SIM_TEMATICO_2025-11-15_PROG.json
- SIM_COMPLETO_2025-11-30_GERAL.json
```

---

## 5. Técnicas de Estudo

### 🧠 Técnicas Comprovadas

#### 5.1 Técnica Pomodoro Adaptada
```
📚 Estudo Intenso: 50 minutos
☕ Pausa Curta: 10 minutos
(Repetir 3x)
🍽️ Pausa Longa: 30 minutos
```

**Regras:**
- Durante estudo: sem distrações (celular, redes sociais)
- Durante pausa: levantar, alongar, hidratar
- Usar timer físico ou app

#### 5.2 Método Feynman (Aprender Ensinando)
1. **Escolha um conceito** para estudar
2. **Explique como se ensinasse** uma criança de 12 anos
3. **Identifique lacunas** no seu conhecimento
4. **Revise e simplifique** até dominar

**Aplicação prática:**
- Grave vídeos explicando conceitos
- Escreva posts como se fosse tutorial
- Explique para colegas ou grupos de estudo

#### 5.3 Revisão Espaçada (Curva de Esquecimento de Ebbinghaus)

```
📚 Primeira revisão: 24 horas após estudo
📚 Segunda revisão: 7 dias após primeira
📚 Terceira revisão: 30 dias após segunda
📚 Quarta revisão: 90 dias após terceira
```

#### 5.4 Active Recall (Recuperação Ativa)

Em vez de reler passivamente:
- Faça perguntas sobre o conteúdo
- Tente lembrar sem consultar
- Use flashcards
- Resolva questões sem gabarito

#### 5.5 Elaboração e Interleaving

**Elaboração:**
- Conecte novo conhecimento com o que já sabe
- Faça analogias
- Crie exemplos próprios

**Interleaving (Intercalação):**
- Misture tópicos diferentes na mesma sessão
- Não estude um tema por muitas horas seguidas
- Alterne entre teoria e prática

### 📋 Flashcards Efetivos

#### Estrutura de um Bom Flashcard

**FRENTE:**
```
P: O que é o Princípio da Responsabilidade Única (SRP)?
Contexto: SOLID - Arquitetura de Software
```

**VERSO:**
```
R: Uma classe deve ter apenas uma razão para mudar.
Significa que cada classe deve ter apenas uma responsabilidade
ou um único trabalho/função no sistema.

Exemplo: Uma classe User não deveria ter métodos para salvar
no banco E enviar e-mail. Essas são duas responsabilidades.

Tag: #SOLID #DesignPatterns #Arquitetura
Dificuldade: ⭐⭐ (Médio)
```

#### Ferramentas Recomendadas
- **Anki** (gratuito, com algoritmo de repetição espaçada)
- **Quizlet** (interface amigável)
- **Notion** (personalizável)
- **Cartões físicos** (tátil, sem distrações digitais)

### 🗺️ Mapas Mentais

#### Quando Usar
- Visão geral de um assunto complexo
- Conectar conceitos relacionados
- Revisão rápida antes da prova
- Identificar lacunas no conhecimento

#### Ferramentas
- **XMind** (gratuito e profissional)
- **MindMeister** (colaborativo)
- **Papel e caneta** (melhor para memorização)

#### Exemplo de Estrutura

```
                        [SOLID]
                           |
        __________________|__________________
       |        |         |         |        |
      SRP      OCP       LSP       ISP      DIP
       |        |         |         |        |
   [conceito][exemplos][código][erros][questões]
```

---

## 6. Acompanhamento de Progresso

### 📈 Métricas Essenciais

#### 6.1 Cobertura de Conteúdo
```
Cobertura = (Tópicos Estudados / Total de Tópicos) × 100

Meta: 100% até 2 semanas antes da prova
```

#### 6.2 Taxa de Acerto em Questões
```
Por área:
- Taxa Geral
- Taxa por nível de dificuldade
- Evolução ao longo do tempo

Meta: > 75% em todas as áreas
```

#### 6.3 Velocidade de Resolução
```
Tempo Médio por Questão = Tempo Total / Número de Questões

Meta: < 4 minutos por questão (70 questões em 5h = ~4min/questão)
```

#### 6.4 Retenção de Conhecimento
```
Taxa de Retenção = (Acertos em Revisão / Acertos Inicial) × 100

Meta: > 85%
```

### 📊 Dashboard de Progresso

Criar planilha ou usar `estudos/progresso/analisador.py`:

```
╔══════════════════════════════════════════════════╗
║         DASHBOARD DE PROGRESSO MP-SE             ║
╠══════════════════════════════════════════════════╣
║ Dias até a prova: 45                             ║
║ Horas estudadas: 320 / 400 (80%)                 ║
║ Cobertura de conteúdo: 75%                       ║
╠══════════════════════════════════════════════════╣
║ DESEMPENHO POR ÁREA                              ║
╠══════════════════════════════════════════════════╣
║ ✅ Programação:           85% (Excelente)        ║
║ ✅ Arquitetura:           82% (Bom)              ║
║ ⚠️  Banco de Dados:       68% (Regular)          ║
║ ❌ Governança de TI:      55% (Insuficiente)     ║
║ ✅ DevOps:                78% (Bom)              ║
╠══════════════════════════════════════════════════╣
║ ÚLTIMA SEMANA                                     ║
╠══════════════════════════════════════════════════╣
║ Questões resolvidas: 150                         ║
║ Taxa de acerto: 74%                              ║
║ Simulados realizados: 2                          ║
╠══════════════════════════════════════════════════╣
║ 🎯 PRÓXIMAS AÇÕES                                ║
╠══════════════════════════════════════════════════╣
║ 1. Revisar Normalização de BD                    ║
║ 2. Resolver 50 questões de Governança            ║
║ 3. Simulado completo no domingo                  ║
╚══════════════════════════════════════════════════╝
```

### 📝 Registro Diário

Manter registro simples ao final de cada dia:

```markdown
## 2025-11-12 (Terça-feira)

### Estudado Hoje
- ✅ Design Patterns: Singleton, Factory (2h)
- ✅ Exercícios de SQL (1h30)
- ✅ ITIL v4 - Cap. 2 (1h)

### Questões Resolvidas
- Total: 25 questões
- Acertos: 19 (76%)
- Erros: 6

### Dificuldades Encontradas
- Confundi Factory Method com Abstract Factory
- Dúvidas em GROUP BY com múltiplas colunas

### Próxima Sessão
- Revisar diferenças entre Factory patterns
- Praticar mais queries com GROUP BY
- Continuar ITIL v4

### Energia/Motivação: ⭐⭐⭐⭐ (4/5)
```

---

## 7. Revisão Espaçada

### 📅 Sistema de Revisão

#### Algoritmo de Revisão (Inspirado no Anki)

```
Intervalo 1: 1 dia
Intervalo 2: 3 dias
Intervalo 3: 7 dias
Intervalo 4: 14 dias
Intervalo 5: 30 dias
Intervalo 6: 60 dias
```

#### Como Aplicar

1. **Após estudar um tópico novo:**
   - Marcar data da primeira revisão (1 dia depois)
   - Adicionar ao calendário

2. **Na revisão:**
   - Se LEMBROU BEM: próximo intervalo × 2
   - Se LEMBROU COM DIFICULDADE: mesmo intervalo
   - Se NÃO LEMBROU: voltar ao intervalo 1

3. **Ferramentas:**
   - Planilha de controle
   - App Anki
   - Script Python (`estudos/revisao/agendador.py`)

### 📚 Tipos de Revisão

#### Revisão Rápida (15-30 min)
- Ler resumos
- Ver mapas mentais
- Flashcards rápidos

#### Revisão Média (1-2h)
- Refazer exercícios
- Assistir vídeos-resumo
- Ler anotações completas

#### Revisão Profunda (3-4h)
- Reestudar conceitos difíceis
- Resolver questões inéditas
- Criar novos exemplos

---

## 8. Cronograma Semanal

### 📆 Exemplo de Semana Tipo

#### Semana com 50h de estudo (Dedicação Integral)

```
Segunda-feira (8h)
├── 06:00-07:00: Revisão do dia anterior
├── 07:00-09:00: Programação - Teoria
├── 09:00-09:15: PAUSA
├── 09:15-11:15: Programação - Exercícios
├── 11:15-12:00: ALMOÇO
├── 12:00-14:00: Arquitetura de Software
├── 14:00-14:15: PAUSA
├── 14:15-16:00: Questões FCC mistas
├── 16:00-17:00: Revisão e flashcards

Terça-feira (8h)
├── Similar structure
├── Foco: Banco de Dados e DevOps

Quarta-feira (8h)
├── Foco: Engenharia de Software e Segurança

Quinta-feira (8h)
├── Foco: Governança e Cloud

Sexta-feira (8h)
├── Manhã: Áreas com maior dificuldade
├── Tarde: Simulado temático (2h) + Correção (2h)

Sábado (6h)
├── Manhã: Inteligência Artificial e Acessibilidade
├── Tarde: Revisão geral da semana

Domingo (4h)
├── Manhã: Simulado completo (se for semana de simulado)
│   ou Revisão leve + descanso
├── Tarde: Lazer / Descanso mental
├── Noite: Planejamento da próxima semana
```

#### Semana com 30h de estudo (Meio Período)

```
Segunda a Sexta (5h/dia = 25h)
├── 19:00-20:00: Teoria da área prioritária do dia
├── 20:00-20:15: PAUSA
├── 20:15-21:45: Exercícios
├── 21:45-22:00: PAUSA
├── 22:00-23:00: Revisão e flashcards

Sábado (3h)
├── 09:00-11:00: Simulado temático
├── 11:30-12:30: Correção

Domingo (2h)
├── 10:00-12:00: Revisão dos erros + Planejamento
```

### 🎯 Distribuição Semanal por Fase

#### Fase 1: Base (Semanas 1-4)
- **70% Teoria** + 30% Questões
- Foco: Cobertura completa do conteúdo
- Simulados temáticos semanais

#### Fase 2: Consolidação (Semanas 5-7)
- **50% Teoria** + 50% Questões
- Foco: Aprofundamento e prática
- Simulados parciais quinzenais

#### Fase 3: Treinamento (Semanas 8-10)
- **30% Teoria** + 70% Questões
- Foco: Resolução massiva de questões
- Simulados completos mensais

#### Fase 4: Revisão Final (Últimas 2 semanas)
- **20% Teoria** + 80% Revisão
- Foco: Consolidar pontos fracos
- Simulados completos semanais

---

## 9. Estratégias Específicas por Área

### 💻 Programação (C#, JavaScript, TypeScript)

**Como estudar:**
- Escrever código diariamente
- Resolver desafios no HackerRank/LeetCode
- Criar projetos práticos pequenos
- Ler código de bibliotecas famosas

**Recursos:**
- Documentação oficial (Microsoft Docs, MDN)
- Livros: "C# in Depth", "You Don't Know JS"
- Praticar POO com exemplos reais

### 🏗️ Arquitetura de Software

**Como estudar:**
- Desenhar diagramas de arquitetura
- Implementar cada padrão GoF
- Comparar arquiteturas (quando usar cada uma)
- Estudar sistemas reais (case studies)

**Recursos:**
- Livro "Design Patterns" (GoF)
- Livro "Clean Architecture" (Uncle Bob)
- Refactoring.guru (padrões visuais)

### 🗄️ Banco de Dados

**Como estudar:**
- Instalar PostgreSQL e SQL Server localmente
- Praticar queries diariamente
- Modelar bases de dados reais
- Resolver exercícios de normalização

**Recursos:**
- Use the Index, Luke (performance)
- PostgreSQL Documentation
- SQL Server Documentation
- SQLZoo (exercícios online)

### 🔒 Segurança da Informação

**Como estudar:**
- Ler OWASP Top 10 completo
- Estudar casos reais de vulnerabilidades
- Praticar com labs (OWASP WebGoat)
- Entender LGPD artigo por artigo

**Recursos:**
- Site oficial OWASP
- NIST SSDF Framework
- Lei 13.709/2018 (LGPD)

### ☁️ Cloud Computing

**Como estudar:**
- Criar conta free tier (AWS, Azure, GCP)
- Praticar criação de recursos básicos
- Entender diferenças entre provedores
- Estudar casos de uso

**Recursos:**
- AWS Free Tier
- Azure Free Account
- Google Cloud Free Trial
- Documentação oficial

### 🤖 Inteligência Artificial

**Como estudar:**
- Entender conceitos teóricos (não precisa ser expert)
- Conhecer bibliotecas principais
- Entender quando usar ML vs DL
- Vocabulário técnico

**Recursos:**
- Coursera: Machine Learning (Andrew Ng)
- Scikit-learn documentation
- Tutoriais básicos de TensorFlow

### 📊 Governança de TI

**Como estudar:**
- Fazer resumos dos frameworks
- Criar comparativos (ITIL vs COBIT vs PMBOK)
- Decorar processos principais
- Resolver questões teóricas

**Recursos:**
- Livros oficiais ITIL 4
- COBIT 2019 Framework
- PMBOK 7th Edition

---

## 10. Dicas Finais e Motivação

### ✅ Do's (Faça)

1. **Consistência > Intensidade:** 2h todo dia > 14h no domingo
2. **Durma bem:** 7-8h de sono para consolidar memória
3. **Exercícios físicos:** 30min/dia melhora cognição
4. **Hidratação:** Beba água durante estudos
5. **Alimentação saudável:** Cérebro precisa de glicose
6. **Grupos de estudo:** Trocar conhecimentos
7. **Comemore pequenas vitórias:** Cada módulo concluído
8. **Mantenha equilíbrio:** Vida social e saúde mental

### ❌ Don'ts (Não faça)

1. **Não estude cansado:** Rendimento cai 70%
2. **Não compare com outros:** Cada um tem seu ritmo
3. **Não pule revisões:** Essenciais para retenção
4. **Não acumule dúvidas:** Resolva logo
5. **Não estude só teoria:** Prática é fundamental
6. **Não deixe para última semana:** Não dá tempo
7. **Não desista nos dias ruins:** Todos têm
8. **Não negligencie saúde:** Sem saúde, sem estudo

### 🎯 Mantra do Concurseiro

```
"Não é sobre ser perfeito.
É sobre ser consistente.

Não é sobre estudar 12 horas.
É sobre estudar 3 horas bem feitas.

Não é sobre acertar tudo.
É sobre acertar o suficiente.

Não é sobre não errar.
É sobre aprender com os erros.

Eu consigo. Eu vou conseguir. Eu vou passar!"
```

### 📞 Recursos e Comunidade

- **Grupos de Telegram/WhatsApp:** Buscar "Concurso MP-SE 2025"
- **Fóruns:** Qconcursos, Estratégia, Gran Cursos
- **YouTube:** Canais especializados em TI para concursos
- **Discord:** Comunidades de programadores concurseiros

---

## 📋 Checklist de Preparação Final

### 2 Semanas Antes da Prova
- [ ] Revisei todos os tópicos do conteúdo programático
- [ ] Resolvi pelo menos 500 questões
- [ ] Fiz pelo menos 3 simulados completos
- [ ] Taxa de acerto geral > 75%
- [ ] Identifiquei e revisei pontos fracos
- [ ] Tenho resumos de todas as áreas

### 1 Semana Antes da Prova
- [ ] Simulado completo com nota > 75%
- [ ] Revisei os 23 padrões GoF
- [ ] Revisei SOLID e Clean Architecture
- [ ] Revisei LGPD e OWASP Top 10
- [ ] Revisei SQL e normalização
- [ ] Revisei ITIL, COBIT e PMBOK

### 1 Dia Antes da Prova
- [ ] Revisão leve (apenas resumos)
- [ ] Separei documentos (RG, CPF, comprovante)
- [ ] Verifiquei local da prova e rota
- [ ] Preparei lanche e água
- [ ] Dormi cedo (8 horas de sono)

### Dia da Prova
- [ ] Café da manhã leve
- [ ] Cheguei 1h antes
- [ ] Li todas as questões antes de responder
- [ ] Gerenciei bem o tempo
- [ ] Mantive a calma
- [ ] Revisei respostas antes de entregar

---

## 🎓 Lembre-se

> "O sucesso é a soma de pequenos esforços repetidos dia após dia."
> — Robert Collier

Você tem todas as ferramentas necessárias. Agora é só executar o plano com disciplina e consistência!

**BOA SORTE! VOCÊ CONSEGUE! 🚀**

---

**Criado em:** 12/11/2025
**Última atualização:** 12/11/2025
**Versão:** 1.0
