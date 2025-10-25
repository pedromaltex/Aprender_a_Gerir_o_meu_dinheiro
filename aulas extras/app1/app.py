import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💭 O que é ser rico?",
    "description": (
        """
        Será que a verdadeira riqueza vem do quanto **ganhas por mês** — ou do quanto **consegues guardar**? 💰  

        Neste módulo vais perceber que **ser rico não é ter muito**, mas **precisar de menos**.  
        Vamos explorar como as tuas escolhas e hábitos moldam o teu caminho financeiro. 🌱
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Dados de reflexão (para gráfico) ---
dados_reflexao = pd.DataFrame({
    "Perfil": ["Ganha muito, gasta muito", "Ganha médio, poupa bem", "Ganha pouco, mas é constante"],
    "Poupança Média Mensal (€)": [50, 300, 150],
    "Estabilidade (0-10)": [3, 8, 7]
})

def run():
    st.set_page_config(page_title="O que é ser rico?", page_icon="💭")

    # --- Cabeçalho ---
    st.subheader(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])
    st.divider()

    # --- Reflexão inicial ---
    st.markdown("### 💬 Pensa nisto:")
    st.write(
        """
        👉 Tens 2 pessoas:  
        - A ganha **5000 € por mês**, mas gasta tudo.  
        - B ganha **1500 €**, mas poupa 300 €.  

        **Quem está mais perto da liberdade financeira?**  
        Riqueza é menos sobre *quanto tens* e mais sobre *como usas o que tens*.
        """
    )

    st.divider()

    # --- Visual comparativo ---
    st.markdown("### 📊 Hábitos e estabilidade")
    fig = px.scatter(
        dados_reflexao,
        x="Poupança Média Mensal (€)",
        y="Estabilidade (0-10)",
        text="Perfil",
        size="Poupança Média Mensal (€)",
        color="Estabilidade (0-10)",
        color_continuous_scale="Greens",
        template="plotly_white",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

    st.caption("💡 Quanto mais consistente fores a poupar, maior tende a ser a tua estabilidade financeira.")

    # --- Simulador de poupança ---
    st.divider()
    st.markdown("### 🧮 E tu, quanto consegues poupar?")
    col1, col2 = st.columns(2)
    with col1:
        rendimento = st.number_input("💵 Rendimento mensal (€)", min_value=0.0, value=1500.0, step=50.0)
    with col2:
        despesas = st.number_input("🧾 Despesas mensais (€)", min_value=0.0, value=1200.0, step=50.0)

    poupanca = rendimento - despesas
    percentagem = (poupanca / rendimento * 100) if rendimento > 0 else 0

    if poupanca < 0:
        st.error("⚠️ Estás a gastar mais do que ganhas — é hora de rever o teu orçamento.")
    elif poupanca == 0:
        st.warning("💸 Estás a equilibrar as contas, mas ainda não estás a poupar.")
    else:
        st.success(f"🎯 Consegues poupar **{poupanca:.2f} € por mês** ({percentagem:.1f}% do teu rendimento).")

    st.progress(min(percentagem / 50, 1.0))  # barra visual de progresso (50% como referência saudável)
    st.caption("💡 Uma taxa de poupança acima de 20% é considerada excelente!")

    # --- Conclusão ---
    st.divider()
    st.markdown(
        """
        ### 🌟 Conclusão
        Ser rico **não é um número** — é uma sensação de tranquilidade.  
        É quando o dinheiro **deixa de ser uma preocupação** e passa a ser uma ferramenta para viver melhor.  
        """
    )

    st.info("💬 Poupança é liberdade. Cada euro poupado é tempo ganho no futuro.")

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
