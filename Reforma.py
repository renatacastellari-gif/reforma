
import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(page_title="Conciliações dos Impostos", page_icon="🟪", layout="wide")

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    hide_sidebar = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# =========================
# TELA DE LOGIN
# =========================
if not st.session_state.logged_in:
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun()
        else:
            st.error("Senha incorreta.")
else:
    # =========================
    # CONTEÚDO PROTEGIDO
    # =========================

    # --- LOGO: tenta hines.svg, hines.png, hines.jpg, hines.jpeg ---
    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)

    if logo_path is not None:
        try:
            st.image(str(logo_path), width=220)
        except Exception as e:
            st.warning(f"Não foi possível exibir a imagem '{logo_path.name}'. Detalhe: {e}")
            st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)
    else:
        st.info("Logo 'hines' não encontrado (aceitos: hines.svg, hines.png, hines.jpg, hines.jpeg). Coloque o arquivo na mesma pasta do app.")
        st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)

    # Título principal estilizado
    st.markdown("""
    <h2 style="
        color:#9B4DCC;
        font-family:'Montserrat',sans-serif;
        font-weight:700;
        text-align:center;
        border-bottom:2px solid #FFA500;
        padding-bottom:8px;
        margin-bottom:20px;">
    Conciliações dos Impostos
    </h2>
    """, unsafe_allow_html=True)

    # Marcador
    st.markdown("**`REFORMA TRIBUTÁRIA`**")

    # -------------------------
    # Abas principais
    # -------------------------
    tab_resumo, tab_hines, tab_venda_locacao, tab_transicao, tab_simulador, tab_conciliacoes, tab_fontes = st.tabs([
        "📌 Resumo", "🏢 Impactos na Hines", "🏠 Venda & Locação", "⏱️ Transição", "🧮 Simulador de Carga", "🗂️ Conciliações", "📎 Avisos & Fontes"
    ])

    # =========================
    # 📌 RESUMO
    # =========================
    with tab_resumo:
        st.subheader("Visão Geral")
        st.markdown("""
        **O que muda com a Reforma Tributária**  
        - Substituição de **PIS/COFINS** pela **CBS** (federal).  
        - Substituição de **ICMS/ISS** pelo **IBS** (estadual/municipal).  
        - Estrutura **não cumulativa** com apropriação de créditos ao longo da cadeia.  
        - Introdução do **Imposto Seletivo (IS)** para produtos específicos.  
        
        **Por que isso importa para Hines (setor imobiliário)**  
        - Maior necessidade de **gestão de créditos** em insumos/serviços de obras e incorporação.  
        - Revisão de contratos e cronogramas para mitigar impactos em fases intermediárias e transição.  
        - **Planejamento tributário** contínuo para decisão entre **Lucro Presumido** e **Lucro Real** (IRPJ/CSLL permanecem fora do escopo da reforma).  
        """)

        st.info("Dica rápida: traga os custos de insumos e serviços com granularidade por obra para capturar créditos da CBS/IBS e reduzir o custo efetivo.")

    # =========================
    # 🏢 IMPACTOS NA HINES
    # =========================
    with tab_hines:
        st.subheader("Impactos específicos para Hines")
        st.markdown("""
        **Créditos e Regimes**  
        - Após a reforma, tanto **Lucro Presumido** quanto **Lucro Real** poderão apropriar **créditos de CBS/IBS**.  
        - A diferença entre os regimes permanece principalmente em **IRPJ e CSLL** (bases de cálculo e ajustes fiscais).  

        **Gestão Operacional**  
        - Fim/ajustes de regimes especiais (como RET) e redução de créditos presumidos exigem maior acurácia contábil por obra.  
        - Rastreabilidade de custos e **compliance** fortalecidos (ex.: CIB/SINTER no segmento imobiliário).  

        **Ações Práticas**  
        1) **Simular cenários** (volumetria de créditos vs. alíquotas CBS/IBS).  
        2) **Revisar contratos** e cronogramas de obras (antecipar etapas quando benéfico).  
        3) Implementar **controles por obra** e integração contábil para segregação de créditos.  
        """)

        # Gráfico simples: Carga atual (exemplo informado)
        st.markdown("**Carga tributária atual (exemplo informado):**")
        atual = pd.DataFrame({
            "Tributo": ["PIS", "COFINS", "IRRF", "CSLL"],
            "Alíquota_%": [0.65, 3.00, 4.80, 2.88]
        })
        st.bar_chart(atual.set_index("Tributo"))

    # =========================
    # 🏠 VENDA & LOCAÇÃO
    # =========================
    with tab_venda_locacao:
        st.subheader("Venda e Locação de Imóveis")
        st.markdown("""
        **Venda (incorporações)**  
        - A incidência foca na **diferença** entre o **custo de venda** e o **valor do terreno**.  
        - Há **redutor social** (por exemplo, R$ 100 mil) para tornar a tributação progressiva – beneficiando imóveis populares.  
        - **Crédito amplo** sobre materiais e serviços utilizados na obra, reduzindo custo efetivo.  

        **Locação**  
        - Pessoas físicas com atividade **habitual/profissional** (e/ou volume relevante) podem tornar-se contribuintes de **CBS/IBS**, além do **IRPF**.  
        - Para pequenas locações pontuais, permanece o **IRPF** tradicional.  
        """)

        with st.expander("Notas operacionais"):
            st.markdown("""
            - Avaliar a estrutura societária para locações profissionais, considerando **direito a créditos** via PJ.  
            - Short-term (temporada) tende a ter maior carga efetiva por ser classificado como **serviço**.  
            """)

    # =========================
    # ⏱️ TRANSIÇÃO
    # =========================
    with tab_transicao:
        st.subheader("Linha do Tempo de Transição")
        st.markdown("""
        - **2026**: início da transição, aplicação de **alíquotas teste** de CBS/IBS; coexistência com tributos atuais.  
        - **2026–2032**: fases escalonadas com convivência de sistemas antigo e novo.  
        - **2033**: implementação plena do modelo CBS/IBS; extinção dos antigos tributos de consumo.  
        """)

        st.warning("Planeje sistemas e processos para convivência de dois modelos. Testes de crédito, conciliação e auditoria interna são essenciais.")

    # =========================
    # 🧮 SIMULADOR DE CARGA
    # =========================
    with tab_simulador:
        st.subheader("Simulador – Carga Atual vs. Pós-Reforma (cenário hipotético)")
        st.markdown("""
        **Como usar**  
        - Ajuste as alíquotas **CBS/IBS** estimadas (não cumulativo).  
        - Informe o **percentual de créditos** recuperáveis (insumos/serviços).  
        - Compare com a **carga atual** (PIS+COFINS+IRRF+CSLL = 11,33%).  

        > **Atenção**: Este simulador é **didático** e **não substitui** análise oficial/regulamentação. Use para sensibilizar cenários internos.
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            cbs = st.number_input("CBS estimada (%)", min_value=0.0, max_value=50.0, value=8.0, step=0.1)
        with col2:
            ibs = st.number_input("IBS estimada (%)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
        with col3:
            creditos = st.number_input("Créditos recuperáveis (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)

        # Carga atual
        carga_atual = 0.65 + 3.00 + 4.80 + 2.88  # 11,33%

        # Carga pós-reforma (didática): CBS+IBS líquidos de créditos + IRRF+CSLL (mantidos)
        # Fórmula simplificada: carga_nova = (CBS+IBS) * (1 - creditos%) + IRRF + CSLL
        carga_nova = (cbs + ibs) * (1 - creditos/100.0) + 4.80 + 2.88

        # Apresentação
        colA, colB = st.columns(2)
        with colA:
            st.metric("Carga Atual (%)", f"{carga_atual:.2f}")
        with colB:
            st.metric("Cenário Pós-Reforma (%)", f"{carga_nova:.2f}")

        # Gráfico comparativo
        df_comp = pd.DataFrame({
            "Cenário": ["Atual", "Pós-Reforma (simulado)"],
            "Carga_%": [carga_atual, carga_nova]
        })
        st.bar_chart(df_comp.set_index("Cenário"))

        with st.expander("Parâmetros e suposições do simulador"):
            st.markdown("""
            - **CBS/IBS** aqui são parâmetros ajustáveis para estudos internos.  
            - O **percentual de créditos** reflete a fração dos tributos recuperáveis via insumos/serviços.  
            - **IRRF** e **CSLL** são mantidos para comparação (a reforma não altera IRPJ/CSLL).  
            """)

    # =========================
    # 🗂️ CONCILIAÇÕES (bloco original)
    # =========================
    with tab_conciliacoes:
        st.subheader("Conciliações dos Impostos – Razão vs. Fiscal")
        st.markdown("<p style='font-size:28px; font-weight:bold; color:#FFA500;'>Seja bem-vindo(a)!</p>", unsafe_allow_html=True)

        st.markdown("""
        Esta aplicação apresenta as **demonstrações das conciliações entre os saldos fiscais e contábeis (Razão)**, destacando as **diferenças identificadas** e seus respectivos detalhes.

        O objetivo é oferecer uma visão clara e organizada para apoiar os departamentos fiscal e contábil:
        - **Conciliação dos impostos**
        - **Validação dos lançamentos contábeis**
        - **Identificação de ajustes necessários**

        ✅ Navegue pelas abas para consultar as diferenças do mês.

        ---
        > **Objetivo:** Garantir o alinhamento entre os saldos fiscais e contábeis, prevenindo divergências nos registros.  
        <span style="color:#FFD700;">Desenvolvemos essa página para proporcionar acesso rápido e facilidade na visualização das conciliações.</span>
        """, unsafe_allow_html=True)

        # Dados como strings (códigos de contas), alinhados
        dados = [
            ("IPI a Recolher", "2300390"),
            ("ICMS a Recolher", "2300391"),
            ("COFINS a Recolher", "2300394"),
            ("PIS a Recolher", "2300395"),
            ("IPI a Recuperar", "1280342"),
            ("PIS a Recuperar", "1280343"),
            ("COFINS a Recuperar", "1280344"),
            ("ICMS a Recuperar", "1280345"),
            ("VENDAS", "4000000"),
        ]
        linhas_formatadas = [f"{nome:<25} {codigo:>10}" for nome, codigo in dados]
        st.code("\n".join(linhas_formatadas))

    # =========================
    # 📎 AVISOS & FONTES
    # =========================
    with tab_fontes:
        st.subheader("Avisos & Fontes (consultar antes de decisões)")
        st.markdown("""
        - Ministério da Fazenda – **Impactos da Reforma** (CBS/IBS, princípio do destino, transição):  
          https://www.gov.br/fazenda/pt-br/acesso-a-informacao/acoes-e-programas/futuro-seguro/reforma-tributaria/impactos-da-reforma

        - Nota à imprensa – **Setor Imobiliário** (redutor social, base de incidência nas incorporações):  
          https://www.gov.br/fazenda/pt-br/canais_atendimento/imprensa/notas-a-imprensa/2025/abril/reforma-tributaria-sera-positiva-para-o-setor-imobiliario

        - Artigos sobre **Lucro Presumido vs. Lucro Real** pós-reforma e créditos não cumulativos:  
          https://netcpa.com.br/colunas/principais-impactos-da-reforma-tributaria-para-empresas-do-lucro-real-lucro-presumido-e-simples-nacional/24146  
          https://blog.camargoevieira.adv.br/planejamento-tributario-na-reforma-tributaria/

        - **Imobiliário**: impactos práticos, fim de regimes especiais e transição:  
          https://www.controllercontabil.com.br/setor-imobiliario-e-construcao-civil-os-impactos-da-reforma-tributaria-de-2025-para-empresas-e-investidores/

        - **CIB/SINTER** e reforço de controle sobre transações imobiliárias:  
          https://jornalcontabil.ig.com.br/noticia/entenda-o-impacto-que-a-reforma-tributaria-tera-nas-atividades-imobiliarias/
               """)

        # *** Linha única para evitar quebra de string ***

