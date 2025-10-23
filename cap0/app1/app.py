import streamlit as st

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🌍 Sabias que existem várias moedas diferentes?",
    "description": (
        """
        Descobre como o dinheiro pode ter **valores diferentes** dependendo do país!  
        - 💵 Insere um valor numa moeda.  
        - 🔄 Vê quanto ele vale noutras moedas com base na taxa de câmbio.  
        - 📊 Experimenta diferentes cenários e aprende sobre conversão de moedas.
        """
    ),
    "video": "https://www.youtube.com/watch?v=5rbXGjqHCvk&t=261s"
}

def run():

    # --- Informação da aplicação ---
    st.subheader(APP_INFO["title"])
    st.video(APP_INFO["video"])
    st.info(APP_INFO["description"])

    st.divider()

    # --- Lista de moedas e câmbios fictícios (ou reais se quiseres ligar à API depois) ---
    moedas = {
        "Euro (€)": 1.0,
        "Dólar ($)": 1.10,
        "Libra (£)": 0.88,
        "Iene (¥)": 145.0,
        "Franco Suíço (CHF)": 0.97
    }

    # --- Inputs ---
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("💰 Valor:", min_value=0.0, value=100.0, step=1.0)
        moeda_origem = st.selectbox("💳 Moeda de origem:", list(moedas.keys()))
    with col2:
        moeda_destino = st.selectbox("💱 Moeda de destino:", list(moedas.keys()))

    # --- Cálculo de conversão ---
    valor_euro = valor / moedas[moeda_origem]  # converte para Euro como referência
    valor_convertido = valor_euro * moedas[moeda_destino]

    # --- Mostrar resultado ---
    st.success(f"{valor:.2f} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}!")

    # --- Tabela interativa de comparação ---
    st.markdown("### 💡 Valores equivalentes noutras moedas:")
    tabela = {m: round(valor_euro * r, 2) for m, r in moedas.items()}
    st.table(tabela)

if __name__ == "__main__":
    run()