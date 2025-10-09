import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💰 Desafio da Poupança",
    "description": (
        "Define um objetivo de poupança e vê **quanto tempo precisas para alcançá-lo**! 🏦\n\n"
        "Experimenta diferentes valores de poupança mensal e percebe como pequenas mudanças podem acelerar o teu sucesso financeiro. 🚀"
    )
}

def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Inputs ---
    col1, col2 = st.columns(2)
    with col1:
        objetivo = st.number_input("🎯 Objetivo (€)", min_value=1.0, value=500.0, step=10.0)
        saldo_inicial = st.number_input("💵 Quanto tens agora (€)", min_value=0.0, value=0.0, step=10.0)
    with col2:
        poupanca_mensal = st.number_input("💰 Quanto podes poupar por mês (€)", min_value=1.0, value=50.0, step=5.0)
        taxa_juros = st.number_input("📈 Rendimento mensal (%)", min_value=0.0, value=0.0, step=0.1) / 100

    # --- Simulação ---
    meses = 0
    saldo = saldo_inicial
    historico = [saldo]

    while saldo < objetivo:
        saldo = saldo * (1 + taxa_juros) + poupanca_mensal
        historico.append(saldo)
        meses += 1
        if meses > 600:  # limite de 50 anos
            st.warning("⏳ Mais de 50 anos para atingir o objetivo! Tenta aumentar a poupança.")
            break

    anos = meses // 12
    meses_restantes = meses % 12

    # --- DataFrame para gráfico ---
    df = pd.DataFrame({
        "Mês": range(len(historico)),
        "Saldo (€)": historico
    })

    # --- Resultado ---
    st.success(f"Vai demorar cerca de **{anos} anos e {meses_restantes} meses** para atingir {objetivo:.2f} €")
    st.metric("Valor final estimado", f"{historico[-1]:.2f} €")

    # --- Gráfico ---
    fig = px.line(df, x="Mês", y="Saldo (€)", title="Evolução da Poupança ao Longo do Tempo",
                  labels={"Mês": "Mês", "Saldo (€)": "Saldo (€)"},
                  template="plotly_white")
    fig.update_traces(mode="lines+markers", line=dict(color="green", width=3), marker=dict(size=6))
    st.plotly_chart(fig, use_container_width=True)

    # --- Reflexão ---
    st.divider()
    st.markdown(
        "💭 **Reflete:** Se aumentares a poupança mensal, consegues atingir o objetivo mais rápido. "
        "Que pequenas mudanças no dia a dia poderiam aumentar a tua poupança?"
    )


if __name__ == "__main__":
    run()
