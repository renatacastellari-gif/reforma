
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
    # CSS GLOBAL (FUNDO PRETO)
    # =========================
    st.markdown(
        """
        <style>
            html, body, [class*="css"]  {
                background-color: #000000;
            }
            /* Título principal na cor #B91E27 */
            .titulo-principal {
                font-size: 34px;
                font-weight: bold;
                color: #B91E27;
                margin-bottom: 10px;
            }
            /* Subtítulos na cor #D96569 */
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
            .box {
                background-color: #111111;
                padding: 20px;
                border-radius: 12px;
                margin-top: 15px;
                border: 1px solid #2a2a2a;
            }

            /* Tabela comparativa (tema escuro) */
            .tabela {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            .tabela thead th {
                background-color: #6b1f3a; /* vinho */
                color: #ffffff;
                padding: 10px;
                text-align: center;
            }
            .tabela tbody td {
                background-color: #0f0f0f;
                color: #eaeaea;
                padding: 10px;
                text-align: center;
                border-bottom: 1px solid #333333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TÍTULO PRINCIPAL
    # =========================
    st.markdown("<div class='titulo-principal'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='texto'>
        Resumo prático da Reforma Tributária aplicado a
        <b>empresas prestadoras de serviços de consultoria e assessoria patrimonial imobiliária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2026 – PERÍODO DE TESTE
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ Entrada da <b>CBS em fase piloto</b><br>
        ✔ Alíquota teste: <b>0,9%</b><br>
        ✔ Valor recolhido é <b>compensado com PIS e COFINS</b><br>
        ✔ Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias<br><br>
        ❗ <b>Não há aumento real de carga tributária em 2026</b>.  
        O objetivo é apenas informativo e de adaptação dos sistemas.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2027 EM DIANTE
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ❌ <b>PIS e COFINS são extintos</b><br>
        ✔ Entra a <b>CBS</b> de forma definitiva<br><br>

        <b>Características da CBS:</b><br>
        • Não cumulativa (modelo IVA)<br>
        • Crédito financeiro amplo<br>
        • Alíquota estimada: <b>~8,8%</b><br><br>

        ⚠️ Empresas de serviços com poucos insumos
        tendem a sentir <b>aumento real da carga tributária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TABELA COMPARATIVA (GERAL)
    # =========================
    st.markdown("<div class='subtitulo'>📊 Comparativo Geral</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <table class="tabela">
            <thead>
                <tr>
                    <th>Período</th>
                    <th>Tributo</th>
                    <th>Alíquota</th>
                    <th>Crédito</th>
                    <th>Impacto Financeiro</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Até 2025</td>
                    <td>PIS + COFINS</td>
                    <td>3,65%</td>
                    <td>Não</td>
                    <td>Baixo</td>
                </tr>
                <tr>
                    <td>2026</td>
                    <td>CBS (teste)</td>
                    <td>0,9%</td>
                    <td>Sim (compensado)</td>
                    <td>Neutro</td>
                </tr>
                <tr>
                    <td>2027+</td>
                    <td>CBS definitiva</td>
                    <td>~8,8%</td>
                    <td>Sim (pleno)</td>
                    <td>Mais elevado</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # CONCLUSÃO
    # =========================
    st.markdown("<div class='subtitulo'>🧾 Conclusão Prática</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ 2026 é um ano de adaptação<br>
        ✔ A mudança financeira começa em 2027<br>
        ✔ Revisão de preços e contratos será essencial para serviços
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # TABELA FINAL — IDÊNTICA AO PRINT (3 BLOCOS NA CBS + PIS MESCLADO 2027–2033)
    # ==========================================================
    st.markdown("<div class='subtitulo'>🗂️ Tabela – Linha do Tempo</div>", unsafe_allow_html=True)

    html_tabela_print = """
    <style>
        .print-table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, Helvetica, sans-serif;
            background: #ffffff;
            margin-top: 6px;
        }
        .print-table th, .print-table td {
            border: 1px solid #d6d6d6;
            color: #222;
            padding: 12px 10px;
            text-align: left;
            vertical-align: middle;
            background: #fff;
        }
        .print-table thead th {
            background: #cfe0f1; /* cabeçalho azul claro conforme print */
            color: #1f2a37;
            font-weight: 700;
            text-align: center;
        }
        .center { text-align: center; }
        .muted  { color: #3b3b3b; }

        /* Larguras aproximadas para o visual do print */
        .col-ano   { width: 10%; }
        .col-pis   { width: 22%; }
        .col-cofins{ width: 22%; }
        .col-cbs   { width: 46%; }

        /* Altura das linhas para proporção semelhante ao print */
        .row { height: 56px; }
    </style>

    <table class="print-table">
        <thead>
            <tr>
                <th class="col-ano">Ano</th>
                <th colspan="2">Tributos Atuais</th>
                <th>Novos Tributos</th>
            </tr>
            <tr>
                <th></th>
                <th class="col-pis center">PIS/PASEP</th>
                <th class="col-cofins center">COFINS</th>
                <th class="col-cbs center">CBS</th>
            </tr>
        </thead>
        <tbody>
            <!-- 2024 -->
            <tr class="row">
                <td class="center">2024</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>

            <!-- 2025 -->
            <tr class="row">
                <td class="center">2025</td>
                <td></td>
                <td class="center muted">Sem mudanças</td>
                <td class="center">-</td>
            </tr>

            <!-- 2026 -->
            <tr class="row">
                <td class="center">2026</td>
                <td></td>
                <td class="muted">
                    Alíquotas mantidas; com a possibilidade de compensação de 1% dos novos tributos (CBS 0,9% e IBS 0,1%).
                </td>
                <td class="muted center">Alíquota teste: 0,9%</td>
            </tr>

            <!-- 2027 (início dos blocos) -->
            <tr class="row">
                <td class="center">2027</td>

                <!-- BLOCO PIS/PASEP: grande, 2027–2033 -->
                <td rowspan="7"></td>

                <!-- COFINS -->
                <td></td>

                <!-- BLOCO CBS #1: 2027–2028 com texto -->
                <td class="muted center" rowspan="2">Alíquota estabelecida (-) 0,1%</td>
            </tr>

            <!-- 2028 (continua bloco CBS #1) -->
            <tr class="row">
                <td class="center">2028</td>
                <td></td>
            </tr>

            <!-- 2029 (abre bloco CBS #2: 2029–2030 vazio) -->
            <tr class="row">
                <td class="center">2029</td>
                <td></td>
                <td rowspan="2"></td>
            </tr>

            <!-- 2030 (COFINS com Extinção; continua CBS #2 vazio) -->
            <tr class="row">
                <td class="center">2030</td>
                <td class="center muted">Extinção</td>
                <!-- CBS mesclado acima (vazio) -->
            </tr>

            <!-- 2031 (abre bloco CBS #3: 2031–2033 com texto) -->
            <tr class="row">
                <td class="center">2031</td>
                <td></td>
                <td class="muted center" rowspan="3">Alíquota estabelecida</td>
            </tr>

            <!-- 2032 (continua CBS #3) -->
            <tr class="row">
                <td class="center">2032</td>
                <td></td>
            </tr>

            <!-- 2033 (continua CBS #3) -->
            <tr class="row">
                <td class="center">2033</td>
                <td></td>
            </tr>
        </tbody>
    </table>
    """

    # Renderiza HTML puro — garante rowspan/colspan e CSS sem interferência do Markdown
    components.html(html_tabela_print, height=780, scrolling=True)
