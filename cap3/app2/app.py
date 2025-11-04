import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💡 Risco e tipos de investimento",
    "description": (
        """
        Nem todos os investimentos são iguais. Alguns são mais seguros, outros oferecem maior potencial de retorno, mas também maior risco.  

        Nesta aula vais aprender:
        - Quais são os principais tipos de investimento  
        - Qual o risco associado a cada tipo  
        - Como o risco e o retorno estão relacionados

        📌 O que vais aprender nesta aula:

        ⚖️ Conceito de risco - Entender porque não há retorno sem algum nível de incerteza.  

        💰 Tipos de investimento - Conhecer opções como depósitos, obrigações, ações e fundos.  

        📈 Relação risco-retorno - Perceber que investimentos com maior potencial exigem maior tolerância ao risco.  

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
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

# --- Simulação simples de crescimento ao longo de 10 anos ---
def simular_crescimento(valor_inicial, anos, rendimento_anual):
    """Simula crescimento de um investimento sem reinvestimentos adicionais."""
    meses = anos * 12
    crescimento = [valor_inicial * ((1 + rendimento_anual / 100) ** (meses / 12)) for _ in range(meses)]
    df = pd.DataFrame({
        "Mês": range(1, meses + 1),
        "Valor (€)": crescimento
    })
    return df

def run():
    st.set_page_config(page_title="Risco e investimentos", page_icon="💡")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # --- Mostrar tipos de investimentos ---
    st.subheader("📊 Tipos de investimento e risco")
    st.dataframe(INVESTIMENTOS)

    st.caption(
        "💡 Dica: geralmente, quanto maior o risco, maior o retorno potencial — mas cuidado com perdas possíveis."
    )

    # --- Selecionar investimento para simulação ---
    st.subheader("💰 Simula o crescimento de um investimento")
    ativo = st.selectbox("Escolhe um ativo", INVESTIMENTOS["Ativo"])
    valor_inicial = st.number_input("Quanto queres investir (€)", min_value=100.0, value=1000.0, step=100.0)
    anos = st.slider("Horizonte temporal (anos)", min_value=1, max_value=40, value=10)
    
    rendimento = INVESTIMENTOS.loc[INVESTIMENTOS["Ativo"] == ativo, "Rendimento médio anual (%)"].values[0]

    df_crescimento = simular_crescimento(valor_inicial, anos, rendimento)
    final_valor = df_crescimento["Valor (€)"].iloc[-1]

    st.success(
        f"Se investires **{valor_inicial:,.0f} €** em **{ativo}** durante **{anos} anos**, com rendimento médio anual de **{rendimento:.1f}%**, terás aproximadamente **{final_valor:,.0f} €**."
    )

    st.info(
        "💬 **Conclusão:** Cada investimento tem um nível de risco diferente. Conhecer esta relação ajuda a tomar decisões conscientes e escolher o ativo que melhor se adapta ao teu perfil."
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
