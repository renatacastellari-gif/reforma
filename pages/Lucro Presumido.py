
import streamlit as st

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
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

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
    # CSS GLOBAL (TEMA ESCURO + LAYOUT + CARDS)
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] { background-color: #1b1b1b; }
        body { color: #F9EEEF; font-family: Consolas, Menlo, Monaco, 'Courier New', monospace; }

        #MainMenu, footer { visibility: hidden; }

        .content-wrapper { max-width: 1100px; margin: 0 auto; padding: 0 1.2rem; }

        .titulo-principal {
            font-size: 34px; font-weight: 800; color: #B91E27; margin-bottom: 10px;
            text-align: left; border-bottom: 2px solid #B91E27; padding-bottom: 8px; letter-spacing: 0.2px;
        }

        .card {
            background-color: #2a2a2a; padding: 26px 28px; border-radius: 14px; margin: 22px 0;
            border-left: 6px solid #B91E27; box-shadow: 0 2px 0 #111111; color: #f0f0f0;
        }
        .card h3 {
            font-size: 26px; font-weight: 800; margin: 0 0 16px 0; color: #ffffff; letter-spacing: 0.2px;
            display: flex; align-items: center; gap: 10px;
        }

        /* BLOCO DE COMPARAÇÃO (sem tabela) */
        .grid-3 {
            display: grid;
            grid-template-columns: 2.2fr 1fr 1fr;
            gap: 0px;
            border: 1px solid #3a3a3a;
            border-radius: 10px;
            overflow: hidden;
        }
        .grid-3 .row {
            display: contents;
        }
        .grid-3 .cell {
            padding: 12px 14px;
            border-bottom: 1px solid #3a3a3a;
        }
        .grid-3 .head {
            background: #303030; font-weight: 800; color: #fff;
        }
        .grid-3 .label { color: #eaeaea; }
        .grid-3 .val  { color: #f5f5f5; }
        .grid-3 .total { font-weight: 800; background: #2b2b2b; }

        /* “Tabelinhas” como cartões de especificação (sem <table>) */
        .spec-cards {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
            margin-top: 16px;
        }
        @media (min-width: 820px) {
            .spec-cards { grid-template-columns: 1fr 1fr; }
        }
        .spec {
            border: 1px solid #3a3a3a; border-radius: 12px; padding: 14px 16px; background: #222;
        }
        .spec h4 {
            margin: 0 0 8px 0; font-size: 16px; font-weight: 800; color: #F2D5D7; letter-spacing: .2px;
        }
        .kv {
            display: grid; grid-template-columns: 1.2fr 1fr; gap: 8px; padding: 8px 0; border-bottom: 1px dashed #3a3a3a;
        }
        .kv:last-child { border-bottom: none; }
        .k  { color: #cfcfcf; }
        .v  { color: #ffffff; font-weight: 700; }

        .muted { color: #c9bfc0; font-size: 13px; }
        .highlight { color: #F2D5D7; font-weight: 700; }
        .bullet ul { margin: 8px 0 0 18px; }
        .badge {
            display:inline-block; padding: 4px 8px; border-radius: 8px; background:#373737; color:#fff; font-size:12px; margin-left:8px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Wrapper
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD – COMPARATIVO (sem tabela) + “duas tabelinhas” em cards
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📊 Comparativo de alíquotas efetivas</h3>

        <!-- Quadro comparativo em grid -->
        <div class="grid-3" role="table" aria-label="Comparativo de alíquotas">
            <div class="row">
                <div class="cell head">Tributo</div>
                <div class="cell head">Atual (32%)</div>
                <div class="cell head">Novo (35,2%)</div>
            </div>

            <div class="row">
                <div class="cell label">IRPJ (15%)</div>
                <div class="cell val">4,80%</div>
                <div class="cell val">5,28%</div>
            </div>
            <div class="row">
                <div class="cell label">Adicional IRPJ (10% sobre lucro presumido acima de R$ 60 mil/mês)</div>
                <div class="cell val">3,20%</div>
                <div class="cell val">3,52%</div>
            </div>
            <div class="row">
                <div class="cell label">CSLL (9%)</div>
                <div class="cell val">2,88%</div>
                <div class="cell val">3,17%</div>
            </div>

            <div class="row">
                <div class="cell total">Total</div>
                <div class="cell total">10,88%</div>
                <div class="cell total">11,97%</div>
            </div>
        </div>

        <!-- DUAS “TABELINHAS” sem <table>: cartões de especificações -->
        <div class="spec-cards">
            <div class="spec">
                <h4>Detalhamento IRPJ <span class="badge">DARF 2089</span></h4>
                <div class="kv"><div class="k">Presunção – até R$ 5 milhões (ano)</div><div class="v">32%</div></div>
                <div class="kv"><div class="k">Presunção – excedente &gt; R$ 5 milhões (ano)</div><div class="v">35,2%</div></div>
                <div class="kv"><div class="k">Alíquota do IRPJ</div><div class="v">15%</div></div>
            </div>

            <div class="spec">
                <h4>Detalhamento CSLL <span class="badge">DARF 2372</span></h4>
                <div class="kv"><div class="k">Presunção – até R$ 5 milhões (ano)</div><div class="v">32%</div></div>
                <div class="kv"><div class="k">Presunção – excedente &gt; R$ 5 milhões (ano)</div><div class="v">35,2%</div></div>
                <div class="kv"><div class="k">Alíquota da CSLL</div><div class="v">9%</div></div>
            </div>
        </div>

        <p class="muted" style="margin-top:10px;">
            Observação: os percentuais acima expressam a alíquota efetiva sobre a receita, considerando a base de presunção.
            O adicional do IRPJ é 10% sobre o <i>lucro presumido</i> que exceder o limite legal de referência.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – EXEMPLO PRÁTICO (cálculo trimestral)
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧮 Exemplo prático – cálculo trimestral</h3>

        <div class="bullet">
            <p>O cálculo considera cada trimestre <b>isoladamente</b> e aplica a regra mista:</p>
            <ul>
                <li><b>Limite proporcional por trimestre:</b> R$ 1.250.000 (R$ 5 milhões ÷ 4).</li>
                <li>Até <b>R$ 1.250.000</b> → presunção <b>32%</b>.</li>
                <li>Excedente do trimestre → presunção <b>35,2%</b>.</li>
                <li><b>IRPJ</b> = 15% sobre a base presumida + adicional de 10% sobre o <i>lucro presumido</i> que exceder <b>R$ 60.000</b> no trimestre.</li>
                <li><b>CSLL</b> = 9% sobre a base presumida.</li>
            </ul>
        </div>

        <div class="spec" style="margin-top:12px;">
            <h4>📌 Cenário A — Receita trimestral: R$ 2.000.000</h4>
            <div class="kv"><div class="k">Faixa até R$ 1.250.000 (32%)</div><div class="v">R$ 400.000</div></div>
            <div class="kv"><div class="k">Excedente R$ 750.000 (35,2%)</div><div class="v">R$ 264.000</div></div>
            <div class="kv"><div class="k">Base total do trimestre</div><div class="v">R$ 664.000</div></div>
            <p class="muted">Depois aplica: IRPJ 15% + adicional (excesso sobre R$ 60 mil) e CSLL 9%.</p>
        </div>

        <div class="spec" style="margin-top:12px;">
            <h4>📌 Cenário B — Receita trimestral: R$ 3.000.000</h4>
            <div class="kv"><div class="k">Faixa até R$ 1.250.000 (32%)</div><div class="v">R$ 400.000</div></div>
            <div class="kv"><div class="k">Excedente R$ 1.750.000 (35,2%)</div><div class="v">R$ 616.000</div></div>
            <div class="kv"><div class="k">Base total do trimestre</div><div class="v">R$ 1.016.000</div></div>
            <p class="muted">Depois aplica: IRPJ 15% + adicional (excesso sobre R$ 60 mil) e CSLL 9%.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)

