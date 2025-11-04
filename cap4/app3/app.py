import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "📊 Poder em Simplicidade: Regra 50/30/20",
    "description": (
        """
        A **regra 50/30/20** ajuda-te a distribuir o teu dinheiro de forma simples e eficaz:  

        - **50%** para necessidades essenciais (alimentação, transporte, contas básicas)  
        - **30%** para desejos e lazer (saídas, hobbies, compras supérfluas)  
        - **20%** para poupança ou investimento (objetivos futuros, emergência, educação)

        Nesta aula, vais ver como aplicar esta regra mesmo com mesada ou salário.

        📌 O que vais aprender nesta aula:

        ⚖️ Equilíbrio financeiro - Aprender a dividir o dinheiro entre necessidades, desejos e poupança.  

        💡 Simplicidade prática - Ver como aplicar a regra 50/30/20 de forma fácil e adaptada à tua realidade.  

        🎯 Objetivos claros - Entender como pequenas escolhas mensais constroem estabilidade e liberdade financeira.  

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=150s"
}

def run():
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])
    st.divider()

    st.subheader("💡 Testa a Regra 50/30/20 com o teu dinheiro")

    # --- Inputs do utilizador ---
    valor_total = st.number_input(
        "Quanto dinheiro tens para gerir neste mês? (€)", min_value=10.0, value=20.0, step=5.0
    )

    st.markdown("### Ajusta os teus percentuais (opcional)")
    necessidades_pct = st.slider("Necessidades (%)", 0, 100)
    desejos_pct = st.slider("Desejos (%)", 0, 100)
    poupanca_pct = 100 - necessidades_pct - desejos_pct

    # --- Mensagem de aviso sobre poupança ---
    if poupanca_pct < 0:
        st.error(
            f"❌ A poupança está negativa ({poupanca_pct}%). "
            "Isto significa que estarás a gastar mais do que tens e a usar dinheiro que devias poupar."
        )
    elif poupanca_pct < 10:
        st.warning(f"⚠️ Atenção! A tua poupança está baixa ({poupanca_pct}%). Tenta aumentar para pelo menos 20%.")
    elif 10 <= poupanca_pct < 20:
        st.info(f"ℹ️ A tua poupança está moderada ({poupanca_pct}%). Considera aumentar um pouco para objetivos futuros.")
    else:
        st.success(f"✅ Excelente! A tua poupança está adequada ({poupanca_pct}%).")

    st.info(f"Poupança / Investimento será automaticamente {poupanca_pct}%")

    # --- Cálculo da distribuição ---
    distribuicao = {
        "Categoria": ["Necessidades", "Desejos", "Poupança / Investimento"],
        "Valor (€)": [
            valor_total * necessidades_pct / 100,
            valor_total * desejos_pct / 100,
            valor_total * poupanca_pct / 100
        ]
    }
    df = pd.DataFrame(distribuicao)

    # --- Mostrar tabela ---
    st.markdown("### 💵 Distribuição do teu dinheiro")
    st.dataframe(df.style.format({"Valor (€)": "€{:.2f}"}))

    # --- Gráfico interativo ---
    fig = px.pie(df, names="Categoria", values="Valor (€)",
                 title="Distribuição segundo a Regra 50/30/20",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📝 Reflexão")
    st.info(
        """
        - Esta regra é simples e flexível: podes ajustá-la conforme a tua realidade.  
        - Mesmo com pouco dinheiro, reservar **20% para poupança ou objetivos futuros** faz diferença ao longo do tempo.  
        - Se fores estudante, aplica a regra à mesada ou dinheiro de trabalhos pontuais.  
        - Para adultos, aplica ao salário e despesas fixas e variáveis.
        """
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
