
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
        """
        <style>
            [data-testid="stSidebar"] { display: none; }
        </style>
        """,
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
    # CSS GLOBAL (TEMA ESCURO + TÍTULO + CARDS)
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

        /* Título principal */
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

        /* Inputs e botões */
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
            color: #F9EEEF;
        }}

        /* Cards */
        .card {{
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
            color: #f0f0f0;
        }}

        .card h3 {{
            font-family: {HEADING_FONT};
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.2px;
        }}

        .card ul {{
            margin: 10px 0 0 18px;
            padding: 0;
            list-style-type: disc;
        }}

        .card li {{
            font-size: 17px;
            line-height: 1.7;
            margin-bottom: 6px;
            color: #e6e6e6;
        }}

        .card li b {{
            color: #ffffff;
            font-weight: 700;
        }}

        .card p {{
            margin: 0;
            color: #dcdcdc;
            font-size: 16px;
            line-height: 1.65;
        }}

        .highlight {{
            color: #F2D5D7;
            font-weight: 600;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Nota Nacional | Nota Carioca</div>", unsafe_allow_html=True)

    # =========================
    # CARD – Obrigatoriedade Nota Nacional (IBS)
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🟦 Obrigatoriedade emissão pela Nota Nacional</h3>
            <p>
                A <b>a partir de 01/01/2026</b> os contribuintes são obrigados a emitir suas notas no Emissor Nacional.
            </p>
            <p class="highlight">
               Para possibilitar a emissão das guias de recolhimento do ISS a partir do período de apuração 01/2026, 
                os contribuintes deverão, além da emissão da NFS-e individualizada no padrão nacional, emitir, de forma consolidada, 
                a Declaração Mensal de Serviços Prestados. A emissão será realizada na forma de NFS-e - Nota Carioca.
                Deverá ser emitida uma declaração mensal para cada serviço prestado</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # NOVO CARD – NFS-e individual & Declaração consolidada
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🟥 NFS‑e individual & Declaração consolidada</h3>
            <ul>
                <li><b>NFS‑e individual</b><br/>
                    <span class="highlight">Onde?</span> ➜ Sistema Nacional da NFS‑e
                </li>
                <li><b>Declaração consolidada</b><br/>
                    <span class="highlight">Onde?</span> ➜ Nota Carioca &nbsp;|&nbsp;
                    <span class="highlight">Como?</span> ➜ Consolidada mensal
                    <br/>Uma declaração para cada código de serviço.
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)
