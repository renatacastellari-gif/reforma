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
# LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
    <style>
    [data-testid='stSidebar']{display:none;}
    </style>
    """, unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado!")
            try:
                st.rerun()
            except:
                st.experimental_rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO
# =========================
else:

    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

html, body {background-color:#1b1b1b;}
body {color:#F9EEEF;}

.content-wrapper {
max-width:1100px;
margin:auto;
padding:10px;
}

.titulo {
font-family:'JetBrains Mono', monospace;
font-size:38px;
color:#B91E27;
margin-bottom:20px;
}

.card {
background:#2a2a2a;
padding:24px;
border-radius:12px;
margin-bottom:20px;
border-left:6px solid #B91E27;
font-family:'Montserrat';
line-height:1.7;
}

.highlight {
color:#F2D5D7;
font-weight:600;
}
</style>
""", unsafe_allow_html=True)

    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # TÍTULO
    st.markdown("<div class='titulo'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # CARD SIMPLES
    st.markdown("""
<div class='card'>
<h3>📌 Presunção</h3>
<ul>
<li>Presunção padrão: <b>32%</b></li>
<li>Nova regra: <b>35,2%</b> acima de R$ 5 milhões/ano</li>
</ul>
</div>
""", unsafe_allow_html=True)

    # =========================
    # CARD CORRIGIDO (SEU PROBLEMA)
    # =========================
    st.markdown("""
<div class='card'>
<h4>Nova regra só se aplica a CSLL no 2º trimestre de 2026.</h4>

<p><b>Nota ECONET:</b></p>

<ul>
<li>
A partir de <b>01/04/2026</b>, será aplicado um acréscimo de <b>10%</b>
nos percentuais de presunção sobre a receita bruta, se esta exceder
<b>R$ 5.000.000,00 no ano-calendário</b>.
</li>

<li>
Esse limite será proporcionalizado por trimestre:
<b>R$ 1.250.000,00 por trimestre</b>.
</li>

<li>
No ano-calendário de <b>2026</b>, o limite proporcional será de
<b>R$ 3.750.000,00</b>, pois a regra passa a valer
<b>a partir do 2º trimestre para a CSLL</b>.
</li>
</ul>

<p class="highlight">
Base legal: LC 224/2025 e IN RFB 2.305/2025 (alterada pela IN RFB 2.306/2026).
</p>
</div>
""", unsafe_allow_html=True)

    # VÍDEO
    video_id = "lCdcBlPqBxk"
    components.iframe(
        src=f"https://www.youtube.com/embed/{video_id}",
        height=420
    )

    st.markdown("</div>", unsafe_allow_html=True)
