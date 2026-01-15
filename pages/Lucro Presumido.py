
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
    # CSS GLOBAL (TEMA ESCURO + TÍTULO + CARDS + TABELAS)
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] { background-color: #1b1b1b; }
        body { color: #F9EEEF; font-family: Consolas, Menlo, Monaco, 'Courier New', monospace; }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .content-wrapper {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 1.2rem;
        }

        .titulo-principal {
            font-size: 34px;
            font-weight: 800;
            color: #B91E27;
            margin-bottom: 10px;
            text-align: left;
            border-bottom: 2px solid #B91E27;
            padding-bottom: 8px;
            letter-spacing: 0.2px;
        }

        .card {
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
            color: #f0f0f0;
        }

        .card h3 {
            font-size: 26px;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.2px;
        }

        .subtitulo {
            margin-top: 16px;
            font-weight: 700;
            color: #F2D5D7;
        }

        /* TABELAS */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 15px;
        }
        th, td {
            border: 1px solid #3a3a3a;
            padding: 10px 12px;
        }
        th {
            background-color: #303030;
            color: #fff;
            text-align: left;
        }
        tr:nth-child(even) td { background-color: #252525; }
        tr:nth-child(odd)  td { background-color: #202020; }
        tfoot td {
            font-weight: 800;
            background-color: #2b2b2b;
        }

        .muted { color: #c9bfc0; font-size: 13px; }
        .highlight { color: #F2D5D7; font-weight: 600; }
        .list-item { margin-bottom: 6px; }
    </style>
    """, unsafe_allow_html=True)

    # Wrapper para alinhar e controlar largura
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD – COMPARATIVO + DUAS TABELINHAS
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📊 Comparativo de alíquotas efetivas</h3>

        <!-- Tabela principal -->
        <table>
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
                    <td>Adicional IRPJ (10% sobre lucro presumido acima de R$ 60 mil/mês)</td>
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

        <!-- Tabelinha IRPJ -->
        <p class='subtitulo'>Detalhamento IRPJ</p>
        <table>
            <tbody>
                <tr>
                    <td>Presunção (receita bruta anual de até R$ 5 milhões)</td>
                    <td>32%</td>
                </tr>
                <tr>
                    <td>Presunção (parcela da receita bruta anual que exceder R$ 5 milhões)</td>
                    <td>35,2%</td>
                </tr>
                <tr>
                    <td>Alíquota</td>
                    <td>15%</td>
                </tr>
                <tr>
                    <td>Código do DARF</td>
                    <td>2089</td>
                </tr>
            </tbody>
        </table>

        <!-- Tabelinha CSLL -->
        <p class='subtitulo'>Detalhamento CSLL</p>
        <table>
            <tbody>
                <tr>
                    <td>Presunção (receita bruta anual de até R$ 5 milhões)</td>
                    <td>32%</td>
                </tr>
                <tr>
                    <td>Presunção (parcela da receita bruta anual que exceder R$ 5 milhões)</td>
                    <td>35,2%</td>
                </tr>
                <tr>
                    <td>Alíquota</td>
                    <td>9%</td>
                </tr>
                <tr>
                    <td>Código do DARF</td>
                    <td>2372</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – EXEMPLO PRÁTICO (cálculo trimestral)
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧮 Exemplo prático – cálculo trimestral</h3>
        <p>O cálculo considera cada trimestre <b>isoladamente</b> e aplica a regra mista:</p>
        <ul>
            <li><b>Limite proporcional de presunção reduzida por trimestre:</b> R$ 1.250.000 (R$ 5 milhões ÷ 4).</li>
            <li>Até <b>R$ 1.250.000</b> → presunção <b>32%</b> (base de IRPJ/CSLL).</li>
            <li>Excedente do trimestre → presunção <b>35,2%</b>.</li>
            <li><b>IRPJ</b> = 15% sobre a base presumida + adicional de 10% sobre o <i>lucro presumido</i> que exceder <b>R$ 60.000</b> no trimestre.</li>
            <li><b>CSLL</b> = 9% sobre a base presumida.</li>
        </ul>

        <p class="subtitulo">Cenário A — Receita trimestral: <b>R$ 2.000.000</b></p>
        <ul>
            <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
            <li>Excedente (R$ 750.000) → 35,2% = <b>R$ 264.000</b></li>
            <li><b>Base total do trimestre:</b> <b>R$ 664.000</b></li>
            <li>Depois aplica IRPJ (15% + adicional sobre o que exceder R$ 60 mil) e CSLL (9%).</li>
        </ul>

        <p class="subtitulo">Cenário B — Receita trimestral: <b>R$ 3.000.000</b></p>
        <ul>
            <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
            <li>Excedente (R$ 1.750.000) → 35,2% = <b>R$ 616.000</b></li>
            <li><b>Base total do trimestre:</b> <b>R$ 1.016.000</b></li>
            <li>Depois aplica IRPJ (15% + adicional sobre o que exceder R$ 60 mil) e CSLL (9%).</li>
        </ul>

        <p class="muted">
            Observação: este card ilustra apenas a formação da <b>base presumida trimestral</b>.
            A apuração oficial do IRPJ/CSLL é trimestral; adicional do IRPJ incide sobre o lucro presumido que ultrapassar R$ 60 mil no trimestre.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Fecha o wrapper
    st.markdown("</div>", unsafe_allow_html=True)
