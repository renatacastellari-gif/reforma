import streamlit as st
from pathlib import Path
# import pandas as pd  # remova se não usar

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Reforma Tributária",
    page_icon="🟥",
    layout="centered"
)

# =========================
# CSS - TEMA ESCURO + PALETA
# =========================
st.markdown(
    """
    <style>
    /* Fundo geral */
    .stApp {
        background-color: #1b1b1b;
        color: #F9EEEF;
    }

    /* Esconder menu e rodapé */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Títulos */
    h1, h2, h3, h4 {
        color: #B91E27;
    }

    /* Caixa de texto e inputs */
    input, textarea {
        background-color: #2a2a2a !important;
        color: #F9EEEF !important;
        border: 1px solid #EBBFC1 !important;
    }

    /* Botões */
    .stButton > button {
        background-color: #B91E27;
        color: #F9EEEF;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #8f1620;
        color: #F9EEEF;
    }

    /* Cards */
    .card {
        background-color: #2a2a2a;
        padding: 18px;
        border-radius: 12px;
        border-left: 6px solid #B91E27;
        margin-bottom: 16px;
    }

    /* Destaque */
    .highlight {
        color: #F2D5D7;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral se não estiver logado
if not st.session_state.logged_in:
    st.markdown(
        "<style>[data-testid='stSidebar']{display:none;}</style>",
        unsafe_allow_html=True
    )

# =========================
# TELA DE LOGIN
# =========================
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

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:


    # =========================

    # TÍTULO

    # =========================
    
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária</div>", unsafe_allow_html=True)

  

    # =========================
    # CARDS – IBS
    # =========================

    st.markdown(
        """
        <div class='card'>
            <h3>🟦 IBS – Imposto sobre Bens e Serviços</h3>
            <p>
                O <b>IBS</b> é o tributo criado pela Reforma Tributária para substituir
                os impostos sobre o consumo.
            </p>
            <p class="highlight">
                Acaba a divisão entre imposto estadual e municipal
                sobre bens e serviços.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>📌 Quais impostos o IBS substitui?</h3>
            <ul>
                <li><b>ICMS</b> (estadual)</li>
                <li><b>ISS</b> (municipal)</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>💳 Créditos do IBS</h3>
            <ul>
                <li>
                    Gera crédito em praticamente todas as aquisições
                    ligadas à atividade econômica
                </li>
                <li>
                    Crédito <b>integral</b> e <b>não cumulativo</b>
                </li>
                <li>
                    Reduz o efeito de <b>“imposto sobre imposto”</b>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>🧾 Exemplos de crédito de IBS para prestador de serviços</h3>
            <ul>
                <li>Aluguel</li>
                <li>Energia elétrica</li>
                <li>Internet e telefonia</li>
                <li>Softwares e licenças</li>
                <li>Serviços de terceiros</li>
                <li>Equipamentos e bens do ativo imobilizado</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>⏳ Quando entra em vigor?</h3>
            <ul>
                <li><b>2026 a 2032</b>: fase de transição</li>
                <li>
                    <b>2033</b>: IBS plenamente vigente,
                    com extinção definitiva do ICMS e ISS
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>⚠️ Pontos de atenção</h3>
            <ul>
                <li>Alíquotas ainda dependem de regulamentação</li>
                <li>Setores com benefícios fiscais podem perder incentivos</li>
                <li>Estados e Municípios terão adaptação gradual</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
