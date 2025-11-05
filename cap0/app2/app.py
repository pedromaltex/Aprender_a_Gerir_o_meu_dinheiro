import streamlit as st

# --- Informação da aplicação ---
APP_INFO = {
    "title": "⚖️ Preço vs Valor",
    "description": (
        """
        Aprende a distinguir entre **preço** e **valor**! ⚖️💰  

        📌 **O que vais aprender nesta aula:**
        - 💵 **Preço:** é o que pagas por um produto ou serviço.  
        - 💎 **Valor:** é o quanto esse produto realmente **significa ou importa** para ti.  
        - 🤔 **Refletir:** Nem sempre o produto mais caro é o mais valioso — depende das tuas prioridades.  

        💡 **Desafio:** Escolhe um produto, indica quanto estarias disposto a pagar e descobre se o preço faz sentido para ti.  

        💡 Esta aplicação é parte do projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

def run():
    st.set_page_config(page_title="Preço vs Valor", page_icon="⚖️")
    
    st.subheader(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])
    st.divider()


    # --- Inputs do produto ---
    produto = st.text_input("🛒 Produto:", "Bicicleta")
    preco = st.number_input("💰 Preço do produto (€):", min_value=0.0, value=100.0, step=5.0)
    disposto = st.number_input("💭 Quanto estavas disposto a pagar (€)?", min_value=0.0, value=80.0, step=5.0)
    valor_perc = st.slider("🌟 Quanto valor este produto tem para ti? (1 = pouco, 10 = muito)", 1, 10, 5)

    st.markdown("---")
    st.subheader("Resultado:")

    # --- Lógica de avaliação ---
    if preco <= disposto:
        st.success(f"✅ O {produto} está dentro do valor que consideras justo! Boa compra.")
    elif preco <= disposto * 1.2:
        st.info(f"ℹ️ O {produto} custa um pouco mais do que querias pagar, mas pode valer a pena se o valor for alto ({valor_perc}/10).")
    else:
        st.warning(f"⚠️ O {produto} está **acima do que estás disposto a pagar**. Talvez o preço não compense o valor que lhe atribuis.")

    # --- Mostrar resumo ---
    st.markdown("### Resumo da tua escolha")
    st.write(f"- Produto: {produto}")
    st.write(f"- Preço: {preco:.2f} €")
    st.write(f"- Valor percebido: {valor_perc}/10")
    st.write(f"- Estavas disposto a pagar: {disposto:.2f} €")

    st.markdown("---")
    st.caption("Projeto *Todos Contam* — Aprender a Gerir o Meu Dinheiro 🪙")

if __name__ == "__main__":
    run()
