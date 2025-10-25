import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💸 A inflação está a comer as tuas poupanças?",
    "description": (
        """
        A **inflação** faz com que o mesmo dinheiro valha **menos no futuro**.  
        Mesmo que poupes todos os meses, o que hoje custa 10.000 € poderá custar **muito mais daqui a alguns anos**.

        💡 Nesta simulação, podes comparar o impacto da inflação no teu objetivo e perceber
        quanto **mais** precisas de poupar para manter o mesmo poder de compra.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Funções auxiliares ---
def valor_futuro_inflacao(valor_atual, taxa_inflacao, anos):
    """Calcula o valor futuro ajustado pela inflação."""
    return valor_atual * ((1 + taxa_inflacao / 100) ** anos)


def calcular_poupanca_mensal_sem_inflacao(objetivo, anos):
    """Poupança simples (sem inflação)."""
    meses = anos * 12
    return objetivo / meses


def calcular_poupanca_mensal_com_inflacao(objetivo, anos, taxa_inflacao):
    """Poupança ajustada à inflação."""
    objetivo_futuro = valor_futuro_inflacao(objetivo, taxa_inflacao, anos)
    meses = anos * 12
    return objetivo_futuro / meses, objetivo_futuro


def gerar_crescimento(poupanca_mensal, anos):
    """Gera evolução da poupança (sem rendimentos)."""
    meses = int(anos * 12)
    valores = [poupanca_mensal * i for i in range(1, meses + 1)]
    df = pd.DataFrame({
        "Mês": np.arange(1, meses + 1),
        "Valor acumulado (€)": valores
    })
    return df


# --- Aplicação principal ---
def run():
    st.set_page_config(page_title="A inflação está a comer as tuas poupanças?", page_icon="💸")

    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # --- Escolher objetivo ---
    st.subheader("🎯 Define o teu objetivo")
    objetivo_tipo = st.selectbox(
        "Tipo de objetivo:",
        ["Carro", "Casa", "Bicicleta", "Viagem", "Computador", "Outro"]
    )

    preco = st.number_input(
        f"Preço atual do teu {objetivo_tipo.lower()} (€)",
        min_value=0.0,
        step=100.0,
        value=10000.0 if objetivo_tipo == "Carro" else 2000.0
    )

    anos = st.slider("Prazo para o objetivo (anos)", min_value=1, max_value=30, value=5)

    st.divider()

    # --- Taxa de inflação ---
    st.subheader("📈 Taxa de inflação")
    inflacao = st.slider("Taxa média de inflação anual (%)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
    st.caption("ℹ️ Nota: A inflação média em Portugal nas últimas décadas tem rondado **~2% ao ano** (dados do INE).")

    st.divider()

    # --- Cálculos principais ---
    poupanca_sem = calcular_poupanca_mensal_sem_inflacao(preco, anos)
    poupanca_com, objetivo_futuro = calcular_poupanca_mensal_com_inflacao(preco, anos, inflacao)

    df_sem = gerar_crescimento(poupanca_sem, anos)
    df_sem["Cenário"] = "Sem inflação"

    df_com = gerar_crescimento(poupanca_com, anos)
    df_com["Cenário"] = "Com inflação"

    df_total = pd.concat([df_sem, df_com])

    # --- Resultados ---
    st.success(
        f"""
        🏷️ **Hoje:** O teu {objetivo_tipo.lower()} custa **{preco:,.0f} €**  
        📅 **Daqui a {anos} anos (com {inflacao:.1f}% de inflação):** custará cerca de **{objetivo_futuro:,.0f} €**  

        💰 Para o conseguires:
        - Sem inflação → poupar **{poupanca_sem:,.0f} € / mês**
        - Com inflação → precisas de **{poupanca_com:,.0f} € / mês**
        """
    )

    # --- Gráfico comparativo ---
    fig = px.line(
        df_total,
        x="Mês",
        y="Valor acumulado (€)",
        color="Cenário",
        title="Evolução da poupança: com e sem inflação",
        labels={"Mês": "Meses", "Valor acumulado (€)": "Total acumulado (€)"},
    )

    # Adicionar linha do preço ajustado
    fig.add_hline(y=preco, line_dash="dot", annotation_text="Preço atual", annotation_position="bottom right")
    fig.add_hline(y=objetivo_futuro, line_dash="dot", annotation_text="Preço futuro (com inflação)", annotation_position="top right")

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "💡 A inflação **diminui o poder de compra** das tuas poupanças. "
        "Guardar dinheiro é importante — mas fazê-lo com consciência do seu valor real é essencial!"
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
