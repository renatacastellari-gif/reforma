
import streamlit as st
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
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

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
    # Toggle de estilo de fonte (opcional)
    col_a, col_b = st.columns([3, 1])
    with col_b:
        fonte_modo = st.radio(
            "Estilo de fonte",
            options=["Clean (Inter)", "Mono (Consolas)"],
            index=0,
            help="Altere a tipografia para leitura mais limpa ou visual técnico."
        )

    # =========================
    # CSS GLOBAL (FUNDO PRETO + CARDS + TIPOGRAFIA)
    # =========================
    # Carrega Google Fonts para a opção Clean
    # (Se estiver offline, cai nos fallbacks sem quebrar)
    if fonte_modo == "Clean (Inter)":
        st.markdown(
            "<link rel='preconnect' href='https://fonts.googleapis.com'>"
            "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
            "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap' rel='stylesheet'>",
            unsafe_allow_html=True
        )

    # Define famílias de fontes conforme o modo
    body_font = "Inter, Segoe UI, Roboto, Helvetica Neue, Arial, system-ui, -apple-system, sans-serif" \
        if fonte_modo == "Clean (Inter)" else \
        "Consolas, Menlo, Monaco, 'Courier New', monospace"

    heading_font = "Consolas, Menlo, Monaco, 'Courier New', monospace" \
        if fonte_modo == "Clean (Inter)" else \
        "Consolas, Menlo, Monaco, 'Courier New', monospace"

    st.markdown(
        "<style>"
        "html, body, [class*='css']{background-color:#000000;}"
        f"body {{ font-family:{body_font}; }}"
        ".content-wrapper{max-width:1100px;margin:0 auto;}"
        f".titulo-principal{{font-family:{heading_font};font-size:34px;font-weight:800;color:#B91E27;margin-bottom:10px;text-align:left;border-bottom:2px solid #B91E27;padding-bottom:8px;}}"
        ".subtitulo{font-size:22px;font-weight:700;color:#D96569;margin-top:30px;}"
        ".texto{font-size:16px;color:#dddddd;line-height:1.65;}"
        ".card{background-color:#1e1e1e;color:#f0f0f0;padding:26px 28px;border-radius:14px;margin:22px 0;border-left:6px solid #B91E27;box-shadow:0 2px 0 #111111;}"
        f".card h3{{font-family:{heading_font};font-size:28px;font-weight:800;margin:0 0 12px 0;color:#ffffff;letter-spacing:0.2px;}}"
        ".card ul{margin:10px 0 0 18px;padding:0;list-style-type:disc;}"
        ".card li{font-size:17px;line-height:1.7;margin-bottom:6px;color:#e6e6e6;}"
        ".card li b{color:#ffffff;font-weight:700;}"
        ".img-container{display:flex;justify-content:center;align-items:center;margin-top:12px;}"
        ".callout{background:#101010;border:1px dashed #B91E27;border-radius:10px;padding:14px 16px;margin-top:12px;color:#dddddd;font-size:16px;}"
        /* pequenos ajustes de legibilidade */
        ".card p{margin:0;color:#dcdcdc;font-size:16px;line-height:1.65;}"
        "</style>",
        unsafe_allow_html=True
    )

    # Wrapper
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária</div>", unsafe_allow_html=True)

    # =========================
    # CARD: CBS
    # =========================
    st.markdown(
        "<div class='card'>"
        "<h3>CBS – Contribuição sobre Bens e Serviços</h3>"
        "<ul>"
        "<li>Substitui <b>PIS e COFINS</b></li>"
        "<li>Imposto <b>federal</b></li>"
        "<li>Modelo de <b>IVA</b> (não cumulativo)</li>"
        "<li>Permite <b>crédito financeiro</b> amplo</li>"
        "<li>Objetivo: <b>simplificar</b> a tributação</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # CARD: Para Empresa (prestação de serviços)
    # =========================
    st.markdown(
        "<div class='card'>"
        "<h3>Para Empresa (prestação de serviços)</h3>"
        "<ul>"
        "<li><b>Obrigatoriedade de emitir documento fiscal eletrônico:</b><br>"
        "Para qualquer operação com serviços em 2026, a empresa deve emitir <b>NFS-e</b> "
        "(Nota Fiscal de Serviços Eletrônica) — exatamente o que vocês já fazem. "
        "A NFS-e está listada como documento <b>recepcionado</b> pelo <b>IBS</b> e <b>CBS</b>."
        "</li>"
        "<li><b>Campos do IBS e da CBS na NFS-e:</b><br>"
        "No início, <b>não haverá penalidade</b> se vocês ainda não preencherem os novos "
        "campos de IBS/CBS na NFS-e. Isso vale <b>até o primeiro dia do 4º mês</b> após a "
        "publicação dos regulamentos do IBS/CBS (ainda não publicados)."
        "</li>"
        "<li><b>2026 será um ano de apuração “informativa”:</b>"
        "<ul>"
        "<li>A apuração de <b>IBS</b> e <b>CBS</b> <b>não terá efeitos tributários</b> em 2026.</li>"
        "<li>Mas será <b>obrigatório</b> enviar as informações conforme a legislação.</li>"
        "</ul>"
        "</li>"
        "</ul>"
        "<div class='callout'>"
        "Ou seja:<br>"
        "➡️ <b>não paga IBS/CBS em 2026</b>,<br>"
        "➡️ <b>mas precisa transmitir</b> as informações corretamente quando exigido.<br><br>"
        "• Em 2026, precisarão atender <b>obrigações acessórias</b> do IBS/CBS, mas sem recolhimento.<br>"
        "• Os <b>novos campos de IBS/CBS</b> na NFS-e <b>não gerarão multa</b> inicialmente.<br>"
        "• A apuração será <b>somente informativa</b> durante 2026."
        "</div>"
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # CARD: NFS-e — layouts que poderão ser usados em 2026
    # =========================
    st.markdown(
        "<div class='card'>"
        "<h3>NFS-e — layouts que poderão ser usados em 2026</h3>"
        "<p class='texto' style='margin-bottom:10px;'>"
        "Segundo comunicado de <b>15/12/2025</b>, o município permitirá duas modalidades de emissão da NFS-e: "
        "<span style='opacity:0.7;'>[reformatri...utaria.com]</span>"
        "</p>"
        "<ul>"
        "<li><b>Layout 1 (atual)</b>"
        "<ul>"
        "<li>Só contém <b>ISS</b></li>"
        "<li>Não inclui ainda os campos de <b>IBS/CBS</b></li>"
        "<li>Ainda será aceito em 2026 (online, webservice, TXT)</li>"
        "</ul>"
        "</li>"
        "<li><b>Layout 2 (novo)</b>"
        "<ul>"
        "<li>Inclui <b>ISS + IBS + CBS</b></li>"
        "<li><b>Válido a partir de 01/01/2026</b></li>"
        "<li>Se a empresa optar por usar, os campos de IBS/CBS passam a constar na emissão</li>"
        "</ul>"
        "</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # CARDS DE PERÍODO
    # =========================
    st.markdown(
        "<div class='card'>"
        "<h3>2026 — Período de Teste</h3>"
        "<ul>"
        "<li>Entrada da <b>CBS em fase piloto</b></li>"
        "<li>Alíquota teste: <b>0,9%</b></li>"
        "<li>Valor recolhido é <b>compensado</b> com PIS/COFINS</li>"
        "<li>Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias</li>"
        "<li><b>Não há aumento</b> real de carga tributária em 2026</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='card'>"
        "<h3>A partir de 2027</h3>"
        "<ul>"
        "<li><b>PIS e COFINS</b> são extintos</li>"
        "<li>Entra a <b>CBS</b> de forma definitiva</li>"
        "<li>Não cumulativa (modelo <b>IVA</b>)</li>"
        "<li>Crédito financeiro amplo</li>"
        "<li>Alíquota estimada: <b>~8,8%</b></li>"
        "<li>Serviços tendem a <b>aumentar a carga tributária</b></li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # TABELA FINAL (IMAGEM)
    # =========================
    st.markdown("<div class='subtitulo'>🗂️ Tabela – Linha do Tempo</div>", unsafe_allow_html=True)

    img_path = Path("tabela.png")
    if img_path.exists():
        st.markdown("<div class='img-container'>", unsafe_allow_html=True)
        st.image(str(img_path), caption="Linha do Tempo — PIS/COFINS → CBS", width=650)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Arquivo 'tabela.png' não encontrado.")

    st.markdown("</div>", unsafe_allow_html=True)
