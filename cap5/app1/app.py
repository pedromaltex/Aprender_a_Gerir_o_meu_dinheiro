import streamlit as st
import random

# --- Informação da aplicação ---
APP_INFO = {
    "title": "🏁 Aula Final – Conclusão do Curso",
    "description": (
        """
        Chegaste ao fim da tua jornada! 🎉  

        Ao longo deste curso aprendeste a **pensar sobre dinheiro de forma inteligente**,  
        a planear, poupar, investir e — acima de tudo — a **tomar decisões conscientes**. 💡  

        A educação financeira não é sobre saber números,  
        mas sim sobre **entender escolhas** e **criar liberdade**.  
        Cada passo que deres a partir de agora conta para o teu futuro. 🚀  
        """
    ),
}


def run():
    st.subheader(APP_INFO["title"])
    st.markdown(APP_INFO["description"])
    st.divider()

    st.write("### 💬 O que aprendeste até agora:")
    st.markdown(
        """
        - Que **ser rico não é ter muito, mas precisar de menos** 💭  
        - A importância de um **fundo de emergência** e de um **orçamento pessoal** 🧾  
        - Como o **tempo e os juros compostos** podem multiplicar o teu dinheiro ⏳  
        - Que **investir é a melhor defesa contra a inflação** 📈  
        - E que uma **mentalidade financeira equilibrada** é o verdadeiro superpoder 💪  
        """
    )

    st.info(
        """
        💡 *Lembra-te: o dinheiro é apenas uma ferramenta.  
        Usa-o para construir a vida que desejas, não para te prender a ela.*  
        """
    )

    st.divider()
    st.write("### 🎯 Pronto para o desafio final?")
    st.markdown(
        """
        No **Quiz Final**, vais testar o que aprendeste e descobrir o teu **perfil financeiro**.  
        Responde às perguntas, reflete sobre as escolhas e vê o quanto evoluíste! 🧠💰
        """
    )

    if st.button("👉 Fazer o Quiz Final!"):
        st.success("Abre o módulo do **Quiz Final** no menu lateral para começar o desafio! 🚀")

    st.divider()
    st.markdown(
        """
        🙏 **Obrigado por chegares até aqui!**  
        Cada aula, cada simulação e cada reflexão foram um passo na tua jornada rumo à liberdade financeira.  
        
        Continua a aprender, continua a crescer — e lembra-te:  
        > “A melhor altura para começar foi ontem. A segunda melhor é hoje.” 💫
        """
    )
