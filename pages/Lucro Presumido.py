
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

if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

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
else:
    # =========================
    # CSS GLOBAL
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {background-color: #1b1b1b;}
        body {color: #F9EEEF; font-family: Consolas, monospace;}

        .titulo-principal {
            font-size: 34px; font-weight: 800; color: #B91E27;
            border-bottom: 2px solid #B91E27; padding-bottom: 8px;
        }

        .card {
            background-color: #2a2a2a; padding: 20px; border-radius: 12px;
            margin: 20px 0; border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
        }
        .card h3 {color: #fff; font-size: 26px; margin-bottom: 14px; display:flex; align-items:center; gap:10px;}

        .highlight {color: #F2D5D7; font-weight: 600;}
        .list-item {margin-bottom:6px;}

        /* Tabela principal do comparativo */
        table {width:100%; border-collapse: collapse; margin-top:10px;}
        th, td {border:1px solid #3a3a3a; padding:10px 12px;}
        th {background:#303030; color:#fff; text-align:left;}
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        tfoot td {font-weight:800; background:#2b2b2b;}

        /* Cartões “tabelinha” (sem <table>) */
        .spec-wrap { display: grid; grid-template-columns: 1fr; gap: 12px; margin-top: 16px; }
        @media (min-width: 820px) {
            .spec-wrap { grid-template-columns: 1fr 1fr; }
        }
        .spec-card {
            background: #222; border:1px solid #3a3a3a; border-radius: 12px; padding: 14px 16px;
        }
        .spec-card h4 { margin: 0 0 10px 0; font-size: 16px; font-weight: 800; color:#F2D5D7; }
        .kv { display:grid; grid-template-columns: 1.2fr 1fr; gap:10px; padding:8px 0; border-bottom:1px dashed #3a3a3a; }
        .kv:last-child { border-bottom:none; }
        .k { color:#cfcfcf; }
        .v { color:#ffffff; font-weight:700; }
        .badge { display:inline-block; padding: 3px 8px; border-radius: 8px; background:#373737; color:#fff; font-size:12px; margin-left:8px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='titulo-principal'>Lucro Presumido | Alteração</div>", unsafe_allow_html=True)

    # =========================
    # CARD PRESUNÇÃO
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📌 Presunção – CNAE 6822-6/00</h3>
        <p>Para <b>prestação de serviços</b> (inclui Gestão e administração da propriedade imobiliária):</p>
        <ul>
            <li class='list-item'>Presunção padrão: <b>32%</b>.</li>
            <li class='list-item'>Com PLP 128/2025: <b>35,2%</b> sobre a parcela que exceder <b>R$ 5 milhões/ano</b>.</li>
            <li class='list-item'>No trimestre, limite proporcional: <b>R$ 1.250.000</b>.</li>
        </ul>
        <p class="highlight">Até R$ 1.250.000 → 32%; excedente → 35,2%.</p>
        <p>Adicional IRPJ: 10% sobre lucro presumido que exceder <b>R$ 60 mil/trimestre</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD – COMPARATIVO + “tabelinhas” (sem <table> nas tabelinhas)
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📊 Comparativo de alíquotas efetivas</h3>

        <!-- Tabela principal (mantida como <table> igual à sua imagem) -->
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

        <!-- As DUAS “tabelinhas” das imagens, mas em cartões (sem <table>) -->
        <div class="spec-wrap">
            <div class="spec-card">
                <h4>Detalhamento IRPJ <span class="badge">DARF 2089</span></h4>
                <div class="kv"><div class="k">Presunção (receita bruta anual de até R$ 5 milhões)</div><div class="v">32%</div></div>
                <div class="kv"><div class="k">Presunção (parcela da receita bruta anual que excedeu R$ 5 milhões)</div><div class="v">35,2%</div></div>
                <div class="kv"><div class="k">Alíquota</div><div class="v">15%</div></div>
            </div>

            <div class="spec-card">
                <h4>Detalhamento CSLL <span class="badge">DARF 2372</span></h4>
                <div class="kv"><div class="k">Presunção (receita bruta anual de até R$ 5 milhões)</div><div class="v">32%</div></div>
                <div class="kv"><div class="k">Presunção (parcela da receita bruta anual que excedeu R$ 5 milhões)</div><div class="v">35,2%</div></div>
                <div class="kv"><div class="k">Alíquota</div><div class="v">9%</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # EXEMPLO PRÁTICO – CÁLCULO TRIMESTRAL (como estava)
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧮 Exemplo prático – cálculo trimestral</h3>
        <p>O cálculo considera cada trimestre isolado, aplicando a regra mista:</p>
        <ul>
            <li><b>Receita trimestral:</b> R$ 2.000.000</li>
            <li><b>Limite proporcional do adicional:</b> R$ 1.250.000 (porque R$ 5 milhões ÷ 4 trimestres)</li>
            <li><b>Cálculo:</b>
                <ul>
                    <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
                    <li>Excedente (R$ 750.000) → 35,2% = <b>R$ 264.000</b></li>
                </ul>
            </li>
            <li><b>Base total:</b> R$ 664.000</li>
        </ul>
        <p>Se fosse <b>R$ 3.000.000</b> no trimestre, ficaria assim:</p>
        <ul>
            <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
            <li>Excedente (R$ 1.750.000) → 35,2% = <b>R$ 616.000</b></li>
            <li><b>Base total:</b> R$ 1.016.000</li>
        </ul>
        <p class='highlight'>Depois aplica IRPJ (15% + adicional sobre excedente) e CSLL (9%).</p>
    </div>
    """, unsafe_allow_html=True)
