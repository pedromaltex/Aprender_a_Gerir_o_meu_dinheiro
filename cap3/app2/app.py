import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💡 Investir no futuro: começa hoje, colhe amanhã",
    "description": (
        """
        Investir não é apenas para ricos — é a forma de **proteger e fazer crescer o teu dinheiro**.  

        Nesta aula vais perceber:
        - Quais são os **principais tipos de investimento**  
        - Como o **risco e retorno** estão relacionados  
        - Por que investir cedo faz toda a diferença
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Dados de exemplo sobre investimentos ---
INVESTIMENTOS = pd.DataFrame({
    "Ativo": ["Poupança", "Obrigações", "Fundos Mistos", "Ações", "Imobiliário"],
    "Rendimento médio anual (%)": [1.5, 2.5, 4.0, 6.0, 5.0],
    "Risco": ["Muito baixo", "Baixo", "Médio", "Alto", "Médio"]
})

# --- Função de simulação simples ---
def simular_crescimento(valor_inicial, anos, rendimento_anual):
    """Simula crescimento de um investimento sem reinvestimentos adicionais."""
    meses = anos * 12
    crescimento = [valor_inicial * ((1 + rendimento_anual / 100) ** (meses / 12)) for _ in range(meses)]
    df = pd.DataFrame({
        "Mês": range(1, meses + 1),
        "Valor (€)": crescimento
    })
    return df

# --- Aplicação principal ---
def run():
    st.set_page_config(page_title="Investir no futuro", page_icon="💡")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # --- Mostrar tipos de investimentos ---
    st.subheader("📊 Tipos de investimento")
    st.dataframe(INVESTIMENTOS)

    # --- Selecionar investimento ---
    st.subheader("💰 Escolhe um investimento para simular")
    ativo = st.selectbox("Ativo", INVESTIMENTOS["Ativo"])
    valor_inicial = st.number_input("Quanto queres investir (€)", min_value=100.0, value=1000.0, step=100.0)
    anos = st.slider("Horizonte temporal (anos)", min_value=1, max_value=40, value=10)
    
    rendimento = INVESTIMENTOS.loc[INVESTIMENTOS["Ativo"] == ativo, "Rendimento médio anual (%)"].values[0]

    # --- Simulação ---
    df_crescimento = simular_crescimento(valor_inicial, anos, rendimento)
    
    final_valor = df_crescimento["Valor (€)"].iloc[-1]

    st.success(
        f"Se investires **{valor_inicial:,.0f} €** em **{ativo}** durante **{anos} anos**, com um rendimento médio anual de **{rendimento:.1f}%**, terás aproximadamente **{final_valor:,.0f} €**."
    )


    st.info(
        "💡 **Dica:** Quanto mais cedo começares a investir, maior será o efeito do tempo e do rendimento composto, mesmo que o valor inicial seja pequeno."
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
