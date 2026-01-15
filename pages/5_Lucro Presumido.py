
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
    # CSS GLOBAL COM FONTE
    # =========================
    st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #1b1b1b;
            font-family: Consolas, Menlo, Monaco, 'Courier New', monospace; /* Fonte aplicada */
        }
        body {
            color: #F9EEEF;
        }
        .titulo-principal {
            font-size: 34px; font-weight: 800; color: #B91E27;
            border-bottom: 2px solid #B91E27; padding-bottom: 8px;
        }
        .card {
            background-color: #2a2a2a; padding: 20px; border-radius: 12px;
            margin: 20px 0; border-left: 6px solid #B91E27;
        }
        .card h3 {color: #fff; font-size: 26px; margin-bottom: 14px;}
        .highlight {color: #F2D5D7; font-weight: 600;}
        table {width:100%; border-collapse: collapse; margin-top:10px;}
        th, td {border:1px solid #3a3a3a; padding:10px;}
        th {background:#303030; color:#fff;}
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        tfoot td {font-weight:800; background:#2b2b2b;}
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
            <li>Presunção padrão: <b>32%</b>.</li>
            <li>Com PLP 128/2025: <b>35,2%</b> sobre a parcela que exceder <b>R$ 5 milhões/ano</b>.</li>
            <li>No trimestre, limite proporcional: <b>R$ 1.250.000</b>.</li>
        </ul>
        <p class="highlight">Até R$ 1.250.000 → 32%; excedente → 35,2%.</p>
        <p>Adicional IRPJ: 10% sobre lucro presumido que exceder <b>R$ 60 mil/trimestre</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD COMPARATIVO
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>📊 Comparativo de alíquotas efetivas</h3>
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
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARD EXEMPLO PRÁTICO
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧮 Exemplo prático – cálculo trimestral</h3>
        <p>O cálculo considera cada trimestre isolado, aplicando a regra mista:</p>
        <ul>
            <li><b>Receita trimestral:</b> R$ 2.000.000</li>
            <li><b>Limite proporcional:</b> R$ 1.250.000 (R$ 5 milhões ÷ 4 trimestres)</li>
            <li><b>Cálculo:</b>
                <ul>
                    <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
                    <li>Excedente (R$ 750.000) → 35,2% = <b>R$ 264.000</b></li>
                </ul>
            </li>
            <li><b>Base total:</b> R$ 664.000</li>
        </ul>
        <p>Se fosse <b>R$ 3.000.000</b> no trimestre:</p>
        <ul>
            <li>Até R$ 1.250.000 → 32% = <b>R$ 400.000</b></li>
            <li>Excedente (R$ 1.750.000) → 35,2% = <b>R$ 616.000</b></li>
            <li><b>Base total:</b> R$ 1.016.000</li>
        </ul>
        <p class="highlight">Depois aplica IRPJ (15% + adicional) e CSLL (9%).</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # NOVO CARD: EXEMPLO PRÁTICO 2
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧮 Exemplo prático 2 – cálculo trimestral</h3>
        <p><b>Receita do Trimestre:</b> R$ 3.580.000,00</p>
        <p>(-) Limite: R$ 1.250.000,00</p>
        <p>(=) Excedente: R$ 2.330.000,00</p>
        <hr>
        <p><b>Receita até o limite:</b> R$ 1.250.000,00<br>
        (x) % Presunção: 32%<br>
        (=) Base de Cálculo: <b>R$ 400.000,00</b></p>
        <p><b>Receita após o limite:</b> R$ 2.330.000,00<br>
        (x) % Presunção: 35,2%<br>
        (=) Base de Cálculo: <b>R$ 820.160,00</b></p>
        <hr>
        <p><b>Base de Cálculo Total:</b> R$ 1.220.160,00 (R$ 400.000,00 + R$ 820.160,00)</p>
        <hr>
        <p>(x) Alíquota IRPJ: 15%<br>
        (=) Valor IRPJ: R$ 183.024,00<br>
        (+) Adicional IRPJ: R$ 116.016,00<br>
        (=) <b>IRPJ Total:</b> R$ 299.040,00</p>
        <p>(x) Alíquota CSLL: 9%<br>
        (=) <b>CSLL Total:</b> R$ 109.814,40</p>
    </div>
    """, unsafe_allow_html=True)
