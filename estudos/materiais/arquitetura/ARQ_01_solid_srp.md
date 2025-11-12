# Arquitetura de Software - SOLID: Single Responsibility Principle (SRP)

**Data de criação:** 12/11/2025
**Última revisão:** 12/11/2025
**Nível de domínio:** [X] Iniciante [ ] Intermediário [ ] Avançado
**Próxima revisão:** 19/11/2025

---

## 🎯 Objetivos de Aprendizagem

Ao final deste estudo, você deve ser capaz de:

- [X] Definir o que é o Princípio da Responsabilidade Única
- [X] Explicar por que SRP é importante na arquitetura de software
- [X] Identificar violações do SRP em código
- [X] Refatorar código para seguir o SRP
- [ ] Acertar > 90% das questões sobre SRP

---

## 📖 Resumo Teórico

### Definição

**Single Responsibility Principle (SRP)** ou **Princípio da Responsabilidade Única** é o primeiro princípio do SOLID que estabelece:

> "Uma classe deve ter apenas uma razão para mudar."

Em outras palavras: **Cada classe deve ter apenas uma responsabilidade ou um único trabalho/função no sistema.**

### Contexto

O SRP foi definido por Robert C. Martin (Uncle Bob) como parte dos princípios SOLID para design orientado a objetos. É fundamental para:
- Criar código mais manutenível
- Facilitar testes unitários
- Reduzir acoplamento entre classes
- Melhorar a coesão do código

### Características Principais

1. **Uma Única Responsabilidade**
   - Cada classe tem apenas um motivo para existir
   - Exemplo: Uma classe `User` só gerencia dados do usuário, não envia e-mails

2. **Uma Única Razão Para Mudar**
   - Se houver mudança em como salvamos no banco, só a classe de persistência muda
   - Se houver mudança no formato de e-mail, só a classe de e-mail muda

3. **Alta Coesão**
   - Todos os métodos da classe trabalham para o mesmo objetivo
   - Não há métodos "soltos" sem relação com a responsabilidade principal

---

## 💡 Conceitos Chave

### Conceito 1: Responsabilidade

**Definição:**
Responsabilidade é a razão de ser de uma classe. É o "trabalho" que ela deve fazer no sistema.

**Importância:**
Quando uma classe tem múltiplas responsabilidades, mudanças em uma responsabilidade podem afetar as outras, criando efeitos colaterais indesejados.

**Exemplo:**
```csharp
// ❌ VIOLAÇÃO do SRP - Múltiplas responsabilidades
public class User
{
    public string Name { get; set; }
    public string Email { get; set; }

    // Responsabilidade 1: Validar dados
    public bool ValidateEmail()
    {
        return Email.Contains("@");
    }

    // Responsabilidade 2: Salvar no banco
    public void SaveToDatabase()
    {
        // Código SQL...
    }

    // Responsabilidade 3: Enviar e-mail
    public void SendWelcomeEmail()
    {
        // Código SMTP...
    }
}

// ✅ SEGUINDO o SRP - Uma responsabilidade por classe
public class User
{
    public string Name { get; set; }
    public string Email { get; set; }
}

public class UserValidator
{
    public bool ValidateEmail(string email)
    {
        return email.Contains("@");
    }
}

public class UserRepository
{
    public void Save(User user)
    {
        // Código SQL...
    }
}

public class EmailService
{
    public void SendWelcomeEmail(User user)
    {
        // Código SMTP...
    }
}
```

### Conceito 2: Coesão

**Definição:**
Coesão mede o quanto os métodos e atributos de uma classe estão relacionados à responsabilidade da classe.

**Relação com SRP:**
Alta coesão = métodos trabalham juntos para uma única responsabilidade
Baixa coesão = métodos fazem coisas não relacionadas (viola SRP)

**Exemplo:**
```javascript
// ❌ Baixa coesão - Métodos não relacionados
class Report {
    generateReport() { /* ... */ }
    printReport() { /* ... */ }
    saveToFile() { /* ... */ }
    sendByEmail() { /* ... */ }
    formatToPDF() { /* ... */ }
}

// ✅ Alta coesão - Cada classe com sua responsabilidade
class ReportGenerator {
    generateReport() { /* ... */ }
}

class ReportPrinter {
    print(report) { /* ... */ }
}

class ReportSaver {
    saveToFile(report, filename) { /* ... */ }
}

class EmailSender {
    sendReport(report, recipient) { /* ... */ }
}

class PDFFormatter {
    format(report) { /* ... */ }
}
```

