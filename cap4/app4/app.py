import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- Informação padrão mínima ---
APP_INFO = {
    "title": "💡 Desafio Prático: Gerindo o Orçamento do João",
    "description": "Cenário inicial do João, valores serão atualizados aleatoriamente ao carregar a app."
}

# --- Funções ---
def gerar_cenario():
    """Gera valores aleatórios para salário e despesas com step razoável."""
    salario = random.randrange(1200, 3001, 50)
    renda = random.randrange(600, 1201, 50) / 2  # divide com a namorada
    alimentacao = random.randrange(150, 401, 10)
    eletrica_agua = random.randrange(30, 71, 5)
    ginasio = random.randrange(20, 51, 5)
    jantar = random.randrange(10, 41, 5)
    roupa = random.randrange(20, 101, 5)        # NOVO
    eletronica = random.randrange(10, 51, 5)    # NOVO
    carro = 300
    transporte = 40
    return salario, renda, alimentacao, eletrica_agua, ginasio, jantar, roupa, eletronica, carro, transporte

def atualizar_app_info(salario, renda, alimentacao, eletrica_agua, ginasio, jantar, roupa, eletronica, carro, transporte):
    """Atualiza APP_INFO com os valores do cenário."""
    return {
        "title": "💡 Desafio Prático: Gerindo o Orçamento do João",
        "description": (
            f"João recebe {salario}€ por mês. A renda da casa é de {renda*2:.0f}€, "
            f"mas ele divide a meias com a sua namorada, a Mariana.\n"
            f"Em alimentação costuma gastar {alimentacao}€ por mês. Eletricidade e água custam {eletrica_agua}€ por pessoa.\n"
            f"João paga {ginasio}€ de ginásio, jantar fora {jantar}€, roupa {roupa}€ e eletrónica {eletronica}€.\n"
            f"Ele está a pensar comprar um carro ({carro}€) ou usar transporte público ({transporte}€).\n\n"
            "O desafio é aplicares a **regra 50/30/20** e perceberes o que faz sentido no orçamento."
        )
    }

def calcular_distribuicao(necessidades_val, desejos_val, poupanca_val):
    """Calcula a distribuição e percentagens."""
    valor_total = necessidades_val + desejos_val + poupanca_val
    necessidades_pct = round(necessidades_val / valor_total * 100, 1)
    desejos_pct = round(desejos_val / valor_total * 100, 1)
    poupanca_pct = round(poupanca_val / valor_total * 100, 1)
    df = pd.DataFrame({
        "Categoria": ["Necessidades", "Desejos", "Poupança / Investimento"],
        "Valor (€)": [necessidades_val, desejos_val, poupanca_val],
        "Percentual (%)": [necessidades_pct, desejos_pct, poupanca_pct]
    })
    return df, poupanca_pct, valor_total

