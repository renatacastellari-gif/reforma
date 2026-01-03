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
            html, body, [class*="css"]  {
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

            .tabela {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            .tabela thead th {
                background-color: #6b1f3a;
                color: #ffffff;
                padding: 10px;
                text-align: center;
            }
            .tabela tbody td {
                background-color: #0f0f0f;
                color: #eaeaea;
                padding: 10px;
                text-align: center;
                border-bottom: 1px solid #333333;
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

    # Wrapper
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='texto'>
        Resumo prático da Reforma Tributária aplicado a
        <b>empresas prestadoras de serviços de consultoria e assessoria patrimonial imobiliária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2026
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ Entrada da <b>CBS em fase piloto</b><br>
        ✔ Alíquota teste: <b>0,9%</b><br>
        ✔ Valor recolhido é <b>compensado com PIS e COFINS</b><br>
        ✔ Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias<br><br>
        ❗ <b>Não há aumento real de carga tributária em 2026</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2027+
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ❌ <b>PIS e COFINS são extintos</b><br>
        ✔ Entra a <b>CBS</b> de forma definitiva<br><br>
        • Não cumulativa (IVA)<br>
        • Crédito financeiro amplo<br>
        • Alíquota estimada: <b>~8,8%</b><br><br>
        ⚠️ Serviços tendem a sentir <b>aumento da carga tributária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # EXCEL – UPLOAD
    # =========================
    st.markdown("<div class='subtitulo'>📂 Simulação com Excel</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='box texto'>Faça upload de um Excel para visualizar os dados no painel.</div>",
        unsafe_allow_html=True
    )

    arquivo = st.file_uploader(
        "Selecione o arquivo Excel",
        type=["xlsx", "xls"]
    )

    if arquivo:
        xls = pd.ExcelFile(arquivo)
        aba = st.selectbox("Escolha a aba", xls.sheet_names)
        df = pd.read_excel(arquivo, sheet_name=aba)

        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # TABELA FINAL (IMAGEM)
    # =========================
    st.markdown("<div class='subtitulo'>🗂️ Tabela – Linha do Tempo</div>", unsafe_allow_html=True)

    img_path = Path("tabela.png")

    if img_path.exists():
        st.markdown("<div class='img-container'>", unsafe_allow_html=True)
        st.image(
            str(img_path),
            caption="Linha do Tempo — PIS/COFINS → CBS",
            width=650
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Arquivo 'tabela.png' não encontrado.")

    st.markdown("</div>", unsafe_allow_html=True)
