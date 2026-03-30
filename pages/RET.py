
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
    # TIPOGRAFIA
    # =========================
    BODY_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"

    # =========================
    # CSS GLOBAL (TEMA ESCURO + TÍTULO + CARDS)
    # =========================
    style_str = f"""
    <style>
        html, body, [class*="css"] {{
            background-color: #1b1b1b; /* mantém seu fundo escuro do app original */
        }}
        body {{
            font-family: {BODY_FONT};
            color: #F9EEEF;
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        .content-wrapper {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 1.2rem; /* respira nas laterais */
        }}

        /* Título exatamente como o seu exemplo */
        .titulo-principal {{
            font-family: {HEADING_FONT};
            font-size: 34px;
            font-weight: 800;
            color: #B91E27;
            margin-bottom: 10px;
            text-align: left;
            border-bottom: 2px solid #B91E27;
            padding-bottom: 8px;
            letter-spacing: 0.2px;
        }}

        /* Inputs e botões mantidos no tema escuro */
        input, textarea {{
            background-color: #2a2a2a !important;
            color: #F9EEEF !important;
            border: 1px solid #EBBFC1 !important;
        }}

        .stButton > button {{
            background-color: #B91E27;
            color: #F9EEEF;
            border-radius: 8px;
            border: none;
            font-weight: 600;
        }}
        .stButton > button:hover {{
            background-color: #8f1620;
            color: #F9EEEF;
        }}

        /* Cards */
        .card {{
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
            color: #f0f0f0;
        }}

        .card h3 {{
            font-family: {HEADING_FONT};
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.2px;
        }}

        .card ul {{
            margin: 10px 0 0 18px;
            padding: 0;
            list-style-type: disc;
        }}

        .card li {{
            font-size: 17px;
            line-height: 1.7;
            margin-bottom: 6px;
            color: #e6e6e6;
        }}

        .card li b {{
            color: #ffffff;
            font-weight: 700;
        }}

        .card p {{
            margin: 0;
            color: #dcdcdc;
            font-size: 16px;
            line-height: 1.65;
        }}

        .highlight {{
            color: #F2D5D7;
            font-weight: 600;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO (EXATO AO SEU ESTILO)
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária | RET</div>", unsafe_allow_html=True)

    # =========================
    # CARDS – IBS
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🟦 O RET (Regime Especial de Tributação)</h3>
            <p>
                O <b>IBS</b> Empreendimentos que optarem pelo RET até 31/12/2028:
Podem continuar no regime atual (alíquota de 4%) até o fim da obra/incorporação.
Depois dessa data:
Novos projetos tendem a entrar já no novo sistema (CBS/IBS) ou em regras adaptadas.

        """,
        unsafe_allow_html=True
    )

   
    st.markdown(
        """
        <div class='card'>
            <h3>Prazos</h3>
            <ul>
                <li>📊 Resumo direto: Depois disso → tende a acabar a entrada no modelo atual</li>
                <li>Até 31/12/2028 → ainda dá pra entrar no RET “antigo”</b></li>
                <li>Quem entrou antes → mantém o RET até concluir o empreendimento</b></li>
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
                <li><b>2033</b>: IBS plenamente vigente, com extinção definitiva do ICMS e ISS</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <h3>⚠️ O que é? </h3>
            <ul>
                <li>O RET (Regime Especial de Tributação) é um regime fiscal simplificado para incorporadoras imobiliárias no Brasil, aplicado sobre o patrimônio de afetação. Ele unifica impostos (IRPJ, CSLL, PIS, Cofins) 
                em uma alíquota única de 4% sobre a receita mensal, reduzindo custos e facilitando obrigações contábeis</li>
                <li>Setores com benefícios fiscais podem perder incentivos</li>
                <li>Estados e Municípios terão adaptação gradual</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)











