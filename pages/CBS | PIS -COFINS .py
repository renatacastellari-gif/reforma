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
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Esconde sidebar se não estiver logado
if not st.session_state.logged_in:
    st.markdown(
        "<style>[data-testid='stSidebar']{display:none;}</style>",
        unsafe_allow_html=True
    )

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
    # CSS GLOBAL (FUNDO PRETO)
    # =========================
    st.markdown(
        """
        <style>
            html, body, [class*="css"] {
                background-color: #000000;
            }

            .titulo-principal {
                font-size: 34px;
                font-weight: bold;
                color: #B91E27;
                margin-bottom: 10px;
            }

            .subtitulo {
                font-size: 22px;
                font-weight: bold;
                color: #D96569;
                margin-top: 30px;
            }

            .texto {
                font-size: 16px;
                color: #dddddd;
                line-height: 1.6;
            }

            .box {
                background-color: #111111;
                padding: 20px;
                border-radius: 12px;
                margin-top: 15px;
                border: 1px solid #2a2a2a;
            }

            .img-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 12px;
            }

            .content-wrapper {
                max-width: 1100px;
                margin: 0 auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='texto'>
        Resumo prático da Reforma Tributária aplicado a
        <b>empresas prestadoras de serviços</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # CONTEÚDO FIXO
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ CBS em fase piloto<br>
        ✔ Alíquota teste: <b>0,9%</b><br>
        ✔ Compensável com PIS/COFINS<br>
        ❗ Sem aumento real de carga
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # EXCEL NA PÁGINA
    # =========================
    st.markdown("<div class='subtitulo'>📊 Dados – Planilha Excel</div>", unsafe_allow_html=True)

    excel_path = Path("tabela.xlsx")

    if excel_path.exists():
        df = pd.read_excel(excel_path)

        st.markdown(
            "<div class='box texto'>"
            "Abaixo, os dados carregados diretamente do arquivo <b>tabela.xlsx</b>."
            "</div>",
            unsafe_allow_html=True
        )

        st.dataframe(
            df,
            use_container_width=True,
            height=450
        )
    else:
        st.error("⚠️ Arquivo 'tabela.xlsx' não encontrado. Coloque-o na mesma pasta do app.")

    # =========================
    # CONCLUSÃO
    # =========================
    st.markdown("<div class='subtitulo'>🧾 Conclusão Prática</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ Dados do Excel integrados ao painel<br>
        ✔ Visual profissional e seguro<br>
        ✔ Pronto para apresentação a cliente ou diretoria
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
