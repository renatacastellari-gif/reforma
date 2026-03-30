import streamlit as st
import streamlit.components.v1 as components

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

# Esconde sidebar até logar
if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
            [data-testid='stSidebar']{display:none;}
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
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');

        html, body, [class*="css"] { background-color: #1b1b1b; }
        body { color: #F9EEEF; font-family: 'Open Sans', Arial, sans-serif; }

        .content-wrapper {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 12px;
        }

        .titulo-principal {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 38px;
            font-weight: 800;
            color: #B91E27;
            margin: 0 0 12px 0;
        }

        .card {
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            color: #f0f0f0;
            font-family: 'Montserrat', sans-serif;
            font-size: 18px;
            line-height: 1.8;
        }

        .highlight {
            color: #F2D5D7;
            font-weight: 600;
        }

        table { width:100%; border-collapse: collapse; margin-top:10px; }
        th, td { border:1px solid #3a3a3a; padding:12px; }
        th { background:#303030; color:#fff; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # TÍTULO
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # SEUS CARDS (mantidos)
    # =========================

    st.markdown("""
    <div class='card'>
        <h3>📌 Presunção – CNAE 6822-6/00</h3>
        <p>Para <b>prestação de serviços</b>:</p>
        <ul>
            <li>Presunção padrão: <b>32%</b></li>
            <li>Nova: <b>35,2%</b> acima de R$ 5 milhões</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 🔥 CARD FINAL FUNCIONANDO
    # =========================
    components.html("""
    <div style="background:#2a2a2a;padding:26px;border-radius:14px;border-left:6px solid #B91E27;color:#f0f0f0;font-family:Montserrat;font-size:18px;line-height:1.8;">
        <h4>Nova regra só se aplica a CSLL no 2º trimestre de 2026.</h4>

        <p><b>Nota ECONET:</b> A partir de 01.04.2026, será aplicado um acréscimo de 10% nos percentuais de presunção sobre receita bruta, se esta exceder R$ 5 milhões no ano-calendário. Esse limite será proporcionalizado por trimestre, ou seja, será de R$ 1.250.000,00 por trimestre. No ano-calendário de 2026, o limite anual proporcional aplicável corresponderá a R$ 3.750.000,00, pois o acréscimo será aplicado a partir do segundo trimestre para a CSLL.</p>

        <p style="color:#F2D5D7;font-weight:600;">
        (artigo 4°, § 5°, da Lei Complementar n° 224/2025; artigo 15, §§ 1°, 2° e 9°, da IN RFB n° 2.305/2025, alterado pelo artigo 1° da IN RFB n° 2.306/2026)
        </p>
    </div>
    """, height=260)

    # =========================
    # VÍDEO (mantido)
    # =========================
    video_id = "lCdcBlPqBxk"
    components.iframe(
        src=f"https://www.youtube.com/embed/{video_id}",
        height=420
    )

    st.markdown("</div>", unsafe_allow_html=True)
