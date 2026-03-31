import streamlit as st
from pathlib import Path

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Reforma Tributária",
    page_icon="🟥",
    layout="centered"
)

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral se não estiver logado
if not st.session_state.logged_in:
    st.markdown(
        "<style>[data-testid='stSidebar']{display:none;}</style>",
        unsafe_allow_html=True
    )

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

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:

    # =========================
    # TIPOGRAFIA
    # =========================
    BODY_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"

    # =========================
    # CSS GLOBAL
    # =========================
    style_str = f"""
    <style>
        html, body, [class*="css"] {{
            background-color: #1b1b1b;
        }}
        body {{
            font-family: {BODY_FONT};
            color: #F9EEEF;
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        .content-wrapper {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 1.2rem;
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
        }}

        input, textarea {{
            background-color: #2a2a2a !important;
            color: #F9EEEF !important;
            border: 1px solid #EBBFC1 !important;
        }}

        .stButton > button {{
            background-color: #B91E27;
            color: #F9EEEF;
            border-radius: 8px;
            border: none;
            font-weight: 600;
        }}

        .stButton > button:hover {{
            background-color: #8f1620;
        }}

        .card {{
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
        }}

        .card h3 {{
            font-size: 26px;
            font-weight: 800;
            margin-bottom: 12px;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown(
        "<div class='titulo-principal'>Reforma Tributária | Impactos nas Incorporações Imobiliárias</div>",
        unsafe_allow_html=True
    )

    # =========================
    # CARD PDF (SIMPLES)
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>📄 Documento</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    with open("seu_arquivo.pdf", "rb") as f:
        st.download_button(
            label="📥 Baixar PDF",
            data=f,
            file_name="documento.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # =========================
    # CARD INCORPORADORA
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>Incorporadora</h3>
            <ul>
                <li>Compra ou negocia terrenos</li>
                <li>Desenvolve o projeto</li>
                <li>Obtém aprovações</li>
                <li>Define o conceito</li>
                <li>Contrata construtora</li>
                <li>Comercializa unidades</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # VÍDEO CORRIGIDO
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🎥 Vídeo Explicativo</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.video("https://www.youtube.com/watch?v=ITUei7wDPH4")

    st.markdown("</div>", unsafe_allow_html=True)
