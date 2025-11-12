# 📚 Sistema de Estudos - MP-SE 2025
## Analista do Ministério Público - Tecnologia da Informação: Desenvolvimento

Este diretório contém todo o sistema organizado de estudos para o concurso MP-SE 2025.

---

## 📁 Estrutura de Diretórios

```
estudos/
├── materiais/          # Materiais de estudo organizados por área
├── questoes/           # Banco de questões e resoluções
├── simulados/          # Scripts e simulados realizados
├── revisao/            # Materiais de revisão (flashcards, mapas mentais)
└── progresso/          # Acompanhamento e estatísticas
```

---

## 🚀 Como Usar Este Sistema

### 1. Estudar um Tópico Novo

```bash
# 1. Vá para a área correspondente
cd materiais/[area]

# 2. Crie ou abra o arquivo do tópico
# Siga o template fornecido em template_material.md

# 3. Após estudar, crie flashcards em estudos/revisao/flashcards/
```

### 2. Gerar um Simulado

```bash
cd simulados/

# Criar banco de questões (primeira vez)
python3 gerador_simulado.py --criar-banco

# Gerar simulado completo (70 questões)
python3 gerador_simulado.py --tipo completo

# Gerar simulado temático de uma área específica
python3 gerador_simulado.py --tipo tematico --area programacao --questoes 20

# Gerar simulado parcial (30 questões)
python3 gerador_simulado.py --tipo parcial
```

### 3. Corrigir um Simulado

```bash
cd simulados/

# Método interativo (digite respostas no terminal)
python3 corretor_simulado.py simulado_completo_geral_20251115.json --tempo 240

# Com arquivo de respostas
python3 corretor_simulado.py simulado_completo_geral_20251115.json \
    --respostas minhas_respostas.json \
    --tempo 240 \
    --salvar
```

### 4. Organizar Questões

```bash
# Questões resolvidas corretamente
cp questao.md questoes/resolvidas/

# Questões para revisar (erradas ou difíceis)
cp questao.md questoes/para-revisar/

# Questões favoritas (muito importantes)
cp questao.md questoes/favoritas/
```

---

## 📝 Templates Disponíveis

### Material de Estudo
Arquivo: `materiais/template_material.md`

Use este template para criar novos materiais de estudo organizados.

### Questão Resolvida
Arquivo: `questoes/template_questao.md`

Use este template para documentar questões com suas resoluções.

### Flashcard
Arquivo: `revisao/flashcards/template_flashcard.md`

Use este template para criar flashcards de revisão.

---

## 🎯 Workflow Recomendado

### Ciclo Semanal de Estudos

```
Segunda a Quinta (Estudo + Prática)
├── Manhã: Teoria nova (2-3h)
├── Tarde: Exercícios (2-3h)
└── Noite: Revisão e flashcards (1h)

Sexta (Avaliação)
├── Manhã: Revisão da semana (2h)
└── Tarde: Simulado temático (2h)

Sábado (Aprofundamento)
├── Manhã: Tópicos difíceis (3h)
└── Tarde: Projetos práticos (2h)

Domingo (Descanso e Planejamento)
├── Manhã: Revisão leve (1h)
└── Tarde: Descanso
└── Noite: Planejamento próxima semana (30min)
```

### Fluxo de Estudo de um Tópico

```
1. ESTUDO INICIAL
   └── Ler material teórico
   └── Fazer resumo próprio
   └── Assistir vídeo complementar (opcional)

2. PRÁTICA
   └── Resolver exercícios básicos
   └── Fazer exemplos práticos
   └── Resolver questões FCC sobre o tema

3. CONSOLIDAÇÃO
   └── Criar flashcards dos conceitos principais
   └── Fazer mapa mental
   └── Explicar para alguém (Método Feynman)

4. AVALIAÇÃO
   └── Fazer simulado temático
   └── Revisar erros
   └── Identificar lacunas

5. REVISÃO ESPAÇADA
   └── Dia 1: Revisão completa
   └── Dia 7: Revisão flashcards
   └── Dia 30: Revisão rápida
```

---

## 📊 Acompanhamento de Progresso

### Métricas Importantes

1. **Cobertura de Conteúdo**
   - Meta: 100% até 2 semanas antes da prova
   - Acompanhar em: `progresso/cobertura.md`

2. **Taxa de Acerto**
   - Meta: > 75% em todas as áreas
   - Acompanhar em: `progresso/estatisticas.json`

3. **Horas de Estudo**
   - Meta: 40-50h por semana (dedicação integral)
   - Acompanhar em: `progresso/horas.md`

4. **Questões Resolvidas**
   - Meta: > 500 questões antes da prova
   - Acompanhar em: `progresso/questoes_log.md`

### Arquivos de Acompanhamento

```bash
# Registrar sessão de estudo diária
echo "2025-11-12 | Programação | 3h | 25 questões | 80% acerto" >> progresso/log_diario.txt

# Atualizar cobertura de conteúdo
# Editar: progresso/cobertura.md

# Registrar simulado
# Automático via corretor_simulado.py --salvar
```

