import streamlit as st
from pathlib import Path
# import pandas as pd  # remova se não usar

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Reforma Tributária",
    page_icon="🟥",
    layout="centered"
)

# =========================
# CSS - TEMA ESCURO + PALETA
# =========================
st.markdown("""
<style>
/* Fundo geral */
.stApp {
    background-color: #1b1b1b;
    color: #F9EEEF;
}

/* Esconder menu e rodapé */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Títulos */
h1, h2, h3, h4 {
    color: #B91E27;
}

/* Caixa de texto e inputs */
input, textarea {
    background-color: #2a2a2a !important;
    color: #F9EEEF !important;
    border: 1px solid #EBBFC1 !important;
}

/* Botões */
.stButton > button {
    background-color: #B91E27;
    color: #F9EEEF;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: #8f1620;
    color: #F9EEEF;
}

/* Cards */
.card {
    background-color: #2a2a2a;
    padding: 18px;
    border-radius: 12px;
    border-left: 6px solid #B91E27;
    margin-bottom: 16px;
}

/* Destaque */
.highlight {
    color: #F2D5D7;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral se não estiver logado
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
            st.success("Acesso liberado!")
            st.rerun()
        else:
            st.error("Senha incorreta.")

else:
    # =========================
    # CONTEÚDO PROTEGIDO
    # =========================

    # ---- LOGO HINES ----
    candidatos = [
        Path("hines.svg"),
        Path("hines.png"),
        Path("hines.jpg"),
        Path("hines.jpeg")
    ]
    logo_path = next((p for p in candidatos if p.exists()), None)

    if logo_path:
        st.image(str(logo_path), width=220)
    else:
        st.markdown(
            "<h3 style='color:#B91E27;'>🟥 Hines – Painel Tributário</h3>",
            unsafe_allow_html=True
        )

    # ---- Título ----
    st.markdown("""
        <h2 style="
            text-align:center;
            border-bottom:2px solid #B91E27;
            padding-bottom:10px;
            margin-bottom:30px;
        ">
            ISS - IBS
        </h2>
    """, unsafe_allow_html=True)
