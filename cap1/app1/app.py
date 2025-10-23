import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🧠 O que a sociedade nos impõe",
    "description": (
        """
        Descobre como a sociedade, amigos, família e publicidade podem influenciar os teus desejos de consumo.  

        💡 **O desafio:** Decide se cada produto é uma **necessidade** ou um **desejo**.  
        ⚠️ Sê sincero contigo mesmo. Algumas escolhas são influenciadas, outras são mesmo tuas.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Produtos e respostas corretas ---
PRODUTOS = [
    {"nome": "Telemóvel topo de gama", "tipo": "Desejo"},
    {"nome": "Alimentação Básica", "tipo": "Necessidade"},
    {"nome": "Snack ou lanche favorito", "tipo": "Desejo"},
    {"nome": "Medicamentos", "tipo": "Necessidade"},
    {"nome": "Última consola de jogos", "tipo": "Desejo"},
    {"nome": "Relógio ou pulseira digital", "tipo": "Desejo"},
    {"nome": "Amazon Prime", "tipo": "Desejo"},
    {"nome": "Conta da Eletricidade", "tipo": "Necessidade"},
    {"nome": "Jantar Fora", "tipo": "Desejo"},
    {"nome": "Conta da água", "tipo": "Necessidade"},
    {"nome": "Roupas de marca / acessórios de moda", "tipo": "Desejo"},
    {"nome": "Carro", "tipo": "Desejo"},

]

def run():
    st.set_page_config(page_title="O que a sociedade nos impõe", page_icon="🧠")

    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # Inicializar estado
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.respostas = []

    total = len(PRODUTOS)
    atual = st.session_state.index

    if atual < total:
        produto = PRODUTOS[atual]["nome"]
        tipo_correto = PRODUTOS[atual]["tipo"]

        st.markdown(f"### Produto {atual + 1} de {total}")
        st.subheader(produto)

        escolha = st.radio(
            "Classifica este produto:",
            ["💚 Necessidade", "💸 Desejo"],
            key=f"q{atual}"
        )

        if st.button("👉 Próximo"):
            resposta_limpa = "Necessidade" if "Necessidade" in escolha else "Desejo"
            st.session_state.respostas.append({
                "Produto": produto,
                "Escolha": resposta_limpa,
                "Correto": resposta_limpa == tipo_correto
            })
            st.session_state.index += 1
            st.rerun()

    else:
        st.success("🎯 Terminaste o quiz! Vamos ver os teus resultados:")

        df = pd.DataFrame(st.session_state.respostas)

        st.markdown("### 🧾 Resultados")
        st.dataframe(df, hide_index=True)

        acertos = sum(df["Correto"])
        st.markdown(f"**Pontuação:** {acertos} / {total}")
        st.warning(
            """
            ⚠️ Repara: nem sempre estas definições são fixas.  
            Para alguém que more longe do trabalho e não tenha transportes públicos, o **carro** pode ser uma *Necessidade*.

            Tudo depende do contexto. É por isso que se chama **finanças pessoais** — o importante é entender o teu caso.
            """
        )

        st.info("💡 Lembra-te: perceber o que é necessidade e o que é desejo é o primeiro passo para gerir melhor o teu dinheiro.")
        st.markdown("---")
        if st.button("🔁 Recomeçar"):
            st.session_state.index = 0
            st.session_state.respostas = []
            st.rerun()

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
