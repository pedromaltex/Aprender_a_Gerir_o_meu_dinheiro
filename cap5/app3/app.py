import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Agradecimentos",
    "description": (
        "Será que **poupar chega**? 🤔\n\n"
        "Descobre como o teu dinheiro **cresce quando é investido** e como a **inflação reduz o seu valor real**. "
        "Compara o dinheiro parado, o investimento nominal e o investimento ajustado à inflação. 💸"
    )
}

# --- Funções auxiliares ---
def compound_interest(principal, annual_rate, years):
    """Cálculo de juros compostos anuais"""
    return principal * (1 + annual_rate) ** years

def decreasing_continuously_compounded(principal, annual_inflation, years):
    """Desvalorização contínua (inflação)"""
    return principal * np.exp(-annual_inflation * years)

# --- Aplicação principal ---
def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Inputs ---
    col1, col2 = st.columns(2)
    with col1:
        initial = st.number_input("💰 Quanto dinheiro tens hoje?", min_value=0.00, value=1000.00, step=100.00)
        inflation = st.number_input("📉 Inflação anual (%)", min_value=0.00, value=2.50, step=0.10) / 100
    with col2:
        investment = st.number_input("📈 Taxa de rendimento anual (%)", min_value=0.00, value=7.00, step=0.10) / 100
        years = st.slider("⏳ Quantos anos queres simular?", 1, 50, 20)

    # --- Cálculos ---
    x_years = np.arange(0, years + 1)
    invest_nominal = [compound_interest(initial, investment, y) for y in x_years]
    invest_real = [v / ((1 + inflation) ** y) for v, y in zip(invest_nominal, x_years)]
    cash_real = [decreasing_continuously_compounded(initial, inflation, y) for y in x_years]

    # --- Gráfico ---
    fig = go.Figure()

    # Dinheiro investido (nominal)
    fig.add_trace(go.Scatter(
        x=x_years, y=invest_nominal,
        mode="lines+markers",
        name="💹 Investimento (sem inflação)",
        line=dict(color="green", width=3)
    ))

    # Investimento ajustado à inflação
    fig.add_trace(go.Scatter(
        x=x_years, y=invest_real,
        mode="lines+markers",
        name="💰 Investimento Real (ajustado à inflação)",
        line=dict(color="orange", width=3, dash="dash")
    ))

    # Dinheiro parado com inflação
    fig.add_trace(go.Scatter(
        x=x_years, y=cash_real,
        mode="lines+markers",
        name="📉 Dinheiro parado (inflação)",
        line=dict(color="red", width=3, dash="dot")
    ))

    fig.update_layout(
        title="Evolução do Valor do Dinheiro ao Longo dos Anos",
        xaxis_title="Ano",
        yaxis_title="Valor (€)",
        template="plotly_white",
        legend=dict(yanchor="bottom", y=0.02, xanchor="right", x=0.98)
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- Métricas ---
    st.metric("💹 Valor investido (nominal)", f"{invest_nominal[-1]:,.2f} €")
    st.metric("💰 Valor real do investimento", f"{invest_real[-1]:,.2f} €")
    st.metric("📉 Valor se o dinheiro ficar parado", f"{cash_real[-1]:,.2f} €")

    # --- Reflexão final ---
    st.info(
        "💭 **Reflete:** Mesmo que o teu investimento cresça, se a inflação for alta, o poder de compra real pode diminuir. "
        "Por isso, é importante investir com rendimentos que superem a inflação!"
    )


if __name__ == "__main__":
    run()
