
import streamlit as st
# import pandas as pd  # remova se não usar pandas
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
    # CSS GLOBAL (FUNDO PRETO + CARDS)
    # =========================
    st.markdown(
        """
        <style>
            html, body, [class*="css"]  {
                background-color: #000000;
            }

            .content-wrapper {
                max-width: 1100px;
                margin: 0 auto;
            }

            .titulo-principal {
                font-size: 34px;
                font-weight: 800;
                color: #B91E27;
                margin-bottom: 10px;
                text-align: left;
                border-bottom: 2px solid #B91E27;
                padding-bottom: 8px;
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

            /* CARD no estilo do print */
            .card {
                background-color: #1e1e1e;  /* corpo escuro */
                color: #f0f0f0;
                padding: 26px 28px;
                border-radius: 14px;
                margin: 22px 0;
                border-left: 6px solid #B91E27; /* borda vermelha na esquerda */
                box-shadow: 0 2px 0 #111111;
            }

            .card h3 {
                font-size: 30px;
                font-weight: 800;
                margin: 0 0 10px 0;
                color: #ffffff;
            }

            .card ul {
                margin: 12px 0 0 18px;
                padding: 0;
                list-style-type: disc;
            }

            .card li {
                font-size: 17px;
                line-height: 1.65;
                margin-bottom: 6px;
            }

            .card li b {
                color: #ffffff;
                font-weight: 700;
            }

            /* Imagem centralizada */
            .img-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 12px;
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
    st.markdown("<div class='titulo-principal'>Reforma Tributária</div>", unsafe_allow_html=True)

    # =========================
    # CARDS (layout da imagem)
    # =========================

    # Card: CBS
    st.markdown(
        """
        <div class="card">
            <h3>CBS – Contribuição sobre Bens e Serviços</h3>
            <ul>
                <li>Substitui <b>PIS e COFINS</b></li>
                <li>Imposto <b>federal</b></li>
                <li>Modelo de <b>IVA</b></li>
                <li>Permite <b>crédito do imposto</b></li>
                <li>Objetivo: <b>simplificar</b> a tributação</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Card: ISS
    st.markdown(
        """
        <div class="card">
            <h3>ISS – Imposto Sobre Serviços</h3>
            <ul>
                <li>Imposto <b>municipal</b></li>
                <li>Incide sobre <b>prestação de serviços</b></li>
                <li>Será <b>extinto</b> com a reforma</li>
                <li>Substituído pelo <b>IBS</b></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Você pode seguir adicionando outros cards na mesma pegada:
    # IBS, IVA Dual, Períodos (2026 e 2027+), regimes especiais etc.
    st.markdown(
        """
        <div class="card">
            <h3>2026 — Período de Teste</h3>
            <ul>
                <li>Entrada da <b>CBS em fase piloto</b></li>
                <li>Alíquota teste: <b>0,9%</b></li>
                <li>Valor recolhido é <b>compensado</b> com PIS/COFINS</li>
                <li>Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias</li>
                <li><b>Não há aumento</b> real de carga tributária em 2026</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <h3>A partir de 2027</h3>
            <ul>
                <li><b>PIS e COFINS</b> são extintos</li>
                <li>Entra a <b>CBS</b> de forma definitiva</li>
                <li>Não cumulativa (modelo <b>IVA</b>)</li>
                <li>Crédito financeiro amplo</li>
                <li>Alíquota estimada: <b>~8,8%</b></li>
                <li>Serviços tendem a <b>aumentar a carga tributária</b></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

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
