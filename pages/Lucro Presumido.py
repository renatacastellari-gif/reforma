
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
    # CSS GLOBAL
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {background-color: #1b1b1b;}
        body {color: #F9EEEF; font-family: Consolas, monospace;}
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
        .info-block {margin-top:16px; padding:12px; background:#222; border-radius:8px;}
        .info-block h4 {margin-bottom:8px; color:#F2D5D7;}
        .info-block ul {margin:0; padding-left:18px;}
        .info-block li {margin-bottom:6px;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD COMPARATIVO + INFORMAÇÕES ADICIONAIS
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📊 Comparativo de alíquotas efetivas</h3>
        <table>
            <thead>
                <tr>
                    <th>Tributo</th>
                    <th>Atual (32%)</th>
                    <th>Novo (35,2%)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>IRPJ (15%)</td>
                    <td>4,80%</td>
                    <td>5,28%</td>
                </tr>
                <tr>
                    <td>Adicional IRPJ (10% sobre lucro presumido acima de R$ 60 mil/mês)</td>
                    <td>3,20%</td>
                    <td>3,52%</td>
                </tr>
                <tr>
                    <td>CSLL (9%)</td>
                    <td>2,88%</td>
                    <td>3,17%</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td><b>Total</b></td>
                    <td><b>10,88%</b></td>
                    <td><b>11,97%</b></td>
                </tr>
            </tfoot>
        </table>

        <!-- Informações adicionais -->
        <div class="info-block">
            <h4>Detalhamento IRPJ</h4>
            <ul>
                <li>Presunção até R$ 5 milhões: <b>32%</b></li>
                <li>Presunção excedente: <b>35,2%</b></li>
                <li>Alíquota: <b>15%</b></li>
                <li>Código DARF: <b>2089</b></li>
            </ul>
        </div>

        <div class="info-block">
            <h4>Detalhamento CSLL</h4>
            <ul>
                <li>Presunção até R$ 5 milhões: <b>32%</b></li>
                <li>Presunção excedente: <b>35,2%</b></li>
                <li>Alíquota: <b>9%</b></li>
                <li>Código DARF: <b>2372</b></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
``
