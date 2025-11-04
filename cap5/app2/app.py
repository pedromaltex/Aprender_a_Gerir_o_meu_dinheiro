import streamlit as st
import random

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🎯 Quiz Final",
    "description": (
        """
        Chegou o momento de testar tudo o que aprendeste! 🧠💰  

        Este **quiz final** vai ajudar-te a perceber até que ponto compreendes os conceitos essenciais,  
        desde o poder dos **juros compostos**, até à importância de ter um **orçamento**  
        e manter uma **mentalidade financeira equilibrada**.  

        No fim, vais receber um **feedback personalizado** com o teu perfil financeiro  
        e algumas sugestões para continuares a evoluir. 🚀  

        Estás pronto para descobrir o teu nível de sabedoria financeira? 🔍
        """
    ),
}

def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    st.write("### 🧩 Vamos ao Quiz!")

    # --- Perguntas com números aleatórios ---
    capital = random.randint(1000, 5000)
    taxa = random.choice([3, 5, 7])
    anos = random.choice([3, 5, 10])
    inflacao = random.choice([2, 3, 4])
    rendimento = random.choice([6, 8, 10])

    # Lista de perguntas
    perguntas = [
        {
            "enunciado": f"Se investires **{capital} €** a uma taxa de **{taxa}% ao ano** durante **{anos} anos**, "
                         "o que acontece ao teu dinheiro?",
            "opcoes": [
                "Cresce de forma linear (acrescentas o mesmo valor todos os anos)",
                "Cresce de forma composta (ganhas juros sobre juros)",
                "Perde valor com o tempo",
                "Mantém-se igual"
            ],
            "correta": "Cresce de forma composta (ganhas juros sobre juros)"
        },
        {
            "enunciado": f"A inflação média é de **{inflacao}% ao ano**. Se guardares 1000 € debaixo do colchão, "
                         "quanto valerá em termos de poder de compra daqui a 5 anos?",
            "opcoes": [
                "Mais de 1000 €",
                "Aproximadamente o mesmo",
                "Menos de 1000 €",
                "Depende da taxa de juro bancária"
            ],
            "correta": "Menos de 1000 €"
        },
        {
            "enunciado": "Qual destas opções representa melhor a **regra 50/30/20**?",
            "opcoes": [
                "50% lazer, 30% poupança, 20% necessidades",
                "50% necessidades, 30% desejos, 20% poupança/investimento",
                "30% necessidades, 50% desejos, 20% investimento",
                "20% necessidades, 30% desejos, 50% poupança"
            ],
            "correta": "50% necessidades, 30% desejos, 20% poupança/investimento"
        },
        {
            "enunciado": "Ter um **fundo de emergência** significa:",
            "opcoes": [
                "Guardar dinheiro para gastar em férias",
                "Investir em ações de alto risco",
                "Ter poupança suficiente para cobrir despesas por 3 a 6 meses",
                "Fazer um empréstimo quando surgir uma emergência"
            ],
            "correta": "Ter poupança suficiente para cobrir despesas por 3 a 6 meses"
        },
        {
            "enunciado": f"Se a inflação é de {inflacao}% e o teu investimento rende {rendimento}%, "
                         "o teu ganho **real** é de aproximadamente:",
            "opcoes": [
                f"{rendimento - inflacao}%",
                f"{rendimento + inflacao}%",
                f"{inflacao - rendimento}%",
                "Depende do montante inicial"
            ],
            "correta": f"{rendimento - inflacao}%"
        },
        {
            "enunciado": "Qual destas atitudes demonstra **inteligência financeira**?",
            "opcoes": [
                "Gastar todo o salário, mas sem dívidas",
                "Ter um orçamento e investir regularmente",
                "Evitar qualquer tipo de risco",
                "Esperar ganhar muito dinheiro antes de começar a poupar"
            ],
            "correta": "Ter um orçamento e investir regularmente"
        },
    ]

    # --- Quiz interativo ---
    respostas_certas = 0
    respostas = {}

    with st.form("quiz_form"):
        for i, q in enumerate(perguntas):
            st.markdown(f"**{i+1}. {q['enunciado']}**")
            resposta = st.radio("Escolhe uma opção:", q["opcoes"], key=f"q{i}")
            respostas[i] = resposta
            st.write("")  # espaçamento visual
        submit = st.form_submit_button("Ver Resultados 🏁")

    if submit:
        for i, q in enumerate(perguntas):
            if respostas[i] == q["correta"]:
                respostas_certas += 1

        st.divider()
        st.subheader("📊 Resultado Final")

        total = len(perguntas)
        score = respostas_certas / total * 100

        st.write(f"Acertaste **{respostas_certas} de {total} perguntas** ({score:.1f}%).")

        if score < 50:
            st.error("💭 Perfil: **Iniciante Financeiro** — Estás a começar bem! Continua a explorar conceitos básicos como orçamento e juros compostos.")
        elif 50 <= score < 80:
            st.warning("📈 Perfil: **Equilibrado** — Já tens boas noções, mas podes melhorar em temas como inflação e rendimento real.")
        else:
            st.success("🚀 Perfil: **Mestre Financeiro** — Excelente! Mostras uma visão sólida e madura sobre o dinheiro e os investimentos.")

        st.divider()
        st.markdown("💡 *Lembra-te: o mais importante não é saber tudo, mas continuar a aprender e a pôr em prática o que sabes.*")

