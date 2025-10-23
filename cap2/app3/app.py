import streamlit as st
import random

# --- Informação da aplicação ---
APP_INFO = {
    "title": "Inflação na poupanças. (Ponte para próximo tema)",
    "description": (
        "Consegues distinguir o que é **necessário** do que é apenas um **desejo**? 🧠💭\n\n"
        "Classifica cada gasto e descobre se estás a pensar como um verdadeiro gestor financeiro! 💪"
    )
}

# --- Lista de exemplos (necessidades vs desejos) ---
ITENS = [
    ("Comprar comida", "necessidade"),
    ("Ir ao cinema", "desejo"),
    ("Comprar roupa de inverno", "necessidade"),
    ("Trocar de telemóvel só porque há um novo modelo", "desejo"),
    ("Pagar a renda de casa", "necessidade"),
    ("Jantar fora todas as semanas", "desejo"),
    ("Comprar material escolar", "necessidade"),
    ("Assinatura de streaming", "desejo"),
    ("Medicamentos", "necessidade"),
    ("Comprar videojogos", "desejo"),
]

# Explicações curtas
EXPLICACOES = {
    "necessidade": "✅ Uma necessidade é algo essencial para viver com segurança e bem-estar.",
    "desejo": "💭 Um desejo é algo que queremos, mas que podemos viver sem — ajuda a equilibrar o orçamento."
}


def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    # --- Inicialização da sessão ---
    if "itens" not in st.session_state:
        st.session_state.itens = random.sample(ITENS, len(ITENS))  # ordem aleatória
        st.session_state.resultados = {}
        st.session_state.mostrados = 0

    # --- Mostrar um item de cada vez ---
    if st.session_state.mostrados < len(st.session_state.itens):
        item, resposta_correta = st.session_state.itens[st.session_state.mostrados]
        st.markdown(f"### 💡 {item}")
        col1, col2 = st.columns(2)

        if col1.button("🧺 Necessidade"):
            st.session_state.resultados[item] = "necessidade"
            st.session_state.mostrados += 1
            st.rerun()
        if col2.button("🎁 Desejo"):
            st.session_state.resultados[item] = "desejo"
            st.session_state.mostrados += 1
            st.rerun()
    else:
        # --- Mostrar resultados ---
        st.success("🎉 Concluíste o desafio!")
        acertos = sum(
            1 for (item, correta) in ITENS if st.session_state.resultados.get(item) == correta
        )
        total = len(ITENS)
        percentagem = (acertos / total) * 100

        st.metric("Pontuação", f"{acertos}/{total} ({percentagem:.0f}%)")

        # Feedback geral
        if percentagem == 100:
            st.balloons()
            st.success("Excelente! 💎 Tens noção clara das tuas prioridades.")
        elif percentagem >= 70:
            st.info("Muito bem! 👏 Já sabes distinguir o essencial do supérfluo.")
        else:
            st.warning("Ainda há espaço para melhorar 🧠 — tenta pensar no que é mesmo essencial.")

        # Mostrar explicações
        st.divider()
        st.markdown("### 🧾 Resumo e explicações")
        for item, correta in ITENS:
            resposta = st.session_state.resultados.get(item)
            if resposta == correta:
                st.markdown(f"✅ **{item}** → {correta.title()}")
            else:
                st.markdown(f"❌ **{item}** → {correta.title()} ({EXPLICACOES[correta]})")

        # Botão de reiniciar
        if st.button("🔁 Tentar novamente"):
            for key in ["itens", "resultados", "mostrados"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


if __name__ == "__main__":
    run()
