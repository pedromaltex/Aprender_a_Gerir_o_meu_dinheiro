import streamlit as st
import plotly.graph_objects as go

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Objectivo 4 - 💶 Simulador da Regra 50/30/20",
    "description": (
        "Aprende a distribuir o teu dinheiro com a **regra 50/30/20**! 🧮💡\n\n"
        "Divide o rendimento entre **necessidades**, **desejos** e **poupança** — "
        "e ajusta as percentagens para encontrares o teu equilíbrio financeiro. 💸"
    )
}


def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Entradas ---
    renda = st.number_input("💰 Quanto dinheiro ganhas por mês (€)?", min_value=0.0, value=1000.0, step=50.0)

    st.markdown("#### 📊 Define as tuas percentagens")
    col1, col2, col3 = st.columns(3)
    with col1:
        percent_necessidades = st.number_input("🏠 Necessidades (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    with col2:
        percent_desejos = st.number_input("🎉 Desejos (%)", min_value=0.0, max_value=100.0, value=30.0, step=1.0)
    with col3:
        percent_poupanca = st.number_input("💎 Poupança (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)

    total = percent_necessidades + percent_desejos + percent_poupanca

    if total != 100:
        st.warning("⚠️ As percentagens devem somar **100%** para criar um orçamento equilibrado.")
        return

    # --- Cálculos ---
    necessidades = renda * (percent_necessidades / 100)
    desejos = renda * (percent_desejos / 100)
    poupanca = renda * (percent_poupanca / 100)

    # --- Mostrar resultados ---
    st.metric("🏠 Necessidades", f"{necessidades:,.2f} €")
    st.metric("🎉 Desejos", f"{desejos:,.2f} €")
    st.metric("💎 Poupança", f"{poupanca:,.2f} €")

    # --- Gráfico de pizza ---
    fig = go.Figure(
        data=[go.Pie(
            labels=["Necessidades", "Desejos", "Poupança"],
            values=[necessidades, desejos, poupanca],
            marker=dict(colors=["#4CAF50", "#FFB347", "#2196F3"]),
            hoverinfo="label+percent",
            textinfo="label+value",
            pull=[0.05, 0, 0]
        )]
    )
    fig.update_layout(
        title="Distribuição do Teu Orçamento Mensal",
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- Feedback pedagógico ---
    st.divider()
    st.markdown("### 💭 Reflexão")
    if percent_poupanca < 10:
        st.warning("Estás a poupar pouco! 💡 Tenta reservar pelo menos 10% do teu rendimento.")
    elif percent_poupanca >= 20:
        st.success("Excelente! 💎 Estás a poupar uma boa parte do teu rendimento.")
    else:
        st.info("Boa! 💰 Já estás no caminho certo — tenta aumentar a poupança gradualmente.")

    if percent_desejos > 40:
        st.warning("⚠️ Cuidado com os desejos — podem estar a pesar demasiado no teu orçamento.")
    elif percent_necessidades > 60:
        st.info("🏠 As necessidades estão altas — vê se há despesas fixas que possas rever.")

    st.caption("💬 *Dica:* pequenas mudanças mensais podem fazer uma grande diferença no final do ano!*")


if __name__ == "__main__":
    run()
