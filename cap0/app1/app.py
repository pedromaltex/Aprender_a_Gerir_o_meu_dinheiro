import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Mentalidade Financeira 💡",
    "description": (
        "Aprende a pensar sobre dinheiro e tomar decisões conscientes! 💸\n\n"
        "Simula como pequenas escolhas podem impactar a tua poupança ao longo do tempo. "
        "O gráfico mostra a evolução do teu dinheiro com diferentes decisões."
    )
}

def run():
    st.subheader(APP_INFO["title"])
    st.info(APP_INFO["description"])
    st.divider()

    # --- Inputs do utilizador ---
    st.markdown("### Simulação de escolhas financeiras")
    initial_amount = st.number_input(
        "Quanto dinheiro tens para gastar/poupar esta semana? (€)", min_value=1, value=20
    )
    choice = st.radio(
        "Escolhe o que fazer com este dinheiro:",
        (
            "Gastar tudo em itens de desejo",
            "Poupar metade, gastar metade",
            "Guardar tudo para uma meta futura"
        )
    )

    # --- Simulação de crescimento ---
    years = list(range(1, 11))  # 10 anos
    savings = []
    for year in years:
        if choice == "Gastar tudo em itens de desejo":
            savings.append(0)
        elif choice == "Poupar metade, gastar metade":
            savings.append((initial_amount * 0.5) * year)
        else:  # Guardar tudo
            savings.append(initial_amount * year)

    df = pd.DataFrame({
        "Ano": years,
        "Poupança (€)": savings
    })

    # --- Gráfico interativo ---
    fig = px.line(
        df,
        x="Ano",
        y="Poupança (€)",
        title="Evolução da tua poupança ao longo do tempo",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Conclusão interativa ---
    st.markdown("### Reflexão")
    if choice == "Gastar tudo em itens de desejo":
        st.info("Escolher gastar tudo impede que o teu dinheiro cresça. Tenta equilibrar desejos e poupança!")
    elif choice == "Poupar metade, gastar metade":
        st.success("Ótimo equilíbrio! Poupar parte do dinheiro já cria impacto positivo a longo prazo.")
    else:
        st.success("Excelente! Guardar todo o dinheiro para metas futuras acelera o crescimento da tua poupança.")

    st.divider()

    # --- Botões alinhados aos cantos ---
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Aula Anterior"):
            st.info("Redirecionar para a aula anterior.")
    with col2:
        st.button("➡️ Próxima Aula")
        st.info("Redirecionar para a próxima aula.")

if __name__ == "__main__":
    run()
