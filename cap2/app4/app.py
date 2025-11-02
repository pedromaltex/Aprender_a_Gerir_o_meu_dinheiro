import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🛟 Fundo de Emergência",
    "description": (
        """
        O **fundo de emergência** é a tua **rede de segurança financeira**,  
        o dinheiro que te protege de imprevistos, como perder o emprego, uma avaria no carro  
        ou uma despesa médica inesperada.  

        💡 A regra geral é ter **entre 3 e 12 meses** das tuas **despesas mensais essenciais** guardados.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"  # (podes trocar pelo teu)
}


# --- Funções auxiliares ---
def calcular_fundo_emergencia(despesas_mensais, meses):
    """Calcula o valor total recomendado para o fundo de emergência."""
    return despesas_mensais * meses


def calcular_tempo_para_fundo(meta, poupanca_mensal):
    """Calcula o tempo necessário para atingir o fundo."""
    meses = meta / poupanca_mensal
    return meses


def formatar_tempo(meses_float):
    """Formata meses decimais em anos e meses."""
    anos = int(meses_float // 12)
    meses = int(round(meses_float % 12))
    if anos == 0:
        return f"{meses} meses"
    elif meses == 0:
        return f"{anos} anos"
    else:
        return f"{anos} anos e {meses} meses"


def gerar_progresso(meta, poupanca_mensal):
    """Gera um DataFrame com o progresso mensal até atingir o fundo."""
    meses = int(np.ceil(meta / poupanca_mensal))
    valores = [min(poupanca_mensal * i, meta) for i in range(1, meses + 1)]
    df = pd.DataFrame({
        "Mês": np.arange(1, meses + 1),
        "Fundo acumulado (€)": valores
    })
    return df


# --- Aplicação principal ---
def run():
    st.set_page_config(page_title="Fundo de Emergência", page_icon="🛟")

    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    st.subheader("💰 As tuas despesas e segurança")

    despesas_mensais = st.number_input(
        "Quanto gastas por mês em despesas essenciais (€)?",
        min_value=0.0, step=50.0, value=1000.0
    )

    meses_recomendados = st.slider(
        "Quantos meses queres cobrir com o teu fundo?",
        min_value=3, max_value=12, value=6,
        help="Regra geral: 3 a 6 meses é o ideal. Mais meses = mais segurança."
    )

    fundo_total = calcular_fundo_emergencia(despesas_mensais, meses_recomendados)

    st.success(
        f"🛡️ Deves ter um fundo de emergência de **{fundo_total:,.0f} €**, "
        f"para cobrir **{meses_recomendados} meses** de despesas essenciais."
    )

    st.divider()

    st.subheader("📆 Quanto tempo demoras a juntar o teu fundo?")

    poupanca_mensal = st.number_input(
        "Quanto consegues poupar por mês (€)?",
        min_value=10.0, step=10.0, value=200.0
    )

    meses_necessarios = calcular_tempo_para_fundo(fundo_total, poupanca_mensal)
    tempo_formatado = formatar_tempo(meses_necessarios)

    df = gerar_progresso(fundo_total, poupanca_mensal)

    st.success(
        f"⏳ A poupar **{poupanca_mensal:,.0f} € por mês**, "
        f"atingirás o teu fundo de emergência de **{fundo_total:,.0f} €** em cerca de **{tempo_formatado}**."
    )

    fig = px.line(df, x="Mês", y="Fundo acumulado (€)",
                  title="Progresso até ao Fundo de Emergência",
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        💡 *Dica:* mantém o teu fundo de emergência num **depósito de baixo risco** ou conta de fácil acesso.  
        Não é para investir, é para te proteger!
        """
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
