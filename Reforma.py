
import streamlit as st
from pathlib import Path
# import pandas as pd  # remova se não usar

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(page_title="Reforma Tributária", page_icon="🟪")

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# =========================
# TELA DE LOGIN
# =========================
if not st.session_state.logged_in:
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun()
        else:
            st.error("Senha incorreta.")
else:
    # =========================
    # CONTEÚDO PROTEGIDO
    # =========================

    # ---- LOGO HINES (hines.svg/png/jpg/jpeg) ----
    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)

    if logo_path:
        try:
            st.image(str(logo_path), width=220)
        except Exception as e:
            st.warning(f"Não foi possível exibir a imagem '{logo_path.name}'. Detalhe: {e}")
            st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)
    else:
        st.info("Logo 'hines' não encontrado. Coloque hines.svg/png/jpg/jpeg na mesma pasta do app.")
        st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)

    # ---- Título ----
    st.markdown(
        "<h2 style='color:#B22222;font-family:Times New Roman,sans-serif;font-weight:700;text-align:center;border-bottom:2px solid #B22222;padding-bottom:8px;margin-bottom:20px;'>Reforma Tributária</h2>",
        unsafe_allow_html=True
    )

    st.image("Apresentação1.png")
    st.image("Apr.svg")