---

## 🔍 Exemplos Práticos

### Exemplo 1: Sistema de E-commerce

**Problema:**
Uma classe `Order` que faz muitas coisas:

```csharp
// ❌ VIOLAÇÃO do SRP
public class Order
{
    public List<Item> Items { get; set; }
    public decimal Total { get; set; }

    public void CalculateTotal()
    {
        // Calcula o total do pedido
    }

    public void SaveToDatabase()
    {
        // Salva no banco de dados
    }

    public void SendConfirmationEmail()
    {
        // Envia e-mail de confirmação
    }

    public void GenerateInvoicePDF()
    {
        // Gera PDF da nota fiscal
    }

    public void ProcessPayment()
    {
        // Processa pagamento
    }
}
```

**Solução:**
```csharp
// ✅ SEGUINDO o SRP

// Responsabilidade: Representar um pedido
public class Order
{
    public List<Item> Items { get; set; }
    public decimal Total { get; set; }
    public DateTime OrderDate { get; set; }
}

// Responsabilidade: Calcular valores do pedido
public class OrderCalculator
{
    public decimal CalculateTotal(Order order)
    {
        return order.Items.Sum(item => item.Price * item.Quantity);
    }
}

// Responsabilidade: Persistir pedidos
public class OrderRepository
{
    public void Save(Order order)
    {
        // Lógica de persistência
    }
}

// Responsabilidade: Enviar e-mails
public class OrderEmailService
{
    public void SendConfirmation(Order order)
    {
        // Lógica de envio de e-mail
    }
}

// Responsabilidade: Gerar documentos
public class InvoiceGenerator
{
    public byte[] GeneratePDF(Order order)
    {
        // Lógica de geração de PDF
    }
}

// Responsabilidade: Processar pagamentos
public class PaymentProcessor
{
    public bool ProcessPayment(Order order, PaymentMethod method)
    {
        // Lógica de pagamento
    }
}
```

**Explicação:**
Agora cada classe tem apenas uma razão para mudar:
- `Order` muda apenas se a estrutura de um pedido mudar
- `OrderRepository` muda apenas se mudar o banco de dados
- `OrderEmailService` muda apenas se mudar o formato ou provedor de e-mail
- `InvoiceGenerator` muda apenas se mudar o formato da nota fiscal
- `PaymentProcessor` muda apenas se mudar o gateway de pagamento

### Exemplo 2: Sistema de Logging

**Problema:**
```typescript
// ❌ VIOLAÇÃO do SRP
class Logger {
    log(message: string): void {
        // Formata a mensagem
        const timestamp = new Date().toISOString();
        const formatted = `[${timestamp}] ${message}`;

        // Salva em arquivo
        fs.appendFileSync('log.txt', formatted + '\n');

        // Envia para servidor remoto
        axios.post('https://logs.example.com', { message: formatted });

        // Exibe no console
        console.log(formatted);
    }
}
```

**Solução:**
```typescript
// ✅ SEGUINDO o SRP

// Responsabilidade: Formatação
class LogFormatter {
    format(message: string): string {
        const timestamp = new Date().toISOString();
        return `[${timestamp}] ${message}`;
    }
}

// Responsabilidade: Destino arquivo
class FileLogWriter {
    write(message: string): void {
        fs.appendFileSync('log.txt', message + '\n');
    }
}

// Responsabilidade: Destino remoto
class RemoteLogWriter {
    async write(message: string): Promise<void> {
        await axios.post('https://logs.example.com', { message });
    }
}

// Responsabilidade: Destino console
class ConsoleLogWriter {
    write(message: string): void {
        console.log(message);
    }
}

// Coordenador (Facade pattern)
class Logger {
    constructor(
        private formatter: LogFormatter,
        private writers: LogWriter[]
    ) {}

    log(message: string): void {
        const formatted = this.formatter.format(message);
        this.writers.forEach(writer => writer.write(formatted));
    }
}

// Uso
const logger = new Logger(
    new LogFormatter(),
    [
        new FileLogWriter(),
        new RemoteLogWriter(),
        new ConsoleLogWriter()
    ]
);
```

