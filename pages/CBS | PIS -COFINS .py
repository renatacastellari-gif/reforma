# =========================
# CSS – MESMO LAYOUT DA PRIMEIRA PÁGINA
# =========================
st.markdown(
    """
    <style>
        html, body, [class*="css"] {
            background-color: #000000;
        }

        .content-wrapper {
            max-width: 1100px;
            margin: 0 auto;
        }

        .titulo-principal {
            font-size: 32px;
            font-weight: bold;
            color: #B91E27;
            margin-bottom: 8px;
        }

        .subtitulo {
            font-size: 22px;
            font-weight: bold;
            color: #EBBFC1;
            margin-top: 35px;
        }

        .texto {
            font-size: 16px;
            color: #e0e0e0;
            line-height: 1.6;
        }

        .card {
            background-color: #111111;
            padding: 22px;
            border-radius: 14px;
            margin-top: 16px;
            border-left: 5px solid #B91E27;
            box-shadow: 0 0 12px rgba(185,30,39,0.15);
        }

        .highlight {
            color: #F2D5D7;
            font-weight: bold;
        }

        .tabela {
            width: 100%;
            border-collapse: collapse;
            margin-top: 18px;
        }

        .tabela th {
            background-color: #6b1f3a;
            color: white;
            padding: 10px;
            text-align: center;
        }

        .tabela td {
            background-color: #0f0f0f;
            color: #eaeaea;
            padding: 10px;
            text-align: center;
            border-bottom: 1px solid #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

# =========================
# TÍTULO
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
    <div class='card texto'>
    ✔ Entrada da <b>CBS em fase piloto</b><br>
    ✔ Alíquota teste: <span class='highlight'>0,9%</span><br>
    ✔ Valor recolhido é <b>compensado com PIS e COFINS</b><br>
    ✔ Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias<br><br>
    ❗ <b>Não há aumento real de carga tributária em 2026</b>.  
    O objetivo é adaptação dos sistemas e validação do modelo.
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
    <div class='card texto'>
    ❌ <b>PIS e COFINS são extintos</b><br>
    ✔ Entra a <b>CBS definitiva</b><br><br>

    <b>Características da CBS:</b><br>
    • Não cumulativa (modelo IVA)<br>
    • Crédito financeiro amplo<br>
    • Alíquota estimada: <span class='highlight'>~8,8%</span><br><br>

    ⚠️ Empresas de serviços com poucos insumos
    tendem a sentir <b>aumento real da carga tributária</b>.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TABELA COMPARATIVA (HTML – NÃO IMAGEM)
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
                <th>Impacto</th>
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
                <td>Elevado</td>
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
    <div class='card texto'>
    ✔ 2026 é um ano de adaptação<br>
    ✔ A mudança financeira começa em 2027<br>
    ✔ Revisão de preços e contratos será essencial para empresas de serviços
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
