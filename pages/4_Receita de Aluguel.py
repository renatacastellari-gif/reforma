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
        """
        <style>
            [data-testid='stSidebar'] { display: none; }
        </style>
        """,
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
            # Use APENAS UM dos comandos abaixo conforme sua versão do Streamlit:
            # st.experimental_rerun()  # versões mais antigas
            st.rerun()  # versões recentes
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

        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}

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
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária | Locação de Imóveis</div>", unsafe_allow_html=True)

    # =========================
    # CARD COM TEXTO SOBRE LOCAÇÃO DE IMÓVEIS EM 2026
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>✅ Como funciona em 2026 para locação de imóveis</h3>
            <p>
                • Locação de imóveis não é considerada operação com bens ou serviços para fins da CBS (nem IBS), pois é uma obrigação de dar, não de fazer.<br>
                • Portanto, não há incidência da CBS sobre receitas de aluguel.<br>
                • Em 2026, mesmo sendo ano-teste, não será necessário emitir nota fiscal para locação nem destacar CBS, porque a operação continua fora do campo de incidência.
            </p>
            <h3>✅ Procedimento em 2026</h3>
            <p>
                • Nenhum recolhimento de CBS ou IBS sobre locação.<br>
                • Nenhuma obrigação de destacar CBS/IBS em contratos ou recibos de aluguel.<br>
                • Apenas manter a escrituração normal do aluguel como receita, seguindo as regras contábeis e fiscais atuais (IRPJ, CSLL, PIS/Cofins, etc.).<br>
                • CBS e IBS só serão aplicados a operações com bens e serviços tributáveis.
            </p>
            <h3>✅ Emissão de Nota</h3>
            <p>
                • A obrigação de emitir nota fiscal de locação foi criada, porém ainda não é possível fazer a emissão dessas notas fiscais, 
                conforme item 3.a da Nota Técnica 007, recentemente divulgada (07.fev.2026).<br>
                • Portanto, não tem como emitir ainda a Nota Fiscal de Locação de Imóveis, tampouco o 
                Comitê Gestor definiu a data para o início dessa obrigação.<br>
            </p>
            <h3>📌 Resumo prático</h3>
            <p class="highlight">
                Se você administra imóveis ou faz locação, não muda nada em 2026 quanto à CBS/IBS. Não há emissão de nota nem cálculo desses tributos para aluguel.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)
