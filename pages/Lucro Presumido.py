
import streamlit as st
from pathlib import Path

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Reforma Tributária – PIS/COFINS",
    page_icon="🟥",
    layout="centered"
)

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Esconde sidebar se não estiver logado
if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# =========================
# TELA DE LOGIN
# =========================
if not st.session_state.logged_in:
    st.title("🔒 Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado!")
            st.rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:
 

    # =========================
    # TIPOGRAFIA (ajuste aqui se quiser trocar)
    # =========================
    BODY_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    # Ex.: para visual “clean”:
    # BODY_FONT = "'Segoe UI', Roboto, Helvetica, Arial, system-ui, -apple-system, sans-serif"
    # HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"

    # =========================
    # CSS GLOBAL (FUNDO PRETO + CARDS + TIPOGRAFIA)
    # =========================
    style_str = f"""
    <style>
        html, body, [class*="css"] {{
            background-color: #000000;
        }}
        body {{
            font-family: {BODY_FONT};
        }}

        .content-wrapper {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        .titulo-principal {{
            font-family: {HEADING_FONT};
            font-size: 34px;
            font-weight: 800;
            color: #B91E27;
            margin-bottom: 10px;
            text-align: left;
            border-bottom: 2px solid #B91E27;
            padding-bottom: 8px;
            letter-spacing: 0.2px;
        }}

        .subtitulo {{
            font-size: 22px;
            font-weight: 700;
            color: #D96569;
            margin-top: 30px;
        }}

        .texto {{
            font-size: 16px;
            color: #dddddd;
            line-height: 1.65;
        }}
