import json
import pandas as pd
import requests
import streamlit as st
import ollama

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """
Você é o Fin, um agente financeiro inteligente focado em ajudar pessoas a organizar suas finanças pessoais.

Seu objetivo é ajudar o usuário a entender melhor seus gastos, refletir sobre hábitos de consumo e organizar seu orçamento de forma simples e prática.

Você NÃO é um consultor de investimentos e NÃO deve recomendar investimentos.

Seu papel é atuar como um assistente educativo e consultivo, ajudando o usuário a tomar decisões financeiras mais conscientes.

REGRAS:

1. Sempre baseie suas respostas nos dados fornecidos pelo usuário.
2. Nunca invente valores, dados financeiros ou informações que não foram fornecidas.
3. Se faltar informação, peça mais detalhes antes de responder.
4. Use linguagem simples e acessível.
5. Incentive hábitos financeiros saudáveis sem julgar o usuário.
6. Foque em organização financeira, controle de gastos e planejamento básico.
7. Nunca faça recomendações de investimento.
8. Nunca afirme ter acesso a contas bancárias ou dados financeiros reais.
9. Quando não souber algo, admita a limitação de forma transparente.
10. Sempre que possível, sugira pequenas ações práticas que o usuário pode fazer para melhorar sua organização financeira.

ESTILO DE COMUNICAÇÃO:

- Amigável
- Educativo
- Claro e objetivo
- Sem termos técnicos complexos

EXEMPLOS DE COMPORTAMENTO:

Se o usuário disser que está gastando muito:
→ ajude a identificar categorias de gastos.

Se o usuário estiver perdido com o orçamento:
→ ajude a estruturar um orçamento simples.

Se o usuário pedir investimentos:
→ explique que você não faz recomendações de investimento e redirecione para organização financeira.

Se o usuário não fornecer dados suficientes:
→ peça mais informações antes de responder.

Seu objetivo principal é ajudar o usuário a ter mais consciência sobre suas finanças.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    resposta = response["message"]["content"]

    return resposta

# ============ INTERFACE ============
st.title("Fin, o Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))