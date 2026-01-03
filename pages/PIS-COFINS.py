    # =========================
    # PÁGINA: PIS / COFINS → CBS
    # =========================

    st.markdown("""
    <style>
        .titulo {
            font-size: 34px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 10px;
        }
        .subtitulo {
            font-size: 22px;
            font-weight: bold;
            color: #c08497;
            margin-top: 30px;
        }
        .texto {
            font-size: 17px;
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
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        thead th {
            background-color: #6b1f3a; /* vinho */
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 16px;
        }
        tbody td {
            background-color: #0f0f0f;
            color: #eaeaea;
            padding: 10px;
            border-bottom: 1px solid #333333;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='titulo'>PIS & COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='texto'>
    Esta página resume, de forma simples, como a <b>Reforma Tributária</b> afeta empresas
    <b>prestadoras de serviços de consultoria e assessoria patrimonial imobiliária</b>.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # RESUMO 2026
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box texto'>
    ✔ A CBS entra em <b>fase piloto</b><br>
    ✔ Alíquota de teste: <b>0,9%</b><br>
    ✔ O valor pago é <b>compensado com PIS e COFINS</b><br>
    ✔ Pode haver <b>dispensa de recolhimento</b> se as obrigações acessórias forem entregues<br><br>
    ❗ Em 2026 <b>não há aumento real de carga tributária</b>.  
    O foco é apenas informativo.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # A PARTIR DE 2027
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027 — Mudança Real</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box texto'>
    ❌ PIS e COFINS são <b>extintos</b><br>
    ✔ Entra a <b>CBS</b>, substituindo ambos<br><br>

    <b>Características da CBS:</b><br>
    • Não cumulativa (modelo IVA)<br>
    • Crédito financeiro amplo<br>
    • Alíquota estimada: <b>~8,8%</b><br><br>

    ⚠️ Para serviços com poucos insumos (como consultoria),
    o impacto tende a ser <b>aumento real de carga</b>.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # TABELA COMPARATIVA
    # =========================
    st.markdown("<div class='subtitulo'>📊 Comparativo — Antes x Depois</div>", unsafe_allow_html=True)

    dados = {
        "Situação": ["Até 2025", "Ano de 2026", "A partir de 2027"],
        "Tributo": ["PIS + COFINS", "CBS (teste)", "CBS definitiva"],
        "Alíquota": ["3,65%", "0,9%", "~8,8%"],
        "Crédito": ["Não", "Sim (compensado)", "Sim (pleno)"],
        "Impacto Financeiro": ["Baixo", "Neutro", "Mais elevado"]
    }

    df = pd.DataFrame(dados)

    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    # =========================
    # CONCLUSÃO
    # =========================
    st.markdown("""
    <div class='subtitulo'>🧾 Conclusão Prática</div>
    <div class='box texto'>
    ✔ Em 2026, sua empresa <b>não paga mais imposto</b><br>
    ✔ A grande mudança começa em <b>2027</b><br>
    ✔ Serviços com pouca despesa creditável sentem mais o impacto<br><br>
    📌 Recomenda-se revisar <b>precificação e contratos</b> antes da virada definitiva.
    </div>
    """, unsafe_allow_html=True)
