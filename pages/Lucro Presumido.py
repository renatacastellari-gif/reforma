
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
        .card h3 {color: #fff; font-size: 26px; margin-bottom: 10px;}
        table {width:100%; border-collapse: collapse; margin-top:10px;}
        th, td {border:1px solid #3a3a3a; padding:8px;}
        th {background:#303030; color:#fff;}
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        .subtitulo {margin-top:15px; font-weight:600; color:#F2D5D7;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD COMPARATIVO + DUAS TABELAS
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

        <p class='subtitulo'>Detalhamento IRPJ</p>
        <table>
            <tbody>
                <tr>
                    <td>Presunção (receita bruta anual de até R$ 5 milhões)</td>
                    <td>32%</td>
                </tr>
                <tr>
                    <td>Presunção (parcela da receita bruta anual que excedeu R$ 5 milhões)</td>
                    <td>35,2%</td>
                </tr>
                <tr>
                    <td>Alíquota</td>
                    <td>15%</td>
                </tr>
                <tr>
                    <td>Código do DARF</td>
                    <td>2089</td>
                </tr>
            </tbody>
        </table>

        <p class='subtitulo'>Detalhamento CSLL</p>
        <table>
            <tbody>
                <tr>
                    <td>Presunção (receita bruta anual de até R$ 5 milhões)</td>
                    <td>32%</td>
                </tr>
                <tr>
                    <td>Presunção (parcela da receita bruta anual que excedeu R$ 5 milhões)</td>
                    <td>35,2%</td>
                </tr>
                <tr>
                    <td>Alíquota</td>
                    <td>9%</td>
                </tr>
                <tr>
                    <td>Código do DARF</td>
                    <td>2372</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
