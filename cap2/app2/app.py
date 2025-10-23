import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Quanto preciso de poupar? Vale a pena",
    "description": (
        "Aprende a **equilibrar rendimentos e despesas** de forma divertida! 🧮💸\n\n"
        "Cria o teu orçamento, vê quanto sobra (ou falta!) e descobre como pequenas decisões "
        "podem fazer uma grande diferença no teu futuro financeiro."
    )
}


def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Rendimentos ---
    st.markdown("### 🏦 Rendimentos")
    col1, col2 = st.columns(2)

    with col1:
        salario = st.number_input("💰 Mesada / salário (€)", min_value=0.0, value=100.0, step=5.0)
        outros = st.number_input("🎁 Outros rendimentos (€)", min_value=0.0, value=20.0, step=5.0)

    total_rendimentos = salario + outros
    st.success(f"**Total de rendimentos:** {total_rendimentos:.2f} €")

    # --- Despesas ---
    st.divider()
    st.markdown("### 🧾 Despesas")

    categorias = ["Alimentação", "Transporte", "Lazer", "Tecnologia", "Roupas", "Outros"]
    despesas = {}

    col1, col2 = st.columns(2)
    for i, categoria in enumerate(categorias):
        col = col1 if i < len(categorias) / 2 else col2
        with col:
            despesas[categoria] = st.number_input(f"{categoria} (€)", min_value=0.0, value=0.0, step=5.0)

    total_despesas = sum(despesas.values())
    st.warning(f"**Total de despesas:** {total_despesas:.2f} €")

    # --- Análise do saldo ---
    st.divider()

    saldo = total_rendimentos - total_despesas
    proporcao_gastos = total_despesas / total_rendimentos if total_rendimentos > 0 else 1

    if saldo < 0:
        st.error(f"🚨 Estás a gastar **{-saldo:.2f} €** a mais do que ganhas! Vamos rever as despesas? 😅")

    elif proporcao_gastos > 0.9:
        st.error(f"⚠️ Estás a gastar **{proporcao_gastos*100:.0f}%** dos teus rendimentos. "
                 "Quase não sobra nada para poupar! 🪙")

    elif proporcao_gastos > 0.8:
        st.warning(f"💡 Estás a gastar **{proporcao_gastos*100:.0f}%** do que ganhas. "
                   "Tenta guardar pelo menos 10% para o futuro. 😉")

    elif saldo == 0:
        st.info("⚖️ Estás equilibrado — mas lembra-te: quem poupa hoje, conquista amanhã! 💪")

    else:
        st.success(f"💎 Excelente! Sobra-te **{saldo:.2f} €** este mês — continua a poupar e investir bem! 🚀")

    # --- Gráfico das despesas ---
    st.divider()

    df_despesas = pd.DataFrame({
        "Categoria": list(despesas.keys()),
        "Valor (€)": list(despesas.values())
    })

    if total_despesas > 0:
        fig = px.pie(
            df_despesas,
            names="Categoria",
            values="Valor (€)",
            title="Distribuição das Despesas Mensais",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(textinfo="label+percent", pull=[0.05] * len(df_despesas))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("👆 Introduz algumas despesas para veres o gráfico de distribuição.")

    # --- Reflexão final ---
    st.divider()
    st.markdown(
        "💭 **Reflete:** O que poderias mudar no teu orçamento para poupar mais? "
        "Há alguma despesa que poderias reduzir ou substituir?"
    )


if __name__ == "__main__":
    run()
