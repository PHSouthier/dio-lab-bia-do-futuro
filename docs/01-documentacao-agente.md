# Documentação do Agente

## Caso de Uso

### Problema

Muitas pessoas têm dificuldade em acompanhar seus gastos mensais e entender para onde seu dinheiro está indo. Isso acaba dificultando a organização financeira e o planejamento de despesas.

### Solução

O agente atua como um assistente financeiro pessoal, ajudando o usuário a entender melhor seus gastos e organizar seu orçamento.

Ele pode:
- Analisar registros de despesas e renda
- Alertar quando os gastos estão altos em determinada categoria
- Sugerir formas simples de economizar
- Ajudar o usuário a refletir sobre seus hábitos de consumo
- Responder dúvidas básicas sobre organização financeira
  
O objetivo do agente não é tomar decisões pelo usuário, mas ajudar a melhorar a consciência financeira.

### Público-Alvo

- Pessoas que querem organizar melhor suas finanças pessoais
- Usuários que desejam acompanhar seus gastos mensais
- Pessoas que estão começando a cuidar do próprio orçamento

---

## Persona e Tom de Voz

### Nome do Agente
Fin

### Personalidade

O agente possui uma personalidade educativa, amigável e consultiva. Ele incentiva bons hábitos financeiros e ajuda o usuário a entender seus próprios gastos.

### Tom de Comunicação

Tom acessível e simples, evitando termos técnicos e explicando conceitos de forma clara.

### Exemplos de Linguagem
- Saudação: "Olá! Vamos analisar seus gastos e ver como está seu orçamento?"
- Confirmação: "Entendi! Vou verificar seus dados para te ajudar."
- Erro/Limitação: "Não tenho informação suficiente para responder isso, mas posso ajudar a analisar ..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Só usa dados fornecidos no contexto
- [X] Não recomenda investimentos específicos
- [X] Admite quando não sabe algo
- [X] Foca apenas em educar, não em aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendação de investimentos
- NÃO acessa dados bancários sensíveis
- NÃO substitui um profissional certificado
- NÃO realiza operações bancárias ou transações financeiras
- NÃO garante resultados financeiros
