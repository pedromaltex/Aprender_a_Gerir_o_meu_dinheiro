import streamlit as st
import importlib
import os
import pkgutil
from videos_link import MAIN_VIDEO_URL

st.set_page_config(page_title="Aprender a Gerir o Meu Dinheiro", page_icon="💸", layout="centered")


# --- Encontrar capítulos disponíveis ---
@st.cache_resource
def load_chapters():
    chapters = []
    chapter_dirs = sorted(
        [d for d in os.listdir() if d.startswith("cap") and os.path.isdir(d)],
        key=lambda x: int(x.replace("cap", ""))  # Ordena cap1, cap2, cap10 corretamente
    )
    for d in chapter_dirs:
        try:
            info_module = importlib.import_module(f"{d}.chapter_info")
            chapter_info = info_module.CHAPTER_INFO
            chapter_info["path"] = d
            chapters.append(chapter_info)
        except Exception as e:
            st.warning(f"⚠️ Falha ao carregar {d}: {e}")
    return chapters

chapters = load_chapters()


# --- Estado da app ---
if "selected_chapter" not in st.session_state:
    st.session_state.selected_chapter = None
if "selected_simulation" not in st.session_state:
    st.session_state.selected_simulation = None

# ========================================================
# 🧭 SIDEBAR – ÍNDICE AUTOMÁTICO
# ========================================================
st.sidebar.header("📚 Temas a Aprender")

for c in chapters:
    with st.sidebar.expander(c["title"], expanded=False):
        # Detetar simulações do capítulo
        sims = []
        for finder, name, ispkg in pkgutil.iter_modules([c["path"]]):
            if ispkg:
                app_path = f"{c['path']}.{name}.app"
                try:
                    app_module = importlib.import_module(app_path)
                    sims.append({
                        "title": app_module.APP_INFO["title"],
                        "module": app_path
                    })
                except Exception:
                    pass

        # Mostrar botões das simulações
        for s in sims:
            if st.button(f"▶️ {s['title']}", key=f"{c['path']}_{s['title']}"):
                st.session_state.selected_chapter = c
                st.session_state.selected_simulation = s
                st.rerun()

# Botão para voltar
if st.session_state.selected_chapter or st.session_state.selected_simulation:
    st.sidebar.divider()
    if st.sidebar.button("⬅️ Voltar ao início"):
        st.session_state.selected_chapter = None
        st.session_state.selected_simulation = None
        st.rerun()

# Créditos
st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por **Pedro Maltez**")

# ========================================================
# 🧩 CONTEÚDO PRINCIPAL
# ========================================================

# Caso 1 — Simulação ativa
if st.session_state.selected_simulation:
    sim = st.session_state.selected_simulation
    chapter = st.session_state.selected_chapter
    app_module = importlib.import_module(sim["module"])

    st.markdown(f"## {chapter['title']}")
    app_module.run()

    # Botão voltar no fim da simulação
    st.divider()
    if st.button("⬅️ Voltar ao início"):
        st.session_state.selected_chapter = None
        st.session_state.selected_simulation = None
        st.rerun()

# Caso 2 — Capítulo selecionado, mas sem simulação
elif st.session_state.selected_chapter:
    chapter = st.session_state.selected_chapter
    st.header(f"📘 {chapter['title']}")
    st.markdown(chapter["description"])
    st.divider()

    sims = []
    for finder, name, ispkg in pkgutil.iter_modules([chapter["path"]]):
        if ispkg:
            app_path = f"{chapter['path']}.{name}.app"
            try:
                app_module = importlib.import_module(app_path)
                sims.append({
                    "title": app_module.APP_INFO["title"],
                    "description": app_module.APP_INFO["description"],
                    "module": app_path
                })
            except Exception as e:
                st.warning(f"⚠️ Erro ao carregar {app_path}: {e}")

    if sims:
        for s in sims:
            with st.container(border=True):
                st.markdown(f"#### {s['title']}")
                st.markdown(s["description"])
                if st.button(f"▶️ Iniciar {s['title']}", key=s["module"]):
                    st.session_state.selected_simulation = s
                    st.rerun()
    else:
        st.info("🚧 Ainda não há simulações neste capítulo.")

    # Botão voltar no fim da simulação
    st.divider()
    if st.button("⬅️ Voltar ao início"):
        st.session_state.selected_chapter = None
        st.session_state.selected_simulation = None
        st.rerun()

# Caso 3 — Página inicial (nenhum capítulo nem simulação)
else:
    st.title("💸 Aprender a Gerir o Meu Dinheiro - Aplicação")
    st.video(MAIN_VIDEO_URL)

    st.info("""
    👋 Olá! Pronto para descobrir o que o teu dinheiro pode fazer por ti?  

    Aqui vais **jogar, simular e aprender** como gerir melhor as tuas finanças.  
    Podes criar orçamentos, testar estratégias de poupança, fazer investimentos fictícios e até competir em quizzes! 🎯  

    💰 **Quanto melhor entenderes o dinheiro, mais longe ele te pode levar.**  
    Escolhe um módulo e começa a aventura! 🚀
    """)
    st.divider()

    st.subheader("📘 O que queres aprender?")
    for c in chapters:
        with st.container(border=True):
            st.markdown(f"### {c['title']}")
            st.markdown(c["description"])
            if st.button(f"➡️ Abrir {c['title']}", key=c["path"]):
                st.session_state.selected_chapter = c
                st.rerun()
