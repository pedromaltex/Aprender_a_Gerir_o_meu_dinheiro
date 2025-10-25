import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import math

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🎯 Quanto preciso de poupar?",
    "description": (
        """
        Escolhe um objetivo — **carro, casa, bicicleta, viagem...** —  
        e descobre **quanto precisas de poupar por mês** ou **quanto tempo demorarias a atingir o teu sonho**.  

        💡 Aqui consideramos apenas a poupança simples, sem rendimentos — o foco é perceber o esforço necessário!
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}


# --- Funções auxiliares ---
def calcular_poupanca_mensal(objetivo, anos):
    """Calcula quanto é preciso poupar por mês para atingir o objetivo em x anos (sem juros)."""
    meses = anos * 12
    return objetivo / meses


def calcular_tempo(objetivo, poupanca_mensal):
    """Calcula quanto tempo demora a atingir o objetivo poupando x por mês (sem juros)."""
    meses = objetivo / poupanca_mensal
    return meses / 12  # devolve em anos (pode ter decimais)


def formatar_tempo(anos_float):
    """Transforma anos decimais em formato 'X anos e Y meses'."""
    anos = int(anos_float)
    meses = int(round((anos_float - anos) * 12))
    if anos == 0:
        return f"{meses} meses"
    elif meses == 0:
        return f"{anos} anos"
    else:
        return f"{anos} anos e {meses} meses"


def gerar_crescimento(poupanca_mensal, anos):
    """Gera tabela de crescimento simples, sem juros."""
    meses = int(anos * 12)
    valores = [poupanca_mensal * i for i in range(1, meses + 1)]
    df = pd.DataFrame({
        "Mês": np.arange(1, meses + 1),
        "Valor acumulado (€)": valores
    })
    return df


# --- Aplicação principal ---
def run():
    st.set_page_config(page_title="Quanto preciso de poupar?", page_icon="🎯")

    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # --- Escolher objetivo ---
    st.subheader("💡 Escolhe o teu objetivo")
    objetivo_tipo = st.selectbox(
        "Tipo de objetivo:",
        ["Carro", "Casa", "Bicicleta", "Viagem", "Computador", "Outro"]
    )

    preco = st.number_input(
        f"Preço estimado do(da) teu(tua) {objetivo_tipo.lower()} (€)",
        min_value=0.0,
        step=100.0,
        value=10000.0 if objetivo_tipo == "Carro" else 2000.0
    )

    st.divider()

    # --- Escolher modo de simulação ---
    st.subheader("⚙️ O que queres descobrir?")
    modo = st.radio(
        "Escolhe uma opção:",
        ["Quanto preciso de poupar por mês", "Quanto tempo demoraria"]
    )

    # --- Modo 1: Calcular poupança mensal ---
    if modo == "Quanto preciso de poupar por mês":
        anos = st.slider("Prazo (anos)", min_value=1, max_value=30, value=5)
        poupanca_mensal = calcular_poupanca_mensal(preco, anos)
        df = gerar_crescimento(poupanca_mensal, anos)

        st.success(
            f"""
            💸 Para comprares um **{objetivo_tipo.lower()} de {preco:,.0f} €** em **{anos} anos**,  
            precisas de poupar **{poupanca_mensal:,.0f} € por mês**.
            """
        )


    # --- Modo 2: Calcular tempo necessário ---
    else:
        poupanca_mensal = st.number_input(
            "Quanto consegues poupar por mês (€)?",
            min_value=10.0,
            step=10.0,
            value=200.0
        )
        anos = calcular_tempo(preco, poupanca_mensal)
        tempo_formatado = formatar_tempo(anos)
        df = gerar_crescimento(poupanca_mensal, anos)

        st.success(
            f"""
            ⏳ A poupar **{poupanca_mensal:,.0f} € por mês**,  
            demorarás cerca de **{tempo_formatado}** a juntar **{preco:,.0f} €**.
            """
        )

    st.info(
        "💡 Mesmo sem juros, a consistência é o segredo. Poupar todos os meses cria hábitos e resultados!"
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
