import streamlit as st
import pandas as pd
import plotly.express as px
import random
from help_clean.clean_question import clean_session_questions

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🧠 Será que és influenciado?",
    "description": (
        """
        Esta é uma aula de autoavaliação onde vais testar se o teu consumo é racional
        ou se estás a cair em armadilhas criadas pelo marketing e pela perceção de valor.

        📌 O que vais perceber nesta aula:

        🧭 Autoconhecimento - Perceber até que ponto as tuas decisões de compra são influenciadas por fatores externos.

        💭 Reflexão prática - Responder a perguntas rápidas que te ajudam a identificar padrões de comportamento.

        🧠 Consciência financeira - Aprender a reconhecer truques de marketing como “999€” e evitar compras por impulso.

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Perguntas organizadas por tema ---
PERGUNTAS0 = {
    "Preço": [
        "Um produto com 999€ parece mais barato do que um com 1000€?",
        "Se vires '-50% desconto', ficas automaticamente mais interessado?",
        "Acreditas que um produto mais caro é, à partida, de melhor qualidade?",
        "Quando algo é anunciado como 'edição limitada', sentes mais vontade de comprar?",
        "Já compraste algo porque 'era uma boa oportunidade', mesmo sem precisares?"
    ],
    "Redes": [
        "Já sentiste vontade de comprar algo só porque muitos amigos ou influencers o têm?",
        "Já compraste algo por recomendação de alguém que segues nas redes sociais?",
        "Já quiseste um produto apenas para não te sentires 'fora de moda'?",
        "Alguma vez te sentiste mal por não ter o que outras pessoas mostram online?",
        "Segues contas de marcas ou influencers que te fazem gastar mais do que querias?"
    ],
    "Emoções": [
        "Alguma vez compraste algo para te sentires melhor ou recompensado?",
        "Acreditas que certos produtos podem realmente mudar a forma como te sentes (mais confiante, feliz, bonito, etc.)?",
        "Frases como 'Tu mereces!' ou 'Torna-te a tua melhor versão' já te motivaram a comprar algo?",
        "Quando vês uma publicidade emocional, sentes-te mais inclinado a confiar na marca?",
        "Já foste influenciado por um anúncio que usava música, imagens ou histórias inspiradoras?"
    ],
    "Comportamento": [
        "Tens tendência a comprar mais quando há promoções ou saldos?",
        "Guardas produtos no carrinho online 'só para ver o preço' e acabas por comprar?",
        "Alguma vez compraste algo e depois arrependeste-te logo de seguida?",
        "Sentes que às vezes compras por impulso?",
        "Costumas esquecer-te de planear as tuas compras?"
    ],
    "Linguagem": [
        "Expressões como 'última oportunidade', 'exclusivo' ou 'só hoje' despertam o teu interesse?",
        "Se uma marca usa palavras como 'natural', 'sustentável' ou 'premium', isso muda a tua perceção?",
        "Achas que a forma como uma marca fala contigo (mais próxima, divertida ou emocional) te faz confiar mais nela?",
        "Palavras como 'novo', 'melhorado' ou 'inovador' chamam mais a tua atenção?",
        "Já sentiste que o nome ou o design de um produto te fizeram valorizá-lo mais?"
    ]
}

def run():
    st.set_page_config(page_title="Será que és influenciado?", page_icon="🧠")

    clean_session_questions()

    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])


    # Inicializar estado
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.respostas = []

        # Selecionar 2 perguntas aleatórias por tema
        perguntas_selecionadas = []
        for tema, lista in PERGUNTAS0.items():
            perguntas_selecionadas.extend(random.sample(lista, 2))
        random.shuffle(perguntas_selecionadas)
        st.session_state.perguntas = perguntas_selecionadas

    total = len(st.session_state.perguntas)
    atual = st.session_state.index

    # --- Mostrar perguntas ---
    if atual < total:
        pergunta = st.session_state.perguntas[atual]

        st.markdown(f"### Pergunta {atual + 1} de {total}")
        st.write(pergunta)

        escolha = st.radio(
            "Escolhe uma opção:",
            ["Sim", "Não", "Depende"],
            key=f"p{atual}"
        )

        # Botão "Próxima" para avançar
        if st.button("👉 Próxima"):
            st.session_state.respostas.append(escolha)
            st.session_state.index += 1
            st.rerun()

    # --- Resultados finais ---
    else:
        st.success("🎯 Terminaste o quiz!")
        df = pd.DataFrame({
            "Pergunta": st.session_state.perguntas,
            "Resposta": st.session_state.respostas
        })

        st.markdown("### 🧾 As tuas respostas")
        st.dataframe(df, hide_index=True)

        # Contar respostas influenciadas
        influenciadas = sum(resp in ["Sim", "Depende"] for resp in st.session_state.respostas)

        # Aviso ou elogio
        if influenciadas >= 5:
            st.warning(
                f"""
                ⚠️ **Atenção!**  
                Respondeste “Sim” ou “Depende” em {influenciadas} de {total} perguntas.  

                Isto indica que **a linguagem, o marketing e as redes sociais te influenciam bastante** — totalmente normal, mas é bom estar consciente.  

                💬 Na próxima vez que fores comprar algo, pergunta-te:  
                *“Preciso mesmo disto, ou só quero porque me fizeram querer?”*
                """
            )
        else:
            st.success(
                f"""
                💪 Muito bem!  
                Apenas {influenciadas} de {total} respostas mostraram influência direta.  

                Isto significa que tens **bom pensamento crítico** perante publicidade e preços.  
                Continua assim — questionar é o melhor antídoto contra decisões impulsivas.
                """
            )

        st.info("💡 Reconhecer a influência é o primeiro passo para fazer escolhas conscientes e gerir melhor o teu dinheiro.")

        # Botão para reiniciar o quiz
        if st.button("🔁 Recomeçar"):
            st.session_state.index = 0
            st.session_state.respostas = []
            # Selecionar novas perguntas aleatórias
            perguntas_selecionadas = []
            for tema, lista in PERGUNTAS0.items():
                perguntas_selecionadas.extend(random.sample(lista, 2))
            random.shuffle(perguntas_selecionadas)
            st.session_state.perguntas = perguntas_selecionadas
            st.rerun()

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
