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
def coin(up_prob=0.5001):
    return 1 if np.random.random() < up_prob else 0

def geometric_random_walk(initial_value=100, up_prob=0.501, steps=4000):
    traj = np.zeros(steps)
    traj[0] = initial_value
    for i in range(1, steps):
        traj[i] = traj[i-1] * 1.01 if coin(up_prob) else traj[i-1] * 0.99
    return traj


# --- Estado da app ---
if "reset" not in st.session_state:
    st.session_state.reset = False

if "stocks_df" not in st.session_state:
    st.session_state.stocks_df = None

if st.session_state.reset:
    st.session_state.stocks_df = None


# --- Função principal ---
def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    steps = 4000
    n_stocks = 6

    if st.session_state.stocks_df is None:
        # --- Gerar 4000 passos por stock ---
        stocks = pd.DataFrame({
            f"Stock {i+1}": geometric_random_walk(steps=steps)
            for i in range(n_stocks)
        })
        stocks["Média"] = stocks.mean(axis=1)

        # --- Mostrar só os primeiros 2000 passos ---
        df_initial = stocks.iloc[:2000].copy()
        df_initial["Step"] = df_initial.index

        df_all = stocks.copy()
        df_all["Step"] = df_all.index
        st.session_state.stocks_df = df_all
    else:
        df_all = st.session_state.stocks_df
        df_initial = df_all.iloc[:2000].copy()
        df_initial["Step"] = df_initial.index

    # --- Gráfico inicial ---
    fig_init = px.line(
        df_initial,
        x="Step", y=[col for col in df_initial.columns if col != "Step"],
        title="Evolução inicial (primeiros 2000 passos)",
        labels={"value": "Preço", "variable": "Stock"},
        template="plotly_white"
    )
    st.plotly_chart(fig_init, width='stretch')

    # --- Escolha do ativo ---
    choices = [f"Stock {i+1}" for i in range(n_stocks)] + ["Média"]
    chosen_stock = st.radio("Escolhe o ativo que queres comprar:", choices)

    # --- Mostrar resultados ---
    if st.button("➡️ Ver resultados"):

        fig_all = px.line(
            df_all,
            x="Step", y=[col for col in df_all.columns if col != "Step"],
            title="Evolução final (após a tua escolha)",
            labels={"value": "Preço", "variable": "Ativo"},
            template="plotly_white"
        )
        st.plotly_chart(fig_all, width='stretch')

        st.markdown("### 💰 Resultados finais:")

        initial_prices = df_all.iloc[1999, :-1]  # preços no momento 1
        final_prices = df_all.iloc[-1, :-1]      # preços no momento 2
        initial_etf = df_all["ETF"].iloc[1999]
        final_etf = df_all["ETF"].iloc[-1]

        investment = 1000
        values = {
            stock: investment * (final_prices[stock] / initial_prices[stock])
            for stock in final_prices.index
        }
        values["ETF"] = investment * (final_etf / initial_etf)

        # --- Tabela de resultados ---
        results_df = pd.DataFrame({
            "Ativo": list(values.keys()),
            "Valor Final (€)": [f"{v:,.2f}" for v in values.values()]
        })

        results_df["Ativo"] = results_df["Ativo"].apply(
            lambda x: f"👉 **{x}**" if x == chosen_stock else x
        )

        st.dataframe(results_df, width='stretch', hide_index=True)

        # --- Feedback dinâmico ---
        chosen_value = values[chosen_stock]
        difference = chosen_value - investment

        if difference > 0:
            st.success(
                f"🎉 Excelente escolha! Se tivesses investido **1000 €** em **{chosen_stock}**, "
                f"terias agora **{chosen_value:.2f} €**, ou seja, um ganho de **+{difference:.2f} €**."
            )
        else:
            st.warning(
                f"📉 A tua escolha não correu tão bem... Se tivesses investido **1000 €** em **{chosen_stock}**, "
                f"terias agora apenas **{chosen_value:.2f} €**, uma perda de **{difference:.2f} €**."
            )

        # --- Observação educativa sobre o ETF ---
        st.info(
            "💡 **Sabias que a Média costuma ser mais estável?**\n\n"
            "Como representa a média de todos os stocks, ele tende a crescer de forma mais constante, "
            "reduzindo o risco individual de escolher uma ação que corre mal."
        )

    # --- Botão para reiniciar ---
    if st.button("🔄 Nova simulação"):
        st.session_state.stocks_df = None
        st.rerun()


if __name__ == "__main__":
    run()
   