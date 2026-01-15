
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
    # CSS GLOBAL (TEMA ESCURO + TÍTULO + CARDS + TABELA)
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

        /* TABELAS HTML */
        .tabela {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 15px;
        }}
        .tabela th, .tabela td {{
            border: 1px solid #3a3a3a;
            padding: 10px 12px;
        }}
        .tabela th {{
            background-color: #303030;
            color: #fff;
            text-align: left;
        }}
        .tabela tr:nth-child(even) td {{
            background-color: #252525;
        }}
        .tabela tr:nth-child(odd) td {{
            background-color: #202020;
        }}
        .tabela tfoot td {{
            font-weight: 800;
            background-color: #2b2b2b;
        }}
        .muted {{
            color: #c9bfc0;
            font-size: 13px;
        }}
        .small-note {{
            font-size: 13px;
            color: #d4c9ca;
        }}
        .fonte-link a {{
            color: #F2D5D7;
            text-decoration: none;
        }}
        .fonte-link a:hover {{
            text-decoration: underline;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD – PRESUNÇÃO (CNAE 6822-6/00)
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🟦 Presunção – CNAE 6822-6/00</h3>
            <p>
                Para <b>prestação de serviços</b> (inclui <b>Gestão e administração da propriedade imobiliária</b>),
                a presunção padrão é de <b>32%</b>. Com o <b>PLP 128/2025</b>, a presunção é majorada em <b>10%</b>
                (ou seja, <b>35,2%</b>) <u>sobre a parcela da receita bruta anual que exceder <b>R$ 5 milhões</b></u>.
            </p>
            <p class="highlight">
              Em resumo: até R$ 5 mi/ano → 32%; acima de R$ 5 mi/ano → 35,2%.
            </p>
            <p class="small-note">
              Adicional de IRPJ: 10% sobre o <b>lucro presumido</b> que exceder <b>R$ 20 mil/mês</b> (R$ 60 mil/trimestre, R$ 240 mil/ano).
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TABELA – ALÍQUOTAS EFETIVAS (COMPARATIVO SIMPLES)
    # =========================
    tabela_html = """
    <div class='card'>
        <h3>📊 Tabela de alíquotas efetivas (base presumida 32% × 35,2%)</h3>
        <table class='tabela'>
            <thead>
                <tr>
                    <th>Tributo</th>
                    <th>Atual (32%)</th>
                    <th>Novo (35,2%)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>IRPJ (15%)</td>
                    <td>4,80%</td>
                    <td>5,28%</td>
                </tr>
                <tr>
                    <td>Adicional IRPJ (10% sobre lucro presumido acima do limite)</td>
                    <td>3,20%</td>
                    <td>3,52%</td>
                </tr>
                <tr>
                    <td>CSLL (9%)</td>
                    <td>2,88%</td>
                    <td>3,17%</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td><b>Total</b></td>
                    <td><b>10,88%</b></td>
                    <td><b>11,97%</b></td>
                </tr>
            </tfoot>
        </table>
        <p class="muted">Observação: estes percentuais refletem a <b>presunção única</b> aplicada sobre <i>toda</i> a receita. No cenário real,
        a regra nova aplica 35,2% <i>apenas</i> ao que exceder R$ 5 mi/ano (ver exemplo prático abaixo).</p>
    </div>
    """
    st.markdown(tabela_html, unsafe_allow_html=True)

    # =========================
    # EXEMPLO PRÁTICO – 2 MILHÕES/MÊS (REGRA MISTA)
    # =========================

    # ---------
    # Funções auxiliares
    # ---------
    def brl(v: float) -> str:
        return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def pct(v: float) -> str:
        return f"{v*100:,.2f}%".replace(",", "X").replace(".", ",").replace("X", ".")

    # ---------
    # Parâmetros do exemplo
    # ---------
    receita_mensal = 2_000_000.00
    receita_anual = receita_mensal * 12

    # Regras de presunção
    presuncao_atual = 0.32
    presuncao_nova_excedente = 0.352
    limite_anual_nova = 5_000_000.00

    # Bases presumidas (anual)
    # Cenário ATUAL: 32% sobre toda a receita
    base_atual_anual = receita_anual * presuncao_atual

    # Cenário NOVO (regra mista): 32% até R$ 5 mi + 35,2% acima de R$ 5 mi
    excedente = max(0.0, receita_anual - limite_anual_nova)
    faixa_base_32 = min(receita_anual, limite_anual_nova) * presuncao_atual
    faixa_base_352 = excedente * presuncao_nova_excedente
    base_nova_anual = faixa_base_32 + faixa_base_352

    # IRPJ (15%) + Adicional do IRPJ (10% sobre base acima de 240 mil/ano)
    adicional_limite_anual = 240_000.00

    irpj15_atual = 0.15 * base_atual_anual
    irpj_add_atual = 0.10 * max(0.0, base_atual_anual - adicional_limite_anual)
    irpj_total_atual = irpj15_atual + irpj_add_atual

    irpj15_novo = 0.15 * base_nova_anual
    irpj_add_novo = 0.10 * max(0.0, base_nova_anual - adicional_limite_anual)
    irpj_total_novo = irpj15_novo + irpj_add_novo

    # CSLL (9%)
    csll_atual = 0.09 * base_atual_anual
    csll_novo = 0.09 * base_nova_anual

    # Totais (anual e mensal)
    total_atual_anual = irpj_total_atual + csll_atual
    total_novo_anual = irpj_total_novo + csll_novo

    total_atual_mensal = total_atual_anual / 12
    total_novo_mensal = total_novo_anual / 12

    # Alíquotas efetivas (sobre a receita)
    aliq_efetiva_atual = total_atual_anual / receita_anual
    aliq_efetiva_nova = total_novo_anual / receita_anual
    delta_pct = aliq_efetiva_nova - aliq_efetiva_atual

    # --------------------------
    # Render do EXEMPLO PRÁTICO
    # --------------------------
    st.markdown(
        f"""
        <div class='card'>
            <h3>🧮 Exemplo prático – empresa que fatura {brl(receita_mensal)} por mês (R$ 24 mi/ano)</h3>
            <p><b>Regra nova (mista):</b> aplica <b>32%</b> sobre os primeiros <b>R$ 5 mi</b> do ano e <b>35,2%</b> sobre o <b>excedente</b> (R$ {excedente:,.0f}).</p>
            <table class="tabela">
                <thead>
                    <tr>
                        <th>Item</th>
                        <th>Cenário Atual</th>
                        <th>Regra Nova (mista)</th>
                        <th>Variação</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>Base presumida anual</b></td>
                        <td>{brl(base_atual_anual)}</td>
                        <td>{brl(base_nova_anual)}</td>
                        <td>{brl(base_nova_anual - base_atual_anual)}</td>
                    </tr>
                    <tr>
                        <td>IRPJ 15%</td>
                        <td>{brl(irpj15_atual)}</td>
                        <td>{brl(irpj15_novo)}</td>
                        <td>{brl(irpj15_novo - irpj15_atual)}</td>
                    </tr>
                    <tr>
                        <td>Adicional IRPJ (10% acima de R$ 240 mil/ano)</td>
                        <td>{brl(irpj_add_atual)}</td>
                        <td>{brl(irpj_add_novo)}</td>
                        <td>{brl(irpj_add_novo - irpj_add_atual)}</td>
                    </tr>
                    <tr>
                        <td>CSLL 9%</td>
                        <td>{brl(csll_atual)}</td>
                        <td>{brl(csll_novo)}</td>
                        <td>{brl(csll_novo - csll_atual)}</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <td><b>Total anual (IRPJ+CSLL)</b></td>
                        <td><b>{brl(total_atual_anual)}</b></td>
                        <td><b>{brl(total_novo_anual)}</b></td>
                        <td><b>{brl(total_novo_anual - total_atual_anual)}</b></td>
                    </tr>
                </tfoot>
            </table>

            <p style="margin-top:12px;">
                <b>Alíquota efetiva sobre a receita anual:</b>
                <span>Atual: <b>{pct(aliq_efetiva_atual)}</b> &nbsp;|&nbsp; Nova (mista): <b>{pct(aliq_efetiva_nova)}</b> &nbsp;|&nbsp; Diferença: <b>{pct(delta_pct)}</b></span>
            </p>

            <p class="small-note">
                <b>Totais mensais aproximados</b> (anual ÷ 12):<br>
                &bull; Atual: <b>{brl(total_atual_mensal)}</b> &nbsp;|&nbsp; Novo: <b>{brl(total_novo_mensal)}</b> &nbsp;|&nbsp; Acréscimo mensal: <b>{brl(total_novo_mensal - total_atual_mensal)}</b>
            </p>

            <p class="muted">
                Observações:
                <br>&bull; A apuração do IRPJ/CSLL é trimestral; aqui usamos equivalência anual para simplificar o comparativo.
                <br>&bull; O adicional do IRPJ considera o limite anual de R$ 240 mil (R$ 20 mil/mês × 12).
                <br>&bull; Este exemplo não inclui PIS/Cofins (ou CBS/IBS), nem receitas financeiras/ganhos de capital.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # FONTES
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>🔗 Fontes</h3>
            <p class="fonte-link">
                • Contábeis – https://www.contabeis.com.br/noticias/74447/plp-128-aumenta-em-10-custos-dos-tributos-do-lucro-presumido/PLP 128 aumenta em 10% os custos do Lucro Presumido</a><br>
                • Agilize – https://artigos.agilize.com.br/reforma-tributaria-lucro-presumido/Reforma tributária 2026 e lucro presumido (guia)</a><br>
                • AmdJus – https://amdjus.com.br/plp-128-2025-o-impacto-indireto-no-aumento-da-carga-tributaria-pelo-lucro-presumido/Impacto indireto do PLP 128/2025 no Lucro Presumido</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)
