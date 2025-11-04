import streamlit as st
import random

# --- Informação da aplicação ---
APP_INFO = {
    "title": "📝 Será que preciso de um orçamento?",
    "description": (
        """
        Ter um **orçamento** não é só para quem já trabalha ou recebe salário.  
        Mesmo se fores estudante, com mesada, ou dinheiro de trabalhos pontuais,  
        controlar o que entra e o que sai ajuda-te a tomar decisões melhores e a preparar-te para a idade adulta.

        Nesta aula, vais refletir sobre os teus hábitos e perceber porque é importante planear o dinheiro.

        📌 O que vais aprender nesta aula:

        🧠 Consciência financeira - Entender porque o controlo do dinheiro é importante em qualquer fase da vida.  

        💸 Gestão pessoal - Aprender a acompanhar entradas e saídas, mesmo com valores pequenos.  

        🎯 Planeamento futuro - Perceber como um orçamento ajuda-te a atingir objetivos e evitar imprevistos.  

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=90s"
}

# --- Lista de perguntas ---
PERGUNTAS = [
    {
        "pergunta": "Se recebes mesada semanal, mas não sabes quanto gastas, precisas de um orçamento?",
        "opcoes": ["Sim, mesmo com pouco dinheiro.", "Não, só quem recebe salário precisa."],
        "correta": "Sim, mesmo com pouco dinheiro.",
        "explicacao": "Mesmo pequenas quantias precisam de planeamento para evitar gastar tudo sem perceber."
    },
    {
        "pergunta": "Ter um orçamento ajuda apenas a poupar dinheiro?",
        "opcoes": ["Sim, é só para poupar.", "Não, também ajuda a controlar gastos e tomar decisões."],
        "correta": "Não, também ajuda a controlar gastos e tomar decisões.",
        "explicacao": "Orçamento mostra para onde vai o dinheiro e ajuda a priorizar o que é importante."
    },
    {
        "pergunta": "Se anotas todas as tuas despesas de lazer, compras e poupança, já tens um orçamento?",
        "opcoes": ["Sim, isso é suficiente.", "Não, ainda precisas planear limites e objetivos."],
        "correta": "Não, ainda precisas planear limites e objetivos.",
        "explicacao": "Registrar gastos é o primeiro passo, mas definir objetivos e limites completa o orçamento."
    },
    {
        "pergunta": "Se fores adulto e recebes salário, mas gastas tudo sem controlar, vais:",
        "opcoes": ["Ter sempre poupança suficiente.", "Ter dificuldade em atingir objetivos e pagar contas."],
        "correta": "Ter dificuldade em atingir objetivos e pagar contas.",
        "explicacao": "Sem planeamento, mesmo salários maiores podem desaparecer rapidamente."
    },
    {
        "pergunta": "O orçamento serve apenas para cortar gastos?",
        "opcoes": ["Sim, cortar tudo que é supérfluo.", "Não, serve para equilibrar gastos, poupança e objetivos."],
        "correta": "Não, serve para equilibrar gastos, poupança e objetivos.",
        "explicacao": "Orçamento não é só restrição; é sobre **priorizar e organizar**."
    },
    {
        "pergunta": "Se conseguires poupar mesmo pouco dinheiro todo mês, o que acontece com o tempo?",
        "opcoes": ["Nada, é pouco para mudar algo.", "O dinheiro cresce e ajuda a atingir metas maiores."],
        "correta": "O dinheiro cresce e ajuda a atingir metas maiores.",
        "explicacao": "Pequenas poupanças acumulam e podem ser investidas ou usadas em objetivos futuros."
    },
    {
        "pergunta": "Qual é um bom hábito financeiro desde jovem?",
        "opcoes": ["Registrar entradas e saídas de dinheiro.", "Gastar sem se preocupar, aprender depois."],
        "correta": "Registrar entradas e saídas de dinheiro.",
        "explicacao": "Conhecer os teus hábitos desde cedo ajuda a tomar decisões melhores no futuro."
    },
    {
        "pergunta": "Um orçamento flexível é melhor que um rígido?",
        "opcoes": ["Sim, porque a vida muda e os gastos também.", "Não, rígido é sempre melhor."],
        "correta": "Sim, porque a vida muda e os gastos também.",
        "explicacao": "Flexibilidade permite ajustar o plano sem abandonar o orçamento."
    },
    {
        "pergunta": "Se fores adulto e quiseres viajar ou comprar algo grande, o orçamento ajuda-te a:",
        "opcoes": ["Guardar dinheiro e planejar a compra.", "Gastá-lo todo sem pensar."],
        "correta": "Guardar dinheiro e planejar a compra.",
        "explicacao": "Planeamento financeiro permite atingir objetivos maiores sem dívidas."
    },
    {
        "pergunta": "Quem deve ter um orçamento?",
        "opcoes": ["Apenas estudantes.", "Todos, jovens e adultos."],
        "correta": "Todos, jovens e adultos.",
        "explicacao": "Orçamento é útil para qualquer pessoa que queira controlar o seu dinheiro."
    }
]

def verificar_resposta(pergunta_num, resposta, correta, explicacao):
    """Mostra feedback apenas quando clicam no botão 'Verificar'."""
    if st.button(f"Verificar Pergunta {pergunta_num}", key=f"verif_{pergunta_num}"):
        if resposta == correta:
            st.success(f"✅ Correto! {explicacao}")
        else:
            st.error(f"❌ Incorreto. {explicacao}")

def run():
    st.set_page_config(page_title=APP_INFO["title"], page_icon="📝")
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])
    st.divider()

    st.subheader("🧠 Testa os teus conhecimentos")

    # --- Seleção de 4 perguntas aleatórias e armazenamento na sessão ---
    if "perguntas_aleatorias_aula2" not in st.session_state:
        st.session_state.perguntas_aleatorias_aula2 = random.sample(PERGUNTAS, 4)

    perguntas_aleatorias = st.session_state.perguntas_aleatorias_aula2

    # Exibir perguntas
    for i, p in enumerate(perguntas_aleatorias, start=1):
        st.markdown(f"#### {i}️⃣ {p['pergunta']}")
        resposta = st.radio(
            "Escolhe uma opção:",
            p["opcoes"],
            key=f"aula2_q{i}"
        )
        verificar_resposta(i, resposta, p["correta"], p["explicacao"])
        st.divider()

    # --- Conclusão ---
    st.markdown("### 🏁 Conclusão")
    st.info(
        """
        Um **orçamento** é essencial, quer sejas estudante ou adulto.  
        Ele permite-te **controlar o dinheiro**, **poupar para objetivos** e **tomar decisões mais conscientes**. 💪
        
        Quanto mais cedo começares, mais fácil será lidar com desafios financeiros na idade adulta.
        """
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
