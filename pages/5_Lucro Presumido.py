
import streamlit as st

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

if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

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
    # CSS GLOBAL COM FONTE
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #1b1b1b;
            font-family: Consolas, Menlo, Monaco, 'Courier New', monospace; /* Fonte aplicada */
        }
        body {
            color: #F9EEEF;
        }
        .titulo-principal {
            font-size: 34px; font-weight: 800; color: #B91E27;
            border-bottom: 2px solid #B91E27; padding-bottom: 8px;
        }
        .card {
            background-color: #2a2a2a; padding: 20px; border-radius: 12px;
            margin: 20px 0; border-left: 6px solid #B91E27;
        }
        .card h3 {color: #fff; font-size: 26px; margin-bottom: 14px;}
        .highlight {color: #F2D5D7; font-weight: 600;}
        table {width:100%; border-collapse: collapse; margin-top:10px;}
        th, td {border:1px solid #3a3a3a; padding:10px;}
        th {background:#303030; color:#fff;}
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        tfoot td {font-weight:800; background:#2b2b2b;}
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # CONTEÚDO
    # =========================
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # Seus cards continuam aqui...
