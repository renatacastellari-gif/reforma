import streamlit as st
import pandas as pd

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Reforma Tributária | PIS e COFINS → CBS",
    page_icon="🟥",
    layout="centered"
)

# =========================
# SENHA / LOGIN
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
        html, body, [class*="css"] {
            background-color: #000000;
        }

        .titulo {
            font-size: 38px;
            font-weight: 800;
            color: #8B0000;
            margin-bottom: 12px;
        }

        .subtitulo {
            font-size: 22px;
            font-weight: 700;
            color: #8B0000;
            margin-top: 35px;
        }

        .texto {
            font-size: 16px;
            color: #E6E6E6;
            line-height: 1.7;
        }

        .box {
            background: linear-gradient(145deg, #0E0E0E, #050505);
            padding: 22px;
            border-radius: 16px;
            margin-top: 15px;
            border: 1px solid #2A2A2A;
            box-shadow: 0 0 18px rgba(139,0,0,0.20);
        }

        /* ===== TABELA ===== */

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
            font-size: 15px;
        }

        th {
            background-color: #8B0000;
            color: #FFFFFF;
            padding: 12px;
            border: 1px solid #3A3A3A;
        }

        td {
            background-color: #0B0B0B;
            color: #EAEAEA;
            padding: 10px;
            text-align: center;
            border: 1px solid #2F2F2F;
        }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # CONTEÚDO
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
        ✓ Entrada da CBS em fase piloto<br>
        ✓ Alíquota teste: 0,9%<br>
        ✓ Valor recolhido pode ser compensado com PIS e COFINS<br>
        ✓ Possível dispensa de recolhimento mediante cumprimento das obrigações acessórias<br><br>
        ❗ <b>Não há aumento real de carga tributária em 2026.</b>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 2027+
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box texto'>
        ✖ Extinção do PIS e da COFINS<br>
        ✓ Entrada definitiva da CBS<br>
        • Modelo não cumulativo (IVA)<br>
        • Alíquota a ser definida por lei específica
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # TABELA ANTERIOR (MANTIDA)
    # =========================
    st.markdown("<div class='subtitulo'>📊 Comparativo Geral</div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Tributo": ["PIS", "COFINS", "CBS"],
        "Situação Atual": ["Vigente", "Vigente", "Em fase de teste"],
        "Situação Futura": ["Extinto", "Extinto", "Definitivo"]
    })

    st.dataframe(df, use_container_width=True)

    # =========================
    # NOVA TABELA (NO FINAL)
    # =========================
    st.markdown("<div class='subtitulo'>📈 Linha do Tempo dos Tributos</div>", unsafe_allow_html=True)

    st.markdown("""
    <table>
        <tr>
            <th rowspan="2">Ano</th>
            <th colspan="2">Tributos Atuais</th>
            <th>Novos Tributos</th>
        </tr>
        <tr>
            <th>PIS/PASEP</th>
            <th>COFINS</th>
            <th>CBS</th>
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
                Alíquotas mantidas; possibilidade de compensação
                de 1% dos novos tributos (CBS 0,9% e IBS 0,1%)
            </td>
            <td>Alíquota teste: 0,9%</td>
        </tr>

        <tr>
            <td>2027</td>
            <td colspan="2" rowspan="4">Extinção</td>
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
            <td colspan="2"></td>
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