---

## ⚠️ Pegadinhas Comuns

### Pegadinha 1: Confundir Responsabilidade com Método

**Erro comum:**
Pensar que "uma responsabilidade = um método"

**Por que está errado:**
Uma responsabilidade pode envolver múltiplos métodos desde que todos trabalhem para o mesmo objetivo.

**Forma correta:**
```csharp
// ✅ CORRETO - Múltiplos métodos, uma responsabilidade
public class UserValidator
{
    public bool ValidateEmail(string email) { /* ... */ }
    public bool ValidateName(string name) { /* ... */ }
    public bool ValidateAge(int age) { /* ... */ }

    // Todos os métodos têm a mesma responsabilidade: VALIDAÇÃO
}
```

### Pegadinha 2: Divisão Excessiva

**Confusão comum:**
Criar classes demais e tornar o sistema muito complexo

**Diferença:**
| SRP Balanceado | Divisão Excessiva |
|----------------|-------------------|
| Classes coesas com responsabilidade clara | Classe para cada método |
| Fácil de entender | Difícil de navegar |
| Facilita manutenção | Aumenta complexidade |

**Exemplo:**
```csharp
// ❌ DIVISÃO EXCESSIVA
public class UserNameGetter { }
public class UserNameSetter { }
public class UserEmailGetter { }
public class UserEmailSetter { }

// ✅ SRP BALANCEADO
public class User {
    public string Name { get; set; }
    public string Email { get; set; }
}
```

---

## 📊 Como Cai na FCC

### Padrão de Questões

**Características das questões da FCC sobre SRP:**
- Tipo 1: Identificar violações do SRP em código
- Tipo 2: Escolher a refatoração correta
- Tipo 3: Definição teórica do princípio

### Palavras-chave Frequentes

- "uma única responsabilidade"
- "razão para mudar"
- "coesão"
- "separação de interesses" (separation of concerns)

### Questões Exemplo

#### Questão 1 (Fácil)

O Princípio da Responsabilidade Única (SRP) do SOLID estabelece que:

a) Uma classe deve ter apenas um método público.
b) Uma classe deve ter apenas uma razão para mudar. ✓
c) Uma classe deve herdar de apenas uma classe base.
d) Uma classe deve implementar apenas uma interface.
e) Uma classe deve ter apenas um construtor.

**Gabarito:** B

**Explicação:**
O SRP define que uma classe deve ter apenas uma responsabilidade, o que significa que deve ter apenas uma razão para mudar. As outras alternativas são incorretas:
- A) Número de métodos não define responsabilidade
- C) Refere-se a herança múltipla, não a SRP
- D) Refere-se a interfaces, não a responsabilidade
- E) Construtores não definem responsabilidade

#### Questão 2 (Média)

Analise o código abaixo:

```csharp
public class Relatorio {
    public void GerarRelatorio() { }
    public void SalvarEmArquivo() { }
    public void EnviarPorEmail() { }
    public void ImprimirRelatorio() { }
}
```

Considerando o princípio SRP, qual refatoração está correta?

a) Criar classe base abstrata para Relatorio
b) Separar em classes: GerarRelatorio, SalvarRelatorio, EmailRelatorio, ImprimirRelatorio ✓
c) Adicionar mais métodos à classe Relatorio
d) Transformar Relatorio em interface
e) Usar herança múltipla para separar responsabilidades

**Gabarito:** B

**Explicação:**
A classe Relatorio tem 4 responsabilidades diferentes (gerar, salvar, enviar por e-mail, imprimir). A refatoração correta é separar cada responsabilidade em uma classe específica.

---

## 🔄 Relações com Outros Tópicos

### Pré-requisitos

Para entender este tópico, você deve conhecer:
- [X] Programação Orientada a Objetos - `../programacao/PROG_01_poo_basico.md`
- [X] Classes e Objetos - `../programacao/PROG_02_classes.md`

### Tópicos Relacionados

Este tópico se relaciona com:
- **Open/Closed Principle (OCP)**: SRP facilita extensão sem modificação
- **Dependency Inversion (DIP)**: Classes com SRP são mais fáceis de inverter dependências
- **Design Patterns**: Muitos patterns aplicam SRP (Repository, Service, etc.)

