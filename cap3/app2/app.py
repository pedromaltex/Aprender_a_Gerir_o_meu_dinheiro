import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Como investir no meu futuro?",
    "description": (
        "Descobre como o teu dinheiro pode crescer ao longo do tempo! 💸\n\n"
        "Experimenta diferentes valores e vê como poupar todos os anos faz a diferença. "
        "O gráfico mostra a evolução da tua poupança a cada ano."
    )
}

def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Inputs simplificados ---
    col1, col2 = st.columns(2)
    with col1:
        initial = st.number_input("💵 Com quanto dinheiro começas?", min_value=0.0, value=100.0, step=10.0)
        monthly = st.number_input("💰 Quanto dinheiro poupas por mês?", min_value=0.0, value=50.0, step=5.0)
    with col2:
        annual_growth = st.number_input("📈 Quanto cresce o dinheiro por ano (%)?", min_value=0.0, value=5.0, step=0.1)
        years = st.slider("⏳ Por quantos anos vais poupar?", 1, 50, 20)

    # --- Cálculo do montante com juros anuais ---
    balance = []
    current = initial
    for year in range(1, years + 1):
        # Somar depósitos anuais
        current += monthly * 12
        # Aplicar juros anuais
        current *= (1 + annual_growth / 100)
        balance.append(current)

    # --- Criar DataFrame para gráfico anual ---
    df = pd.DataFrame({
        "Ano": range(1, years + 1),
        "Saldo (€)": balance
    })

    # --- Mostrar resultado final ---
    st.metric("💎 Valor Final Estimado", f"{balance[-1]:,.2f} €")

    # --- Gráfico interativo com Plotly ---
    fig = px.line(df, x="Ano", y="Saldo (€)",
                  title="Evolução da Poupança ao Longo dos Anos",
                  labels={"Ano": "Ano", "Saldo (€)": "Saldo (€)"},
                  template="plotly_white")
    fig.update_traces(mode="lines+markers", line=dict(color="green", width=3), marker=dict(size=8))
    fig.update_layout(title_font_size=20, xaxis_title_font_size=14, yaxis_title_font_size=14)

    st.plotly_chart(fig, use_container_width=True)

    # --- Mostrar tabela opcional ---
    if st.checkbox("📋 Mostrar tabela com valores anuais"):
        st.dataframe(df)
