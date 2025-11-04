import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- Informação da aplicação ---
APP_INFO = {
    "title": "📈 Investir: a arma secreta contra a inflação",
    "description": (
        """
        Como viste, a **inflação** faz com que o dinheiro perca valor ao longo do tempo, 
        o que hoje compras com 100 €, daqui a alguns anos pode custar 120 € ou mais.  

        **Investir** é a forma de proteger (e aumentar) o teu poder de compra.  
        Nesta simulação, vais ver a diferença entre **guardar dinheiro** e **investi-lo**.

        📌 O que vais aprender nesta aula:

        📉 Impacto da inflação - Perceber como a subida dos preços reduz o valor real das tuas poupanças.

        📈 Poder do investimento - Compreender como investir pode superar a inflação e fazer o dinheiro crescer.

        🔢 Simulação prática - Comparar o resultado de poupar vs. investir ao longo do tempo.

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}


def simular_investimento(valor_inicial, anos, rendimento_anual, inflacao_anual):
    """Simula crescimento de dinheiro guardado vs investido ao longo dos anos."""
    meses = anos * 12
    taxa_rendimento_mensal = (1 + rendimento_anual / 100) ** (1 / 12) - 1
    taxa_inflacao_mensal = (1 + inflacao_anual / 100) ** (1 / 12) - 1

    valores_investidos = []
    valores_guardados = []
    poder_compra_investimento = []
    poder_compra_poupanca = []

    valor_investido = valor_inicial
    valor_guardado = valor_inicial

    for mes in range(1, meses + 1):
        valor_investido *= (1 + taxa_rendimento_mensal)
        # valor guardado não rende
        valor_guardado = valor_guardado
        # ajusta ao poder de compra
        valor_real_invest = valor_investido / ((1 + taxa_inflacao_mensal) ** mes)
        valor_real_guard = valor_guardado / ((1 + taxa_inflacao_mensal) ** mes)

        valores_investidos.append(valor_investido)
        valores_guardados.append(valor_guardado)
        poder_compra_investimento.append(valor_real_invest)
        poder_compra_poupanca.append(valor_real_guard)

    df = pd.DataFrame({
        "Mês": np.arange(1, meses + 1),
        "Investimento (€)": valores_investidos,
        "Guardar Dinheiro (€)": valores_guardados,
        "Investimento (valor real €)": poder_compra_investimento,
        "Guardar Dinheiro (valor real €)": poder_compra_poupanca
    })
    return df


def run():
    st.set_page_config(page_title="Investir: a arma secreta contra a inflação", page_icon="📈")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # --- Entradas ---
    st.subheader("💡 Define o teu cenário")

    valor_inicial = st.number_input("Quanto tens atualmente (€)", min_value=100.0, value=10000.0, step=100.0)
    anos = st.slider("Horizonte temporal (anos)", 1, 40, 20)
    rendimento = st.slider("Rendimento médio anual do investimento (%)", 0.0, 15.0, 7.0, step=0.1)
    inflacao = st.slider("Taxa de inflação média anual (%)", 0.0, 10.0, 2.5, step=0.1)

    st.caption("ℹ️ A inflação média em Portugal entre 2000 e 2023 foi de cerca de **2.1%** ao ano (INE).")

    # --- Simulação ---
    df = simular_investimento(valor_inicial, anos, rendimento, inflacao)

    final_invest = df["Investimento (€)"].iloc[-1]
    final_poup = df["Guardar Dinheiro (€)"].iloc[-1]
    real_invest = df["Investimento (valor real €)"].iloc[-1]
    real_poup = df["Guardar Dinheiro (valor real €)"].iloc[-1]

    # --- Resultados ---
    st.success(
        f"""
        📊 Após **{anos} anos**:
        - Se **guardares o dinheiro**, continuas com **{final_poup:,.0f} €**,  
          mas o poder de compra real será de apenas **{real_poup:,.0f} €**.
        - Se **investires**, terás **{final_invest:,.0f} €**,  
          o que equivale a **{real_invest:,.0f} € em valor atual**.
        """
    )

    # --- Gráficos ---
    tabs = st.tabs(["💰 Valor Nominal", "📉 Valor Real (ajustado à inflação)"])

    with tabs[0]:
        fig1 = px.line(
            df, x="Mês",
            y=["Investimento (€)", "Guardar Dinheiro (€)"],
            labels={"value": "Valor (€)", "variable": "Cenário"},
            title="Evolução do valor ao longo do tempo (sem ajustar à inflação)"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with tabs[1]:
        fig2 = px.line(
            df, x="Mês",
            y=["Investimento (valor real €)", "Guardar Dinheiro (valor real €)"],
            labels={"value": "Valor Real (€)", "variable": "Cenário"},
            title="Evolução do poder de compra (ajustado à inflação)"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.info(
        "💬 **Conclusão:** Guardar dinheiro parece seguro, mas com o tempo perdes poder de compra. "
        "Investir é a melhor forma de o proteger e fazer crescer."
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
