import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💹 Juros Compostos",
    "description": (
        """
        Aprende como o **tempo, a taxa de rendimento e os aportes periódicos** fazem o teu dinheiro crescer exponencialmente.  

        Nesta aula vais ver:
        - A fórmula simples de juros compostos  
        - A fórmula com aportes periódicos  
        - Simulação ajustável por períodos: semanal, mensal ou anual  
        - Gráfico do crescimento do capital  

        📌 O que vais aprender nesta aula:

        🧮 Conceito base - Entender como os juros compostos fazem o dinheiro crescer sobre o próprio rendimento.  

        💰 Aportes regulares - Ver como contribuições constantes aceleram o crescimento do capital.  

        📊 Visualização prática - Acompanhar o crescimento do investimento com gráficos e simulações interativas.  

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Função de simulação ---
def simular_juros_compostos(valor_inicial, aporte, anos, rendimento_anual, periodo):
    """Simula crescimento de capital com juros compostos, aportes periódicos e valor inicial."""
    # Determinar número de períodos por ano
    freq_map = {"Semanal": 52, "Mensal": 12, "Anual": 1}
    n_periodos_ano = freq_map[periodo]
    
    taxa_periodo = (1 + rendimento_anual / 100) ** (1/n_periodos_ano) - 1
    total_periodos = anos * n_periodos_ano

    valores = []
    saldo = valor_inicial
    for i in range(1, total_periodos + 1):
        saldo = saldo * (1 + taxa_periodo) + aporte
        valores.append(saldo)
    
    df = pd.DataFrame({"Período": np.arange(1, total_periodos + 1), "Valor (€)": valores})
    df["Ano"] = (df["Período"] - 1) // n_periodos_ano + 1
    return df, taxa_periodo

def run():
    st.set_page_config(page_title="Juros Compostos", page_icon="💹")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    st.subheader("💰 Configura a tua simulação de Juros Compostos")
    
    valor_inicial = st.number_input("Valor inicial (€)", min_value=0.0, value=0.0, step=100.0)
    aporte = st.number_input("Aporte periódico (€)", min_value=0.0, value=100.0, step=10.0)
    rendimento = st.slider("Taxa de rendimento anual (%)", min_value=0.0, max_value=15.0, value=6.0, step=0.1)
    anos = st.slider("Horizonte temporal (anos)", min_value=1, max_value=70, value=20)
    periodo = st.selectbox("Periodicidade dos aportes", ["Semanal", "Mensal", "Anual"])

    freq_map = {"Semanal": 52, "Mensal": 12, "Anual": 1}
    n_periodos_ano = freq_map[periodo]
    n = anos * n_periodos_ano
    r_periodo = (1 + rendimento / 100) ** (1/n_periodos_ano) - 1

    st.markdown("### 🧮 Fórmula simples de Juros Compostos (somente valor inicial)")
    st.latex(r"""
    FV = V_0 \cdot (1 + r)^n
    """)
    st.markdown(
        f"- **V₀** = {valor_inicial} € (valor inicial)\n"
        f"- **r** = {(r_periodo*100):.2f}% (taxa por período)\n"
        f"- **n** = {n} (número total de períodos)"
    )

    st.markdown("### 🧮 Fórmula completa com aportes periódicos")
    st.latex(r"""
    FV = V_0 \cdot (1 + r)^n + P \cdot \frac{(1+r)^n - 1}{r}
    """)
    st.markdown(
        f"- **V₀** = {valor_inicial} € (valor inicial)\n"
        f"- **P** = {aporte} € (aporte {periodo.lower()})\n"
        f"- **r** = {r_periodo:.5f} (taxa por período)\n"
        f"- **n** = {n} (número total de períodos)"
    )

    # --- Simulação ---
    df, taxa_periodo = simular_juros_compostos(valor_inicial, aporte, anos, rendimento, periodo)
    valor_final = df["Valor (€)"].iloc[-1]

    st.success(
        f"Após {anos} anos, com aporte {periodo.lower()} de {aporte:,.0f} € e valor inicial de {valor_inicial:,.0f} €, "
        f"o teu capital será aproximadamente **{valor_final:,.0f} €**."
    )

    # Juros por ano
    df["Juros Período (€)"] = df["Valor (€)"].diff() - aporte
    df.loc[0, "Juros Período (€)"] = df.loc[0, "Valor (€)"] - aporte
    juros_por_ano = df.groupby("Ano")["Juros Período (€)"].sum().reset_index()
    juros_por_ano.rename(columns={"Juros Período (€)": "Juros ganhos (€)"}, inplace=True)

    st.subheader("💸 Juros ganhos por ano (aproximado)")
    st.dataframe(juros_por_ano, hide_index=True)

    # Gráfico
    fig = px.line(df, x="Período", y="Valor (€)", title=f"Crescimento do Capital ({periodo})")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "💬 **Conclusão:** Primeiro aprendeste a fórmula básica e depois viste como os aportes periódicos aumentam exponencialmente o capital. "
        "Quanto mais cedo e frequentes forem os aportes, maior o efeito dos juros compostos."
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
