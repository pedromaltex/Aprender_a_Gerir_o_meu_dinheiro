import streamlit as st
import pandas as pd
import random
from help_clean.clean_question import clean_session_questions

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💭 Quiz da Mentalidade Financeira",
    "description": (
        """
        Descobre se as tuas **crenças e atitudes sobre o dinheiro** te estão a ajudar ou a travar. 💰

        Este quiz revela como pensas sobre sucesso, esforço, investimento e risco.

        Não há respostas certas ou erradas — apenas **formas diferentes de ver o dinheiro**.

        📌 O que vais aprender:

        🧠 **Mentalidade financeira** - Explorar como as tuas crenças influenciam as tuas decisões com o dinheiro.
      
        💭 **Reflexão pessoal** - Identificar padrões de pensamento que te podem estar a limitar.

        🚀 **Crescimento** - Descobrir como pequenas mudanças de mentalidade podem melhorar a tua relação com o dinheiro.

        💡 Esta aplicação faz parte do projeto *Todos Contam — Aprender a Gerir o Meu Dinheiro*.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

# --- Perguntas organizadas por tema ---
PERGUNTAS2 = {
    "Sucesso e comparação": [
        {
            "texto": "Vês alguém com 25 anos num carro desportivo. O que pensas?",
            "opcoes": {
                "Que bom que ele teve sucesso!": 2,
                "Deve ser herdeiro.": 0,
                "Também queria, mas nunca vou conseguir.": 1
            }
        },
        {
            "texto": "Vês um amigo abrir um negócio. Qual a tua reação?",
            "opcoes": {
                "Que coragem — podia aprender com ele.": 2,
                "Vai perder dinheiro.": 0,
                "Eu não teria coragem, mas admiro.": 1
            }
        }
    ],
    "Medo e atitude": [
        {
            "texto": "Quando pensas em investir, o que sentes?",
            "opcoes": {
                "Curiosidade — quero aprender como funciona.": 2,
                "Medo — posso perder tudo.": 0,
                "Indiferença — isso não é para mim.": 1
            }
        },
        {
            "texto": "Quando falhas num objetivo financeiro:",
            "opcoes": {
                "Aprendo com o erro e ajusto.": 2,
                "Fico frustrado e paro por um tempo.": 1,
                "Acho que não sirvo para isso.": 0
            }
        }
    ],
    "Comportamento e hábitos": [
        {
            "texto": "Tens 100 € extra no fim do mês. O que fazes?",
            "opcoes": {
                "Poupas ou investes parte.": 2,
                "Gastas em algo que te apetece.": 1,
                "Nem pensas muito nisso.": 0
            }
        },
        {
            "texto": "Quando alguém fala de dinheiro, tu:",
            "opcoes": {
                "Ouves com interesse.": 2,
                "Ficas desconfortável.": 1,
                "Mudarias de assunto.": 0
            }
        }
    ],
    "Crenças sobre o dinheiro": [
        {
            "texto": "Qual destas frases se aproxima mais de ti?",
            "opcoes": {
                "O dinheiro é uma ferramenta para viver melhor.": 2,
                "O dinheiro muda as pessoas.": 0,
                "Dinheiro é importante, mas perigoso.": 1
            }
        },
        {
            "texto": "Quando ouves falar de pessoas ricas, pensas:",
            "opcoes": {
                "Trabalharam duro para chegar lá.": 2,
                "Devem ter tido sorte ou herança.": 0,
                "Nem todos conseguem, mas alguns merecem.": 1
            }
        }
    ],
    "Aprendizagem e crescimento": [
        {
            "texto": "Acreditas que todos podem aprender a investir com tempo e prática?",
            "opcoes": {
                "Sim, basta esforço e vontade.": 2,
                "Não, é preciso nascer com jeito.": 0,
                "Depende da pessoa.": 1
            }
        },
        {
            "texto": "Quando vês alguém a falar de finanças, tu:",
            "opcoes": {
                "Tomas notas e tentas aplicar.": 2,
                "Achas interessante, mas não fazes nada.": 1,
                "Desligas logo — não é para ti.": 0
            }
        }
    ]
}


def run():
    st.set_page_config(page_title="Quiz da Mentalidade Financeira", page_icon="💭")


    clean_session_questions()


    st.title(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    # Inicializar estado
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.respostas = []

        # Selecionar 1 pergunta aleatória por tema (para tornar mais curto e dinâmico)
        perguntas_selecionadas = []
        for tema, lista in PERGUNTAS2.items():
            perguntas_selecionadas.append(random.choice(lista))
        random.shuffle(perguntas_selecionadas)
        st.session_state.perguntas = perguntas_selecionadas

    total = len(st.session_state.perguntas)
    atual = st.session_state.index

    # --- Mostrar perguntas ---
    if atual < total:
        pergunta = st.session_state.perguntas[atual]

        st.markdown(f"### Pergunta {atual + 1} de {total}")
        st.write(pergunta["texto"])

        escolha = st.radio(
            "Escolhe uma opção:",
            list(pergunta["opcoes"].keys()),
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
            "Pergunta": [p["texto"] for p in st.session_state.perguntas],
            "Resposta": st.session_state.respostas
        })

        st.markdown("### 🧾 As tuas respostas")
        st.dataframe(df, hide_index=True)

        # Calcular pontuação total
        total_pontos = sum(
            PERGUNTAS2[tema][0]["opcoes"].get(resp, 0)
            if isinstance(PERGUNTAS2[tema][0], dict) else 0
            for tema, resp in zip(PERGUNTAS2.keys(), st.session_state.respostas)
        )

        # Como as perguntas são randomizadas, precisamos mapear o score dinamicamente:
        pontuacao = 0
        for i, resposta in enumerate(st.session_state.respostas):
            opcoes = st.session_state.perguntas[i]["opcoes"]
            pontuacao += opcoes[resposta]

        total_max = len(st.session_state.perguntas) * 2
        st.metric("Pontuação total", f"{pontuacao} / {total_max}")
        st.divider()

        # Feedback interpretativo
        if pontuacao >= total_max * 0.75:
            st.markdown("### 💪 Mentalidade de Crescimento Financeiro")
            st.success(
                "Vês o dinheiro como uma ferramenta e acreditas no esforço e planeamento. "
                "Estás preparado para construir riqueza com consciência e estratégia!"
            )
        elif pontuacao >= total_max * 0.5:
            st.markdown("### 🙂 Mentalidade em Transição")
            st.info(
                "Tens boas intenções e curiosidade, mas ainda deixas algumas crenças ou medos limitarem-te. "
                "Continua a aprender — pequenas mudanças vão trazer grandes resultados."
            )
        else:
            st.markdown("### 🚫 Barreiras Mentais Fortes")
            st.warning(
                "Algumas crenças ou experiências passadas ainda te impedem de ver o dinheiro como aliado. "
                "O primeiro passo é reconhecer e começar a mudar a tua mentalidade."
            )

        st.divider()
        st.markdown("💬 _'O primeiro investimento que precisas de fazer é na tua mentalidade.'_")

        # Botão para reiniciar o quiz
        if st.button("🔁 Recomeçar"):
            st.session_state.index = 0
            st.session_state.respostas = []
            perguntas_selecionadas = []
            for tema, lista in PERGUNTAS2.items():
                perguntas_selecionadas.append(random.choice(lista))
            random.shuffle(perguntas_selecionadas)
            st.session_state.perguntas = perguntas_selecionadas
            st.rerun()

    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")


if __name__ == "__main__":
    run()
