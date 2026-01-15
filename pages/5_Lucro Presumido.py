
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
    # CSS GLOBAL COM FONTES MELHORADAS
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #1b1b1b;
        }
        body {
            color: #F9EEEF;
            font-family: 'Open Sans', Arial, sans-serif; /* Fonte para corpo */
        }
        .titulo-principal {
            font-family: 'Segoe UI', Roboto, Arial, sans-serif; /* Fonte para título */
            font-size: 38px;
            font-weight: 800;
            color: #B91E27;
            margin-bottom: 10px;
            text-align: left;
            border-bottom: 3px solid #B91E27;
            padding-bottom: 8px;
            letter-spacing: 0.5px;
        }
        .card {
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
            color: #f0f0f0;
            font-family: 'Open Sans', Arial, sans-serif; /* Fonte para conteúdo dos cards */
            font-size: 17px;
            line-height: 1.7;
        }
        .card h3 {
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.3px;
        }
        .highlight {
            color: #F2D5D7;
            font-weight: 600;
        }
        table {
            width:100%;
            border-collapse: collapse;
            margin-top:10px;
            font-size: 16px;
        }
        th, td {
            border:1px solid #3a3a3a;
            padding:10px;
        }
        th {
            background:#303030;
            color:#fff;
        }
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        tfoot td {font-weight:800; background:#2b2b2b;}
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # SEUS CARDS (mantidos)
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📌 Presunção – CNAE 6822-6/00</h3>
        <p>Para <b>prestação de serviços</b> (inclui Gestão e administração da propriedade imobiliária):</p>
        <ul>
            <li>Presunção padrão: <b>32%</b>.</li>
            <li>Com PLP 128/2025: <b>35,2%</b> sobre a parcela que exceder <b>R$ 5 milhões/ano</b>.</li>
            <li>No trimestre, limite proporcional: <b>R$ 1.250.000</b>.</li>
        </ul>
        <p class="highlight">Até R$ 1.250.000 → 32%; excedente → 35,2%.</p>
        <p>Adicional IRPJ: 10% sobre lucro presumido que exceder <b>R$ 60 mil/trimestre</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # (Demais cards continuam iguais...)
