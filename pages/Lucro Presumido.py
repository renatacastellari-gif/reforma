
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
        }
        .card h3 {color: #fff; font-size: 26px; margin-bottom: 10px;}
        .highlight {color: #F2D5D7; font-weight: 600;}
        table {width:100%; border-collapse: collapse; margin-top:10px;}
        th, td {border:1px solid #3a3a3a; padding:8px;}
        th {background:#303030; color:#fff;}
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
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
    # FUNÇÕES AUXILIARES
    # =========================
    def brl(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    def pct(v): return f"{v*100:.2f}%"

    # =========================
    # EXEMPLO PRÁTICO TRIMESTRAL
    # =========================
    def calcula_trimestre(receita):
        limite = 1_250_000
        presuncao_32 = min(receita, limite) * 0.32
        presuncao_352 = max(0, receita - limite) * 0.352
        base = presuncao_32 + presuncao_352
        irpj15 = base * 0.15
        adicional = max(0, base - 60_000) * 0.10
        csll = base * 0.09
        total = irpj15 + adicional + csll
        return {
            "receita": receita, "base": base,
            "irpj15": irpj15, "adicional": adicional,
            "csll": csll, "total": total,
            "aliq": total / receita
        }

    exemplo1 = calcula_trimestre(2_000_000)
    exemplo2 = calcula_trimestre(3_000_000)

    st.markdown("<div class='card'><h3>🧮 Exemplo prático – cálculo trimestral</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p>O cálculo considera cada trimestre isolado:</p>
    <ul>
        <li>Até R$ 1.250.000 → presunção 32%.</li>
        <li>Excedente → presunção 35,2%.</li>
        <li>IRPJ = 15% + adicional sobre lucro presumido acima de R$ 60 mil/trimestre.</li>
        <li>CSLL = 9% sobre base presumida.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Tabela com dois exemplos
    st.markdown(f"""
    <table>
        <thead>
            <tr>
                <th>Item</th>
                <th>R$ 2.000.000</th>
                <th>R$ 3.000.000</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Base presumida</td><td>{brl(exemplo1['base'])}</td><td>{brl(exemplo2['base'])}</td></tr>
            <tr><td>IRPJ (15%)</td><td>{brl(exemplo1['irpj15'])}</td><td>{brl(exemplo2['irpj15'])}</td></tr>
            <tr><td>Adicional IRPJ</td><td>{brl(exemplo1['adicional'])}</td><td>{brl(exemplo2['adicional'])}</td></tr>
            <tr><td>CSLL (9%)</td><td>{brl(exemplo1['csll'])}</td><td>{brl(exemplo2['csll'])}</td></tr>
        </tbody>
        <tfoot>
            <tr><td><b>Total tributos</b></td><td><b>{brl(exemplo1['total'])}</b></td><td><b>{brl(exemplo2['total'])}</b></td></tr>
            <tr><td>Alíquota efetiva</td><td>{pct(exemplo1['aliq'])}</td><td>{pct(exemplo2['aliq'])}</td></tr>
        </tfoot>
    </table>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
