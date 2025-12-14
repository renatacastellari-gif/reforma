
import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(page_title="Reforma Tributária", page_icon="🟪", layout="wide")

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    st.markdown(
        "<style>[data-testid='stSidebar'] {display: none;}</style>",
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
        st.info("Logo 'hines' não encontrado. Coloque hines.svg/png/jpg na mesma pasta do app.")
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
    # Abas principais (SEM a aba Conciliações)
    # -------------------------
    tab_resumo, tab_hines, tab_venda_locacao, tab_transicao, tab_simulador, tab_fontes = st.tabs([
        "📌 Resumo", "🏢 Impactos na Hines", "🏠 Venda & Locação", "⏱️ Transição", "🧮 Simulador de Carga", "📎 Avisos & Fontes"
    ])

    # =========================
    # 📌 RESUMO
    # =========================
    with tab_resumo:
        st.subheader("Visão Geral")
        st.markdown(
            "**O que muda com a Reforma Tributária**  \n"
            "- Substituição de **PIS/COFINS** pela **CBS** (federal).  \n"
            "- Substituição de **ICMS/ISS** pelo **IBS** (estadual/municipal).  \n"
            "- Estrutura **não cumulativa** com apropriação de créditos ao longo da cadeia.  \n"
            "- Introdução do **Imposto Seletivo (IS)** para produtos específicos.  \n\n"
            "**Por que isso importa para Hines (setor imobiliário)**  \n"
            "- Maior necessidade de **gestão de créditos** em insumos/serviços de obras e incorporação.  \n"
            "- Revisão de contratos e cronogramas para mitigar impactos em fases intermediárias e transição.  \n"
            "- **Planejamento tributário** contínuo para decisão entre **Lucro Presumido** e **Lucro Real** (IRPJ/CSLL fora do escopo da reforma)."
        )
        st.info("Dica: detalhe custos por obra para capturar créditos de CBS/IBS.")

    # =========================
    # 🏢 IMPACTOS NA HINES
    # =========================
    with tab_hines:
        st.subheader("Impactos específicos para Hines")
        st.markdown(
            "**Créditos e Regimes**  \n"
            "- Após a reforma, **Lucro Presumido** e **Lucro Real** poderão apropriar **créditos de CBS/IBS**.  \n"
            "- Diferenças permanecem em **IRPJ/CSLL** (bases e ajustes).  \n\n"
            "**Gestão Operacional**  \n"
            "- Ajustes de regimes e redução de créditos presumidos exigem acurácia por obra.  \n"
            "- Fortalecer **compliance** e rastreabilidade (CIB/SINTER).  \n\n"
            "**Ações Práticas**  \n"
            "1) Simular cenários (créditos vs. alíquotas).  \n"
            "2) Revisar contratos e cronogramas.  \n"
            "3) Implementar controles por obra e integração contábil."
        )

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
        st.markdown(
            "**Venda (incorporações)**  \n"
            "- Incidência na **diferença** entre custo de venda e valor do terreno, com redutor social para imóveis populares.  \n"
            "- **Crédito** sobre materiais e serviços da obra.  \n\n"
            "**Locação**  \n"
            "- PF com atividade habitual/profissional pode recolher **CBS/IBS** além do **IRPF**.  \n"
            "- Pequenas locações: permanece **IRPF** tradicional."
        )
        with st.expander("Notas operacionais"):
            st.markdown(
                "- Avaliar estrutura PJ em locações profissionais para aproveitar créditos.  \n"
                "- Temporada/serviços pode ter carga maior por classificação."
            )

    # =========================
    # ⏱️ TRANSIÇÃO
    # =========================
    with tab_transicao:
        st.subheader("Linha do Tempo de Transição")
        st.markdown(
            "- **2026**: início da transição; alíquotas-teste; coexistência de sistemas.  \n"
            "- **2026–2032**: fases escalonadas.  \n"
            "- **2033**: modelo CBS/IBS pleno."
        )
        st.warning("Prepare processos para convivência dos dois modelos e auditoria interna de créditos.")

    # =========================
    # 🧮 SIMULADOR
    # =========================
    with tab_simulador:
        st.subheader("Simulador – Carga Atual vs. Pós-Reforma (didático)")
        st.markdown(
            "**Como usar**  \n"
            "- Ajuste **CBS/IBS**.  \n"
            "- Informe **créditos recuperáveis**.  \n"
            "- Compare com a **carga atual** (11,33%).  \n\n"
            "> Este simulador é didático e não substitui análise oficial."
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            cbs = st.number_input("CBS estimada (%)", min_value=0.0, max_value=50.0, value=8.0, step=0.1)
        with col2:
            ibs = st.number_input("IBS estimada (%)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
        with col3:
            creditos = st.number_input("Créditos recuperáveis (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)

        carga_atual = 0.65 + 3.00 + 4.80 + 2.88  # 11,33%
        carga_nova = (cbs + ibs) * (1 - creditos/100.0) + 4.80 + 2.88  # didático

        colA, colB = st.columns(2)
        with colA:
            st.metric("Carga Atual (%)", f"{carga_atual:.2f}")
        with colB:
            st.metric("Pós-Reforma (simulado) (%)", f"{carga_nova:.2f}")

        df_comp = pd.DataFrame({"Cenário": ["Atual", "Pós-Reforma (simulado)"], "Carga_%": [carga_atual, carga_nova]})
        st.bar_chart(df_comp.set_index("Cenário"))

        with st.expander("Parâmetros e suposições"):
            st.markdown(
                "- **CBS/IBS** são parâmetros ajustáveis.  \n"
                "- **Créditos** refletem insumos/serviços.  \n"
                "- **IRRF/CSLL** mantidos para comparação."
            )

    # =========================
    # 📎 FONTES
    # =========================
    with tab_fontes:
        st.subheader("Avisos & Fontes (consultar antes de decisões)")
        st.markdown(
            "- Ministério da Fazenda – Impactos da Reforma: https://www.gov.br/fazenda/pt-br/acesso-a-informacao/acoes-e-programas/futuro-seguro/reforma-tributaria/impactos-da-reforma  \n"
            "- Nota à imprensa – Setor Imobiliário: https://www.gov.br/fazenda/pt-br/canais_atendimento/imprensa/notas-a-imprensa/2025/abril/reforma-tributaria-sera-positiva-para-o-setor-imobiliario  \n"
            "- Lucro Presumido vs. Lucro Real (créditos): https://netcpa.com.br/colunas/principais-impactos-da-reforma-tributaria-para-empresas-do-lucro-real-lucro-presumido-e-simples-nacional/24146  \n"
            "- Planejamento pós-reforma: https://blog.camargoevieira.adv.br/planejamento-tributario-na-reforma-tributaria/  \n"
            "- Imobiliário e transição: https://www.controllercontabil.com.br/setor-imobiliario-e-construcao-civil-os-impactos-da-reforma-tributaria-de-2025-para-empresas-e-investidores/  \n"
            "- CIB/SINTER: https://jornalcontabil.ig.com.br/noticia/entenda-o-impacto-que-a-reforma-tributaria-tera-nas-atividades-imobiliarias/"
        )
        # Mantenha esta linha curta para não quebrar:
        st.info("Use as fontes como apoio e acompanhe normas complementares.")
``

