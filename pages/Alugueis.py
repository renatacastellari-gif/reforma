
import streamlit as st
from pathlib import Path

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
            background-color: #1b1b1b;
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
            padding: 0 1.2rem;
        }}

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

        .card p {{
            margin: 0 0 12px 0;
            color: #dcdcdc;
            font-size: 16px;
            line-height: 1.65;
        }}

        .highlight {{
            color: #F2D5D7;
            font-weight: 600;
        }}

        iframe {{
            width: 100%;
            height: 400px;
            border-radius: 12px;
            margin-top: 16px;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária | Aluguéis</div>", unsafe_allow_html=True)

    # =========================
    # CARD COM VÍDEO E TEXTO MELHORADO
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🟦 Pronunciamento CRC</h3>
            <p>
                <b>Resumo:</b> Durante a palestra do CRC sobre a Reforma Tributária, foi abordado um ponto importante:
            </p>
            <p class="highlight">
                Não será necessário contabilizar CBS e IBS em 2026.
            </p>
            <p>
             📌 Artigo que estabelece a incidência da CBS e IBS:  
> Art. 4º — O IBS e a CBS incidem sobre operações onerosas com bens ou com serviços.  
> (Inclui qualquer operação com bem ou serviço realizada pelo contribuinte.) [1]

👉 O texto completo e atualizado está na Lei Complementar nº 214, de 16 de janeiro de 2025. [2]

📘 Trecho no site oficial:  
📄 [Lei Complementar nº 214/2025 — texto integral](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm?utm_source=chatgpt.com)

No Art. 4º, a lei define a regra geral de incidência tributária para os dois novos tributos:

🔹 “O IBS e a CBS incidem sobre operações onerosas com bens ou com serviços.” [1]

Esse artigo é a base legal que substitui a antiga regra de PIS/COFINS e estabelece o novo conceito de tributação por consumo (IVA dual) no Brasil.

👉 Importante: a lei não diz que aluguéis são automaticamente isentos — ela define a regra geral de incidência. 
Os detalhes de isenções, reduções e regimes específicos (como para aluguéis residenciais ou condições de locadores) estão distribuídos 
mais adiante no texto (capítulos e artigos específicos) ou poderão ser regulamentados posteriormente.
            </p>
            <p>
                Para mais detalhes, assista ao vídeo oficial do CRC. O trecho relevante está por volta de <b>1:53:18</b>.
            </p>
            <iframe src="https://www.youtube.com/embed/PL2BatYvbic" frameborder="0" allowfullscreen></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)
