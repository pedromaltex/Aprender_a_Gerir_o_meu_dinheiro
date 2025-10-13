import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "📊 Simulação de Diversificação Animada",
    "description": (
        "Observa vários stocks e escolhe aquele que acreditas que vai performar melhor.\n"
        "Depois vê como ele evolui passo a passo comparado com o ETF."
    )
}

# --- Funções auxiliares ---
def coin(up_prob=0.51):
    return 1 if np.random.random() < up_prob else 0

def geometric_random_walk(initial_value=100, up_prob=0.51, steps=4000):
    traj = np.zeros(steps)
    traj[0] = initial_value
    for i in range(1, steps):
        traj[i] = traj[i-1] * 1.01 if coin(up_prob) else traj[i-1] * 0.99
    return traj

# --- Função principal ---
def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    n_stocks = 5

    # --- Gerar 4000 passos por stock ---
    stocks = pd.DataFrame({
        f"Stock {i+1}": geometric_random_walk(steps=4000)
        for i in range(n_stocks)
    })
    stocks["ETF"] = stocks.mean(axis=1)

    # --- Mostrar só os primeiros 2000 passos ---
    df_initial = stocks.iloc[:2000].copy()
    df_initial["Step"] = df_initial.index

    fig_init = px.line(
        df_initial,
        x="Step", y=[col for col in df_initial.columns if col != "Step"],
        title="Evolução inicial (primeiros 2000 passos)",
        labels={"value": "Preço", "variable": "Stock"},
        template="plotly_white"
    )
    st.plotly_chart(fig_init, use_container_width=True)

    # --- Escolha do stock ---
    chosen_stock = st.radio("Escolhe o stock que queres comprar:", [f"Stock {i+1}" for i in range(n_stocks)])

    # --- Mostrar resultado final ---
    if st.button("➡️ Ver resultados"):
        df_final = stocks.iloc[2000:].copy()
        df_final["Step"] = df_final.index

        fig_final = px.line(
            df_final,
            x="Step", y=[col for col in df_final.columns if col != "Step"],
            title="Evolução final (após a tua escolha)",
            labels={"value": "Preço", "variable": "Stock"},
            template="plotly_white"
        )
        st.plotly_chart(fig_final, use_container_width=True)

        i_price = stocks[chosen_stock].iloc[1999]
        f_price = stocks[chosen_stock].iloc[-1]
        roi = (f_price / i_price - 1) * 100

        st.markdown("### Resultado do teu investimento:")
        st.metric(label=chosen_stock, value=f"{roi:.2f} %", delta=f"{f_price - i_price:.2f}")

if __name__ == "__main__":
    run()