# Fin - Agente Financeiro Educativo 💰

**Assistente de organização financeira pessoal baseado em LLM**

## 📋 Sobre o Projeto

Fin é um agente conversacional que ajuda pessoas a organizar suas finanças pessoais, analisar gastos e desenvolver consciência financeira. Ele **não** faz recomendações de investimento, mas atua como um assistente educativo e consultivo.

### Principais Funcionalidades
- ✅ Análise de gastos por categoria
- ✅ Alertas sobre despesas elevadas
- ✅ Sugestões de organização orçamentária
- ✅ Reflexão sobre hábitos de consumo
- ✅ Explicações sobre conceitos financeiros básicos

### O que o Fin NÃO faz
- ❌ Recomendações de investimento
- ❌ Acesso a dados bancários sensíveis
- ❌ Operações financeiras ou transações
- ❌ Substitui consultoria profissional certificada

## 🏗️ Arquitetura

```
Cliente → Streamlit → LLM (Ollama) → Base de Conhecimento → Resposta
```

### Stack Tecnológica
- **Interface**: Streamlit
- **LLM**: Ollama (Llama 3, local)
- **Dados**: JSON/CSV mockados
- **Linguagem**: Python 3.x

## 📊 Base de Dados

| Arquivo | Conteúdo |
|---------|----------|
| `perfil_investidor.json` | Dados do cliente, perfil e objetivos |
| `transacoes.csv` | Histórico de receitas e despesas |
| `historico_atendimento.csv` | Interações anteriores |
| `produtos_financeiros.json` | Produtos disponíveis para ensino |

## 🚀 Como Executar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Garantir que o Ollama está rodando com o modelo llama3
ollama pull llama3

# 3. Executar a aplicação
streamlit run app.py
```

## 💬 Exemplos de Uso

**Análise de gastos:**
```
Usuário: "Onde estou gastando mais?"
Fin: "Olhando suas transações de outubro, sua maior despesa é moradia 
(R$ 1.380), seguida de alimentação (R$ 570). Juntas, representam quase 
80% dos seus gastos. Quer que eu explique algumas estratégias de organização?"
```

**Educação financeira:**
```
Usuário: "O que é CDI?"
Fin: "CDI é uma taxa de referência usada pelos bancos. Quando um 
investimento rende '100% do CDI', significa que ele acompanha essa taxa..."
```

**Redirecionamento consciente:**
```
Usuário: "Devo investir em ações?"
Fin: "Não posso te dizer se você deve, mas posso explicar como funciona! 
Ações são pedaços de empresas... Seu perfil está como 'moderado', então 
vale entender bem antes de decidir."
```

## 🎯 Persona do Agente

**Nome**: Fin  
**Tom**: Amigável, educativo e consultivo  
**Linguagem**: Simples e acessível, sem jargões técnicos  
**Objetivo**: Aumentar a consciência financeira do usuário

## 🔒 Segurança e Anti-Alucinação

- ✅ Responde apenas com dados fornecidos no contexto
- ✅ Admite quando não sabe algo
- ✅ Não inventa valores ou informações financeiras
- ✅ Solicita mais dados quando necessário
- ✅ Mantém foco educativo, nunca aconselha investimentos

## 📈 Público-Alvo

- Pessoas começando a organizar finanças pessoais
- Usuários que querem acompanhar gastos mensais
- Quem busca entender melhor seus hábitos de consumo

## 📝 Estrutura do Projeto

```
.
├── src/
│   ├── app.py                      # Aplicação Streamlit
│   ├── README.md                   # Como rodar a aplicação
├── data/
│   ├── perfil_investidor.json      # Dados do cliente
│   ├── transacoes.csv              # Histórico financeiro
│   ├── historico_atendimento.csv   # Atendimentos anteriores
│   └── produtos_financeiros.json   # Produtos para ensino
├── docs/
│   ├── 01-documentacao-agente.md   # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md     # Estratégia de dados
│   ├── 03-prompts.md               # System prompt e exemplos
│   └── 04-metricas.md              # Avaliação e testes
└── README.md                       # Este arquivo
└── requeirements.md                # Dependências
```

## 🧪 Testes e Validação

O agente foi testado em cenários como:
- Consulta de gastos por categoria
- Perguntas fora do escopo
- Solicitações de informações inexistentes
- Tentativas de obter recomendações de investimento

**Resultado**: Respostas coerentes, dentro do escopo educativo, sem alucinações.

---

**Desenvolvido como projeto educacional de agentes LLM aplicados a finanças pessoais**
