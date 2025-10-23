import streamlit as st
import pandas as pd
import plotly.express as px

# --- Informação da aplicação ---
APP_INFO = {
    "title": "💰 Afinal, o que é o dinheiro e para que serve?",
    "description": (
        """
        Bem-vindo à mini **primeira aula do nosso curso**!  
        Aqui vais descobrir, de forma prática e divertida, **para que serve o dinheiro**.  

        📌 **O que vais aprender nesta aplicação:**
        - 🐔 **Trocar:** Quantas galinhas valem uma bicicleta? Descobre como o dinheiro surgiu para simplificar as trocas.  
        - 🏦 **Guardar:** Aprende a poupar ao longo do tempo e ver como pequenas poupanças crescem.  
        - ⚖️ **Comparar:** Compara o valor de diferentes produtos e toma decisões inteligentes.  

        💡 Esta aplicação é parte do projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}


def run():
    st.subheader(APP_INFO["title"])

    st.video(APP_INFO["video"])

    st.info(APP_INFO["description"])


    st.markdown("Nesta mini aplicação vamos descobrir **as três grandes funções do dinheiro**, de forma prática e divertida!")

    st.divider()
    

    # Tabs
    st.subheader("Agora Tu!")

    aba1, aba2, aba3 = st.tabs(["🐔 Trocar", "🏦 Guardar", "⚖️ Comparar"])

    # --- 1. TROCAR ---
    with aba1:
        st.subheader("🐔 Trocar galinhas ")
        st.info("""
    Antes de existir dinheiro, as pessoas faziam **trocas diretas**. Por exemplo, uma galinha por um saco de arroz.
    Mas... e se quisesses trocar **galinhas por uma bicicleta**? 🤔  
    Vamos descobrir quantas galinhas vale uma bicicleta!
        """)

        preco_galinha = st.number_input("💸 Preço de uma galinha (€):", min_value=0.0, value=10.0, step=0.5)
        preco_bicicleta = st.number_input("🚲 Preço de uma bicicleta (€):", min_value=0.0, value=150.0, step=5.0)

        if preco_galinha > 0:
            galinhas_necessarias = preco_bicicleta / preco_galinha
            st.success(f"Precisarias de aproximadamente **{galinhas_necessarias:.1f} galinhas** para comprar uma bicicleta! 🐔➡️🚲")
            st.caption("💡 O dinheiro surgiu para simplificar estas trocas — imagina andar com tudo isso atrás!")
        else:
            st.warning("Define um preço válido para a galinha 😉")

    # --- 2. GUARDAR ---
    with aba2:
        st.subheader("🏦 Função 2: Guardar — poupar para o futuro")
        st.write("""
    O dinheiro também serve para **guardar valor** — ou seja, poupar.
    Vamos ver quanto conseguirias juntar ao longo do tempo.
        """)

        poupanca_inicial = st.number_input("💰 Poupança inicial (€):", min_value=0.0, value=50.0, step=5.0)
        poupanca_mensal = st.number_input("📆 Poupança mensal (€):", min_value=0.0, value=20.0, step=5.0)
        meses = st.slider("Durante quantos meses queres poupar?", 1, 60, 12)

        total = poupanca_inicial + poupanca_mensal * meses
        st.info(f"Após {meses} meses, terás **{total:.2f} €**! 💪")

        st.caption("💡 Poupar é o primeiro passo para investir e alcançar objetivos maiores!")

    # --- 3. MEDIR ---
    with aba3:
        st.subheader("⚖️ Função 3: Medir — comparar valores")
        st.write("""
    O dinheiro ajuda-nos a **comparar o valor** das coisas.
    Por exemplo, qual destes produtos é mais caro?
        """)

        produto1 = st.text_input("Produto 1:", "Bicicleta")
        preco1 = st.number_input("Preço do produto 1 (€):", min_value=0.0, value=200.0)
        produto2 = st.text_input("Produto 2:", "Telemóvel")
        preco2 = st.number_input("Preço do produto 2 (€):", min_value=0.0, value=300.0)

        if preco1 > preco2:
            st.warning(f"🟡 O {produto1} é mais caro do que o {produto2}.")
        elif preco1 < preco2:
            st.success(f"🟢 O {produto2} é mais caro do que o {produto1}.")
        else:
            st.info("⚖️ Ambos têm o mesmo preço!")

        st.caption("💡 O dinheiro permite comparar e decidir — facilita as escolhas no dia a dia.")

    st.markdown("---")
    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()