# --- Main ---
def run():
    if "cenario" not in st.session_state:
        st.session_state["cenario"] = gerar_cenario()
    salario, renda, alimentacao, eletrica_agua, ginasio, jantar, roupa, eletronica, carro, transporte = st.session_state["cenario"]

    APP_INFO = atualizar_app_info(salario, renda, alimentacao, eletrica_agua, ginasio, jantar, roupa, eletronica, carro, transporte)
    st.title(APP_INFO["title"])
    st.info(APP_INFO["description"])
    st.divider()

    st.subheader("🧮 Calculadora do aluno")
    st.markdown("Preenche os valores que achas que João gasta em cada categoria:")

    # Inputs do aluno
    salario_val = st.number_input("Salário João (€)", min_value=0.0, value=100.0, step=50.0)
    necessidades_val = st.number_input("Necessidades (€) (renda, alimentação, eletricidade/água)", min_value=0.0, value=100.0, step=5.0)
    desejos_val = st.number_input("Desejos/Lazer (€) (ginásio, jantar, roupa, eletrónica)", min_value=0.0, value=100.0, step=5.0)
    poupanca_val = salario_val - (necessidades_val + desejos_val)

    # Distribuição
    df, poupanca_pct, valor_total = calcular_distribuicao(necessidades_val, desejos_val, poupanca_val)
    st.info(f"ℹ️ Poupança: {poupanca_val}€ ({poupanca_pct}%)")

    st.markdown("### 💵 Distribuição do orçamento")
    st.dataframe(df.style.format({"Valor (€)": "€{:.2f}", "Percentual (%)": "{:.1f}%"}))
    fig = px.pie(df, names="Categoria", values="Valor (€)",
                 title="Distribuição do orçamento",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("❓ Perguntas do desafio")

    # Pergunta 1
    st.markdown(f"1️⃣ Se João não comprar o carro ({carro} €) e optar pelo transporte público ({transporte} €), quanto consegue poupar a mais?")
    resposta1 = st.number_input("Resposta (€)", min_value=0.0, value=0.0, step=1.0, key="resposta1")
    poupanca_extra = carro - transporte
    if st.button("Verificar Pergunta 1"):
        if resposta1 == poupanca_extra:
            st.success(f"✅ Correto! João poupa {poupanca_extra} € a mais.")
        else:
            st.error(f"❌ Incorreto. A resposta correta é {poupanca_extra} €.")

    # Pergunta 2
    st.markdown("2️⃣ Se João reduzir os gastos com lazer em 20 €, qual será a nova taxa de poupança (%)?")
    valor_poupanca_novo = poupanca_val + 20
    nova_taxa_poupanca = round(valor_poupanca_novo / valor_total * 100, 1)
    resposta2 = st.number_input("Resposta (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="resposta2")
    if st.button("Verificar Pergunta 2"):
        if round(resposta2, 1) == nova_taxa_poupanca:
            st.success(f"✅ Correto! Nova taxa de poupança: {nova_taxa_poupanca} %")
        else:
            st.error(f"❌ Incorreto. A resposta correta é {nova_taxa_poupanca} %")

    # Pergunta 3
    st.markdown("3️⃣ João quer aumentar a poupança para pelo menos 25% do total. Qual estratégia é mais eficiente?")
    if df.loc[df['Categoria']=="Desejos", 'Percentual (%)'].values[0] < 10:
        st.info("💡 Atenção: João já gasta pouco em lazer, talvez seja mais eficiente aumentar os rendimentos.")
    opcoes = ["Aumentar salário", "Reduzir gastos com desejos e lazer", "Reduzir gastos essenciais"]
    resposta3 = st.radio("Escolhe a opção:", opcoes, key="resposta3")
    if st.button("Verificar Pergunta 3"):
        if df.loc[df['Categoria']=="Desejos", 'Percentual (%)'].values[0] < 10 and resposta3 == "Aumentar salário":
            st.success("✅ Correto! Como os gastos com lazer são baixos, aumentar o salário é mais eficiente.")
        elif df.loc[df['Categoria']=="Desejos", 'Percentual (%)'].values[0] >= 10 and resposta3 == "Reduzir gastos com desejos e lazer":
            st.success("✅ Correto! Reduzir desejos/lazer aumenta a poupança sem comprometer necessidades.")
        else:
            st.error("❌ Incorreto. Revê a distribuição do orçamento para escolher a melhor estratégia.")

    # Pergunta 4 - Carro
    st.markdown(f"4️⃣ Com o carro ({carro} €), João consegue manter poupança acima de 20%? Cabe no orçamento?")
    poupanca_com_carro = poupanca_val - carro + transporte
    taxa_com_carro = round(poupanca_com_carro / valor_total * 100, 1)
    resposta4 = st.radio("Escolhe a opção:", ["Sim", "Não"], key="resposta4")
    if st.button("Verificar Pergunta 4"):
        if taxa_com_carro >= 20 and resposta4 == "Sim":
            st.success(f"✅ Correto! A taxa de poupança seria {taxa_com_carro}%, ainda acima de 20%, então cabe no orçamento.")
        elif taxa_com_carro < 20 and resposta4 == "Não":
            st.success(f"✅ Correto! A taxa de poupança seria {taxa_com_carro}%, abaixo de 20%, então não cabe no orçamento.")
        else:
            st.error(f"❌ Incorreto. A taxa de poupança seria {taxa_com_carro}%.")

if __name__ == "__main__":
    run()
