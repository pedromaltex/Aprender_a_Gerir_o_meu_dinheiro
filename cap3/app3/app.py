import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "⏳ Tempo é dinheiro.",
    "description": (
        """
        Quanto mais cedo começares a investir, maior será o efeito do **tempo** no crescimento do teu dinheiro.  

        Nesta aula vais ver:
        - Quanto podes acumular poupando uma quantia mensal
        - Quanto ganhas em juros ao longo dos anos
        - O impacto de começar 5 anos mais cedo
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Função de simulação com poupança mensal ---
def simular_poupanca(valor_mensal, anos, rendimento_anual):
    """Simula o crescimento de poupança mensal com rendimento anual."""
    meses = anos * 12
    taxa_mensal = (1 + rendimento_anual / 100) ** (1/12) - 1
    valores = []
    saldo = 0
    for mes in range(1, meses + 1):
        saldo = saldo * (1 + taxa_mensal) + valor_mensal
        valores.append(saldo)
    df = pd.DataFrame({"Mês": np.arange(1, meses + 1), "Valor (€)": valores})
    return df

def run():
    st.set_page_config(page_title="Tempo é dinheiro", page_icon="⏳")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    st.subheader("💰 Simulação de poupança mensal")

    valor_mensal = st.number_input("Quanto vais poupar por mês (€)", min_value=10.0, value=100.0, step=10.0)
    rendimento = st.slider("Rendimento médio anual (%)", min_value=0.0, max_value=15.0, value=6.0, step=0.1)
    anos = st.slider("Horizonte temporal (anos)", min_value=1, max_value=40, value=20)

    # Cenário atual
    df_atual = simular_poupanca(valor_mensal, anos, rendimento)
    final_atual = df_atual["Valor (€)"].iloc[-1]

    # Cenário 5 anos mais cedo
    df_mais_cedo = simular_poupanca(valor_mensal, anos + 5, rendimento)
    final_mais_cedo = df_mais_cedo["Valor (€)"].iloc[-1]

    st.success(
        f"Se poupares **{valor_mensal:,.0f} €/mês** durante **{anos} anos**, com rendimento de **{rendimento:.1f}%/ano**, acumularás aproximadamente **{final_atual:,.0f} €**.\n\n"
        f"Se tivesses começado **5 anos mais cedo**, o valor seria **{final_mais_cedo:,.0f} €**, demonstrando o poder do tempo e dos juros compostos."
    )

    # --- Calcular juros corretos por ano ---
    df_atual["Juros Mês (€)"] = df_atual["Valor (€)"].diff() - valor_mensal
    df_atual.loc[0, "Juros Mês (€)"] = df_atual.loc[0, "Valor (€)"] - valor_mensal

    df_atual["Ano"] = (df_atual["Mês"] - 1) // 12 + 1
    juros_por_ano = df_atual.groupby("Ano")["Juros Mês (€)"].sum().reset_index()
    juros_por_ano.rename(columns={"Juros Mês (€)": "Juros ganhos (€)"}, inplace=True)

    st.subheader("💸 Juros ganhos por ano (aproximado)")
    st.dataframe(juros_por_ano, hide_index=True)

    # Mensagem didática
    juros_1 = juros_por_ano.loc[juros_por_ano["Ano"] == 1, "Juros ganhos (€)"].values[0]
    juros_5 = juros_por_ano.loc[juros_por_ano["Ano"] == 5, "Juros ganhos (€)"].values[0] if anos >= 5 else None
    juros_ultimo = juros_por_ano.loc[juros_por_ano["Ano"] == max(juros_por_ano["Ano"]), "Juros ganhos (€)"].values[0]

    msg = f"Aqui consegues perceber o quão importante é ser consistente:\n\n"
    msg += f"- No primeiro ano, recebes aproximadamente **{juros_1:,.0f} €** de juros.\n"
    if juros_5 is not None:
        msg += f"- Passados 5 anos, recebes cerca de **{juros_5:,.0f} €** de juros.\n"
    msg += f"- No último ano, recebes aproximadamente **{juros_ultimo:,.0f} €**, {juros_ultimo/valor_mensal:,.1f} vezes superior à tua poupança mensal."

    st.info(msg)

    # --- Gráfico comparativo ---
    df_atual["Cenário"] = f"Começou agora ({anos} anos)"
    df_mais_cedo["Cenário"] = f"Começou 5 anos mais cedo ({anos + 5} anos)"
    df_comb = pd.concat([df_atual, df_mais_cedo], ignore_index=True)

    fig = px.line(
        df_comb, x="Mês", y="Valor (€)", color="Cenário",
        labels={"Valor (€)": "Valor acumulado (€)", "Mês": "Meses"},
        title="Comparação: Começar agora vs 5 anos mais cedo"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "💬 **Conclusão:** Mesmo pequenas poupanças mensais crescem muito com o tempo e juros compostos. Começar cedo é sempre uma vantagem."
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
