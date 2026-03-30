import streamlit as st
import streamlit.components.v1 as components

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

# Esconde sidebar até logar
if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
            [data-testid='stSidebar']{display:none;}
        </style>
        """,
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
            # Use APENAS UM, conforme sua versão:
            try:
                st.rerun()  # versões recentes
            except AttributeError:
                st.experimental_rerun()  # versões antigas
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:
    # =========================
    # CSS GLOBAL + WRAPPERS (HTML REAL)
    # =========================
    st.markdown("""
    <style>
        /* ====== IMPORTS DE FONTES ====== */
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');

        html, body, [class*="css"] { background-color: #1b1b1b; }
        body { color: #F9EEEF; font-family: 'Open Sans', Arial, sans-serif; }

        /* ====== WRAPPER DE LARGURA ====== */
        .content-wrapper {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 12px;
        }

        /* ====== TÍTULO ====== */
        .titulo-principal {
            font-family: 'JetBrains Mono', 'Fira Mono', 'Consolas', monospace !important;
            font-size: 38px;
            font-weight: 800;
            color: #B91E27;
            letter-spacing: 0.06em;
            margin: 0 0 12px 0;
            position: relative;
            display: inline-block;
        }
        .titulo-principal::after {
            content: "";
            display: block;
            height: 2px;
            background-color: #B91E27;
            margin-top: 10px;
            width: 95%;
        }

        /* ====== CARD ====== */
        .card {
            background-color: #2a2a2a;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
            color: #f0f0f0;
            font-family: 'Montserrat', 'Open Sans', Arial, sans-serif;
            font-size: 18px;
            line-height: 1.8;
        }
        .card h3, .card h4 {
            font-family: 'Montserrat', 'Segoe UI', Roboto, Arial, sans-serif;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.3px;
        }
        .card h3 { font-size: 28px; }
        .card h4 { font-size: 22px; }
        .card p, .card li, .card ul {
            font-family: 'Montserrat', 'Open Sans', Arial, sans-serif;
        }
        .highlight {
            color: #F2D5D7;
            font-weight: 600;
        }

        /* ====== TABELAS ====== */
        table { width:100%; border-collapse: collapse; margin-top:10px; font-size: 16px; }
        th, td { border:1px solid #3a3a3a; padding:12px; }
        th { background:#303030; color:#fff; }
        tr:nth-child(even) td {background:#252525;}
        tr:nth-child(odd) td {background:#202020;}
        tfoot td {font-weight:800; background:#2b2b2b;}
    </style>
    """, unsafe_allow_html=True)

    # Abre wrapper de conteúdo
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
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
    # NOVO CARD 1
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🚩 Excedeu os R$ 5 milhões acumulados no ano</h3>
        <p>Quando o <b>faturamento acumulado no ano ultrapassa R$ 5.000.000</b>, os <b>trimestres restantes</b> do ano-calendário passam a aplicar a <b>presunção majorada</b>, <i>mesmo que algum trimestre isolado não passe de R$ 1,25 mi</i>.</p>
        <ul>
            <li>Gatilho anual: <b>R$ 5.000.000</b>.</li>
            <li>Após o gatilho, aplica-se <b>+10%</b> sobre a base de presunção (ex.: serviços de 32% → <b>35,2%</b>).</li>
            <li>Vigência: vale para <b>todos os períodos seguintes</b> dentro do mesmo ano-calendário.</li>
        </ul>
        <p class="highlight">Conclusão: o acompanhamento é <b>anual</b>. O limite trimestral ajuda no cálculo, mas não isola o efeito após o gatilho anual.</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # NOVO CARD 2
    # =========================
    st.markdown("""
    <div class='card'>
        <h3>🧭 Resumo das Regras (trimestre × ano)</h3>
        <ul>
            <li><b>Limite trimestral:</b> R$ 1.250.000/trimestre para aplicar as bases sem acréscimo.</li>
            <li><b>Acima do limite trimestral:</b> a <i>parcela excedente</i> já recebe presunção majorada (ex.: serviços 35,2%).</li>
            <li><b>Atingiu R$ 5 milhões no ano:</b> todos os <i>períodos seguintes</i> usam presunção majorada, <i>independentemente</i> do valor do trimestre.</li>
        </ul>
        <p class="highlight">Até R$ 1,25 mi no trimestre → presunção padrão. Excedente do trimestre → majorada. Ultrapassou R$ 5 mi no ano → majorada nos trimestres seguintes.</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # ÚLTIMO CARD: APENAS TÍTULO + VÍDEO
    # =========================
    st.markdown("""
    <div class='card'>
        <h4>Nova regra só se aplica a CSLL no 2º trimestre de 2026.</h4>
    </div>
    <h4>Nota ECONET: A partir de 01.04.2026, será aplicado um acréscimo de 10% nos percentuais de presunção sobre receita bruta, se esta exceder R$ 5 milhões no ano-calendário. Esse limite será proporcionalizado por trimestre, ou seja, será de R$ 1.250.000,00 por trimestre. No ano-calendário de 2026, o limite anual proporcional aplicável corresponderá a R$ 3.750.000,00, pois o acréscimo será aplicado a partir do segundo trimestre para a CSLL. (artigo 4°, § 5°, da Lei Complementar n° 224/2025; artigo 15, §§ 1°, 2° e 9°, 
    da IN RFB n° 2.305/2025, 
    alterado pelo artigo 1° da IN RFB n° 2.306/2026)</h4>
    """, unsafe_allow_html=True)

    # Player via iframe DIRETO (sem wrapper responsivo → não gera bloco preto)
    video_id = "lCdcBlPqBxk"
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    components.iframe(
        src=f"{embed_url}?rel=0&modestbranding=1&playsinline=1",
        height=420,  # ajuste se quiser: 360, 420, 480
        scrolling=False
    )

    # Fallback visível (link) caso a rede bloqueie o player
    with st.expander("Não conseguiu reproduzir? Clique para abrir no YouTube ▶️"):
        st.markdown(f"https://www.youtube.com/watch?v={video_id}", unsafe_allow_html=True)

    # Fecha wrapper de conteúdo
    st.markdown("</div>", unsafe_allow_html=True)
