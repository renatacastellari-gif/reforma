import streamlit as st
import pandas as pd
from pathlib import Path

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
    # CSS – CARDS
    # =========================
    st.markdown("""
    <style>
        .stApp {
            background-color: #1b1b1b;
            color: #F9EEEF;
        }

        h1, h2, h3 {
            color: #B91E27;
        }

        .card {
            background-color: #2a2a2a;
            padding: 22px;
            border-radius: 14px;
            border-left: 6px solid #B91E27;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 22px;
            font-weight: 700;
            color: #B91E27;
            margin-bottom: 10px;
        }

        .card-text {
            font-size: 16px;
            color: #EAEAEA;
            line-height: 1.6;
        }

        .highlight {
            color: #F2D5D7;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<h2 style='text-align:center;'>PIS e COFINS → CBS</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;color:#cccccc;'>Resumo prático da Reforma Tributária para empresas de serviços</p>",
        unsafe_allow_html=True
    )

    # =========================
    # CARD – 2026
    # =========================
    st.markdown("""
    <div class="card">
        <div class="card-title">📅 2026 — Período de Teste</div>
        <div class="card-text">
            ✔ Entrada da <span class="highlight">CBS em fase piloto</span><br>
            ✔ Alíquota teste: <span class="highlight">0,9%</span><br>
            ✔ Valor <span class="highlight">compensado com PIS e COFINS</span><br>
            ✔ Possível dispensa de recolhimento se cumprir obrigações acessórias<br><br>
            ❗ <b>Não há aumento real de carga tributária em 2026</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – 2027
    # =========================
    st.markdown("""
    <div class="card">
        <div class="card-title">🚨 A partir de 2027</div>
        <div class="card-text">
            ❌ <b>PIS e COFINS são extintos</b><br>
            ✔ Entra a <span class="highlight">CBS definitiva</span><br><br>

            <b>Características da CBS:</b><br>
            • Não cumulativa (modelo IVA)<br>
            • Crédito financeiro amplo<br>
            • Alíquota estimada: <span class="highlight">~8,8%</span><br><br>

            ⚠️ Empresas de serviços com poucos insumos
            tendem a sentir <b>aumento real da carga tributária</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – COMPARATIVO
    # =========================
    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Comparativo Geral</div>
        <div class="card-text">
            • Até 2025 → PIS + COFINS (3,65%) — sem crédito<br>
            • 2026 → CBS teste (0,9%) — impacto neutro<br>
            • 2027+ → CBS definitiva (~8,8%) — impacto maior
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – CONCLUSÃO
    # =========================
    st.markdown("""
    <div class="card">
        <div class="card-title">🧾 Conclusão Prática</div>
        <div class="card-text">
            ✔ 2026 é um ano de adaptação<br>
            ✔ A mudança financeira começa em 2027<br>
            ✔ Revisão de preços e contratos será essencial
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – EXCEL
    # =========================
    st.markdown("""
    <div class="card">
        <div class="card-title">📈 Dados Detalhados (Excel)</div>
    </div>
    """, unsafe_allow_html=True)

    excel_path = Path("tabela.xlsx")
    if excel_path.exists():
        df = pd.read_excel(excel_path)
        st.dataframe(df, use_container_width=True, height=420)
    else:
        st.warning("Arquivo 'tabela.xlsx' não encontrado.")