### Próximos Passos

Após dominar este tópico, estude:
- [ ] Open/Closed Principle - `ARQ_02_solid_ocp.md`
- [ ] Liskov Substitution Principle - `ARQ_03_solid_lsp.md`
- [ ] Interface Segregation Principle - `ARQ_04_solid_isp.md`
- [ ] Dependency Inversion Principle - `ARQ_05_solid_dip.md`

---

## ✅ Checklist de Domínio

### Nível Básico (Iniciante)
- [X] Consigo definir o conceito com minhas próprias palavras
- [X] Entendo quando este conceito é aplicado
- [X] Reconheço o conceito em questões

### Nível Intermediário
- [ ] Consigo explicar o conceito para outra pessoa
- [ ] Identifico diferenças e semelhanças com outros princípios SOLID
- [ ] Acerto > 70% das questões sobre este tema
- [ ] Consigo criar exemplos próprios

### Nível Avançado (Domínio Completo)
- [ ] Posso ensinar este conceito
- [ ] Acerto > 90% das questões sobre este tema
- [ ] Consigo aplicar o conceito em problemas complexos
- [ ] Identifico violações de SRP em código real

**Meu nível atual:** [X] Iniciante [ ] Intermediário [ ] Avançado

---

## 📚 Recursos Adicionais

### Documentação Oficial
- [SOLID Principles - Wikipedia](https://en.wikipedia.org/wiki/SOLID)
- [Clean Code Blog - Uncle Bob](https://blog.cleancoder.com/)

### Artigos e Tutoriais
- [The Single Responsibility Principle - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
- [Understanding SOLID Principles - Medium](https://medium.com/@cramirez92/s-o-l-i-d-the-first-5-principles-of-object-oriented-design-with-javascript-790f6ac9b9fa)

### Vídeos
- [SOLID Principles - Código Fonte TV](https://www.youtube.com/watch?v=6SfrO3D4dHM)
- [SRP Explained - Programming with Mosh](https://www.youtube.com/watch?v=rtmFCcjEgEw)

### Livros
- **Clean Code** - Robert C. Martin - Capítulo 10
- **Clean Architecture** - Robert C. Martin - Capítulo 7
- **Agile Software Development** - Robert C. Martin

### Prática
- Refatorar código legado identificando violações de SRP
- Revisar seus próprios projetos aplicando SRP

---

## 📝 Notas Pessoais

### Insights e Descobertas

- SRP não significa "uma classe = um método", mas "uma classe = uma responsabilidade"
- A chave é perguntar: "Quantas razões esta classe tem para mudar?"
- SRP torna o código mais testável (posso testar cada responsabilidade isoladamente)

### Dúvidas Resolvidas

**Dúvida 1:** Como saber se estou dividindo demais?
**Resposta:** Se a classe resultante não faz sentido sozinha ou tem nome muito genérico (como "Manager", "Handler"), provavelmente dividiu demais.

**Dúvida 2:** Getters e setters violam SRP?
**Resposta:** Não, pois são parte da responsabilidade de gerenciar o estado do objeto.

### Dúvidas Pendentes

- [ ] Como aplicar SRP em sistemas legados sem refatorar tudo?
- [ ] SRP se aplica a microserviços? Como?

---

## 📅 Histórico de Revisões

| Data | Ação | Observações |
|------|------|-------------|
| 12/11 | Estudo inicial | Leitura completa do material |
| 19/11 | Primeira revisão | - |
| 26/11 | Resolução de questões | - |

---

## 🎯 Plano de Ação

### Esta Semana
- [X] Ler material completo
- [ ] Resolver 10 questões sobre SRP
- [ ] Criar 5 flashcards

### Próxima Revisão (19/11)
- [ ] Revisar exemplos práticos
- [ ] Refazer questões erradas
- [ ] Revisar flashcards

### Antes da Prova
- [ ] Revisão rápida dos pontos principais
- [ ] Revisar pegadinhas comuns

---

**Tags:** #arquitetura #SOLID #SRP #design #POO

**Prioridade:** [X] Alta [ ] Média [ ] Baixa

**Status:** [ ] Não iniciado [X] Em estudo [ ] Revisando [ ] Dominado
