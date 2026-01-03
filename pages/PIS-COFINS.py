import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Reforma Tributária – PIS/COFINS",
    page_icon="🟪",
    layout="centered"
)

# =========================
# LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.title("🔒 Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO
# =========================
else:

    # =========================
    # CSS GLOBAL
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #000000;
        }

        .titulo {
            font-size: 36px;
            font-weight: bold;
            color: #B11226;
            margin-bottom: 10px;
        }

        .subtitulo {
            font-size: 22px;
            font-weight: bold;
            color: #B11226;
            margin-top: 35px;
        }

        .texto {
            font-size: 16px;
            color: #E0E0E0;
            line-height: 1.6;
        }

        .box {
            background-color: #0F0F0F;
            padding: 20px;
            border-radius: 14px;
            margin-top: 15px;
            border: 1px solid #2A2A2A;
        }

        /* TABELA FINAL */
        .tabela-final {
            width: 100%;
            border-collapse: collapse;
            margin-top: 25px;
            font-size: 15px;
        }

        .tabela-final th {
            border: 1px solid #555555;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }

        .tabela-final td {
            border: 1px solid #555555;
            padding: 10px;
            text-align: center;
            color: #EAEAEA;
            background-color: #0B0B0B;
        }

        .th-ano {
            background-color: #C9DEF1;
            color: #000000;
        }

        .th-atual {
            background-color: #C9DEF1;
            color: #000000;
        }

        .th-novo {
            background-color: #C9DEF1;
            color: #000000;
        }

        .th-sub {
            background-color: #FFFFFF;
            color: #000000;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='texto'>
    Visão resumida da transição dos tributos federais conforme a Reforma Tributária,
    aplicada a empresas prestadoras de serviços.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 2026
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box texto'>
    ✔ Entrada da CBS em fase piloto<br>
    ✔ Alíquota teste: 0,9%<br>
    ✔ Valor recolhido pode ser compensado com PIS e COFINS<br>
    ✔ Possível dispensa de recolhimento mediante cumprimento das obrigações acessórias<br><br>
    ❗ Não há aumento real de carga tributária em 2026.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 2027
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box texto'>
    ❌ Extinção do PIS e da COFINS<br>
    ✔ Entrada definitiva da CBS<br>
    • Modelo não cumulativo (IVA)<br>
    • Alíquota a ser definida por lei específica
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # TABELA FINAL (REPLICA)
    # =========================
    st.markdown("<div class='subtitulo'>📊 Linha do Tempo dos Tributos</div>", unsafe_allow_html=True)

    st.markdown("""
    <table class="tabela-final">
        <tr>
            <th rowspan="2" class="th-ano">Ano</th>
            <th colspan="2" class="th-atual">Tributos Atuais</th>
            <th colspan="1" class="th-novo">Novos Tributos</th>
        </tr>
        <tr>
            <th class="th-sub">PIS/PASEP</th>
            <th class="th-sub">COFINS</th>
            <th class="th-sub">CBS</th>
        </tr>

        <tr>
            <td>2024</td>
            <td colspan="2">Sem mudanças</td>
            <td>-</td>
        </tr>

        <tr>
            <td>2025</td>
            <td colspan="2">Sem mudanças</td>
            <td>-</td>
        </tr>

        <tr>
            <td>2026</td>
            <td colspan="2">
                Alíquotas mantidas; com a possibilidade de compensação
                de 1% dos novos tributos (CBS 0,9% e IBS 0,1%)
            </td>
            <td>Alíquota teste: 0,9%</td>
        </tr>

        <tr>
            <td>2027</td>
            <td rowspan="5" colspan="2">Extinção</td>
            <td>Alíquota estabelecida (-)</td>
        </tr>

        <tr>
            <td>2028</td>
            <td>0,1%</td>
        </tr>

        <tr>
            <td>2029</td>
            <td></td>
        </tr>

        <tr>
            <td>2030</td>
            <td></td>
        </tr>

        <tr>
            <td>2031</td>
            <td>Alíquota estabelecida</td>
        </tr>

        <tr>
            <td>2032</td>
            <td colspan="3"></td>
        </tr>

        <tr>
            <td>2033</td>
            <td colspan="3"></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
