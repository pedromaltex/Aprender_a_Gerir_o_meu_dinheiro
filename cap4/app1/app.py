import streamlit as st
import random

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💰 O que é um orçamento?",
    "description": (
        """
        Um **orçamento** é um plano simples que te ajuda a decidir **como usar o teu dinheiro**, 
        quanto gastar, quanto guardar e quanto poupar para o futuro. 🧾
        
        Nesta aula, vais testar o que já sabes sobre gerir dinheiro e perceber  
        porque é que ter um orçamento é essencial para a tua liberdade financeira.

        📌 O que vais aprender nesta aula:

        🧾 Planeamento financeiro - Compreender como organizar receitas e despesas de forma equilibrada.  

        💡 Tomada de decisão - Aprender a escolher conscientemente onde e como gastar o teu dinheiro.  

        🎯 Liberdade financeira - Perceber que o orçamento não limita. Dá-te controlo e tranquilidade.  

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Lista de perguntas ---
PERGUNTAS = [
    {
        "pergunta": "Um orçamento serve apenas para quem tem pouco dinheiro?",
        "opcoes": ["Sim, quem tem pouco dinheiro precisa controlar-se mais.",
                   "Não, todos devem ter um orçamento."],
        "correta": "Não, todos devem ter um orçamento.",
        "explicacao": "Um orçamento é útil para qualquer pessoa, independentemente do rendimento."
    },
    {
        "pergunta": "Se recebes 1000 € e gastas 900 €, o que te sobra é poupança?",
        "opcoes": ["Sim, os 100 € são poupança.",
                   "Não, só é poupança se eu decidir guardá-los."],
        "correta": "Não, só é poupança se eu decidir guardá-los.",
        "explicacao": "Só é poupança quando decides não gastar o que sobra."
    },
    {
        "pergunta": "Qual destas é uma boa razão para fazer um orçamento?",
        "opcoes": ["Saber para onde vai o meu dinheiro.",
                   "Gastar mais sem me preocupar.",
                   "Evitar falar de dinheiro."],
        "correta": "Saber para onde vai o meu dinheiro.",
        "explicacao": "O orçamento ajuda-te a controlar e planear os teus gastos."
    },
    {
        "pergunta": "Qual seria o primeiro passo para criar um orçamento?",
        "opcoes": ["Anotar todos os rendimentos e despesas.",
                   "Comprar uma aplicação cara de finanças.",
                   "Guardar o dinheiro debaixo do colchão."],
        "correta": "Anotar todos os rendimentos e despesas.",
        "explicacao": "O primeiro passo é saber quanto entra e quanto sai todos os meses."
    },
    {
        "pergunta": "Se não sabes para onde vai o teu dinheiro, qual é a consequência?",
        "opcoes": ["Gastas menos do que podes.",
                   "Gastas sem controlo e não poupas."],
        "correta": "Gastas sem controlo e não poupas.",
        "explicacao": "Sem controlo, é fácil gastar mais do que se devia e não criar poupança."
    },
    {
        "pergunta": "O que é considerado uma despesa fixa?",
        "opcoes": ["Renda da casa.", "Comprar roupas novas."],
        "correta": "Renda da casa.",
        "explicacao": "Despesas fixas são aquelas que se repetem todos os meses e são obrigatórias."
    },
    {
        "pergunta": "O que é uma despesa variável?",
        "opcoes": ["Contas de luz e água.", "Comer fora ou lazer."],
        "correta": "Comer fora ou lazer.",
        "explicacao": "Despesas variáveis mudam de mês para mês e são mais flexíveis."
    },
    {
        "pergunta": "Guardar um pouco de dinheiro todo mês é chamado de:",
        "opcoes": ["Investimento.", "Poupança.", "Orçamento."],
        "correta": "Poupança.",
        "explicacao": "Guardar dinheiro regularmente é chamado de poupança."
    },
    {
        "pergunta": "O que deve vir primeiro no teu orçamento mensal?",
        "opcoes": ["Lazer e compras.", "Despesas essenciais e poupança.", "Investimentos arriscados."],
        "correta": "Despesas essenciais e poupança.",
        "explicacao": "O orçamento prioriza o essencial e depois o lazer ou extra."
    },
    {
        "pergunta": "Um bom orçamento deve ser:",
        "opcoes": ["Flexível e realista.", "Rígido e impossível de cumprir."],
        "correta": "Flexível e realista.",
        "explicacao": "Um orçamento deve ser possível de seguir e ajustar conforme a vida muda."
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
    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])
    st.divider()

    st.subheader("🧠 Testa os teus conhecimentos")

    # --- Seleção de 4 perguntas aleatórias e armazenamento na sessão ---
    if "perguntas_aleatorias" not in st.session_state:
        st.session_state.perguntas_aleatorias = random.sample(PERGUNTAS, 4)

    perguntas_aleatorias = st.session_state.perguntas_aleatorias

    # Exibir perguntas
    for i, p in enumerate(perguntas_aleatorias, start=1):
        st.markdown(f"#### {i}️⃣ {p['pergunta']}")
        resposta = st.radio(
            "Escolhe uma opção:",
            p["opcoes"],
            key=f"q{i}"
        )
        verificar_resposta(i, resposta, p["correta"], p["explicacao"])
        st.divider()

    # --- Conclusão ---
    st.markdown("### 🏁 Conclusão")
    st.info(
        """
        Um **orçamento** é o teu mapa financeiro pessoal.  
        Ele mostra-te **onde estás a gastar**, **quanto podes poupar**  
        e ajuda-te a alcançar os teus **objetivos com mais segurança**. 💪
        
        Mesmo um simples registo mensal pode mudar completamente a forma como vês o teu dinheiro.
        """
    )

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