---

## 🎓 Áreas de Estudo

### Prioridade ALTA (mais tempo)
- 💻 **Programação** (C#, JavaScript, TypeScript, POO)
- 🏗️ **Arquitetura de Software** (Padrões, SOLID, Clean Architecture)
- 🗄️ **Banco de Dados** (SQL, PostgreSQL, SQL Server)
- 📐 **Engenharia de Software** (Metodologias, UML, BPMN)

### Prioridade MÉDIA
- 🔧 **DevOps e CI/CD** (Git, Docker, GitLab, GitHub Actions)
- 🔒 **Segurança da Informação** (LGPD, OWASP, Criptografia)
- 📊 **Governança de TI** (ITIL, COBIT, PMBOK)
- ☁️ **Computação em Nuvem** (AWS, Azure, GCP)

### Prioridade BAIXA (revisão)
- 🤖 **Inteligência Artificial** (ML, DL, Python)
- ♿ **Acessibilidade Digital** (WCAG, e-MAG)
- 🌍 **Inglês Técnico**

---

## 📚 Recursos Externos Recomendados

### Plataformas de Questões
- [QConcursos](https://www.qconcursos.com/)
- [TEC Concursos](https://www.tecconcursos.com.br/)
- [Gran Cursos Question](https://questoes.grancursosonline.com.br/)
- [Estratégia Questões](https://www.estrategiaconcursos.com.br/questoes/)

### Cursos Online
- **Estratégia Concursos** - Curso específico MP-SE
- **Gran Cursos Online** - Curso completo
- **Udemy** - Cursos de programação e tecnologia
- **Alura** - Tecnologia em geral

### Documentação Oficial
- [Microsoft Docs](https://docs.microsoft.com/) - C#, .NET, Azure
- [MDN Web Docs](https://developer.mozilla.org/) - JavaScript, TypeScript, Web
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [AWS Documentation](https://docs.aws.amazon.com/)

### Livros Essenciais
- "Clean Code" - Robert C. Martin
- "Design Patterns" - Gang of Four
- "Clean Architecture" - Robert C. Martin
- "Domain-Driven Design" - Eric Evans

### Prática de Código
- [HackerRank](https://www.hackerrank.com/)
- [LeetCode](https://leetcode.com/)
- [Exercism](https://exercism.org/)
- [CodeWars](https://www.codewars.com/)

---

## 🆘 Dicas Importantes

### ✅ Faça

1. **Estude todos os dias** - Consistência é fundamental
2. **Resolva MUITAS questões** - Mínimo 20-30 por dia
3. **Faça simulados regulares** - Pelo menos 1 por semana
4. **Revise seus erros** - Aprenda com eles
5. **Mantenha registros** - Acompanhe seu progresso
6. **Descanse adequadamente** - 7-8h de sono
7. **Cuide da saúde** - Exercícios e alimentação
8. **Participe de grupos** - Troque experiências

### ❌ Evite

1. **Estudar cansado** - Rendimento baixo
2. **Pular revisões** - Esquecimento é rápido
3. **Só ler teoria** - Prática é essencial
4. **Acumular dúvidas** - Resolva logo
5. **Comparar-se com outros** - Foque em você
6. **Procrastinar** - Disciplina é chave
7. **Negligenciar saúde** - Base para tudo
8. **Desanimar com erros** - Fazem parte do processo

---

## 🎯 Metas Semanais Sugeridas

### Semanas 1-4 (Base)
- [ ] Cobrir 70% do conteúdo programático
- [ ] Resolver 200+ questões
- [ ] Fazer 4 simulados temáticos
- [ ] Taxa de acerto > 60%

### Semanas 5-8 (Consolidação)
- [ ] Cobrir 100% do conteúdo programático
- [ ] Resolver 300+ questões
- [ ] Fazer 2 simulados parciais + 1 completo
- [ ] Taxa de acerto > 70%

### Semanas 9-10 (Treinamento Intenso)
- [ ] Resolver 400+ questões
- [ ] Fazer 2 simulados completos
- [ ] Revisar todas as áreas fracas
- [ ] Taxa de acerto > 75%

### Últimas 2 Semanas (Revisão Final)
- [ ] Revisar 100% do conteúdo
- [ ] Fazer 2-3 simulados completos
- [ ] Taxa de acerto > 80%
- [ ] Estar descansado e confiante

---

## 📞 Suporte e Comunidade

Se tiver dúvidas ou precisar de ajuda:

1. **Grupos de estudo** - Procure grupos do MP-SE 2025
2. **Fóruns especializados** - QConcursos, Estratégia
3. **Professores dos cursos** - Use o suporte das plataformas
4. **Comunidade GitHub** - Para dúvidas técnicas de programação

---

## 🎓 Lembre-se

> "A disciplina é a ponte entre metas e conquistas."
> — Jim Rohn

**Você consegue! Mantenha o foco e a consistência! 🚀**

---

**Criado em:** 12/11/2025
**Última atualização:** 12/11/2025
