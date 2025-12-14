
import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="PIS", page_icon="🟣", layout="wide")

# Cabeçalho com logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("hines.svg", width=300)

# Título principal (estilo elegante)
st.markdown(
    """
    <h2 style="
        color:#9B4DCC;
        font-family:'Montserrat',sans-serif;
        font-weight:700;
        text-align:center;
        border-bottom:2px solid #FFA500;
        padding-bottom:8px;
        margin-bottom:20px;">
        Reforma Tributária – PIS e COFINS
    </h2>
    """,
    unsafe_allow_html=True
)

# Etiqueta pequena
st.markdown("**`REFORMA TRIBUTÁRIA`**")

# ====== LAYOUT EM COLUNAS PARA OS CARDS ======
cA, cB = st.columns(2)

with cA:
    st.markdown(
        """
        <div style="
            background-color:#1f1f1f;
            border:1px solid #333;
            border-radius:12px;
            padding:18px;
            box-shadow:0 0 0 1px rgba(255,255,255,0.04) inset;">
            <h3 style="color:#EEE4EF; font-family:'Montserrat',sans-serif; margin-top:0;">Resumo – PIS e COFINS (situação atual)</h3>
            <p style="color:#cfcfcf; font-size:15px; line-height:1.5;">
                <b>PIS</b> e <b>COFINS</b> são contribuições federais sobre a receita. <br/>
                • <b>Lucro Presumido (cumulativo):</b> PIS 0,65% + COFINS 3,00% = <b>3,65%</b> sobre a receita. <br/>
                • <b>Lucro Real (não cumulativo):</b> alíquotas maiores (PIS 1,65% / COFINS 7,60%), porém com <b>direito a créditos</b> sobre insumos e serviços. <br/><br/>
                Para empresas patrimoniais/imobiliárias, incidem sobre receitas de locação e, conforme o caso, sobre receitas de venda (com particularidades de base).
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with cB:
    st.markdown(
        """
        <div style="
            background-color:#1f1f1f;
            border:1px solid #333;
            border-radius:12px;
            padding:18px;
            box-shadow:0 0 0 1px rgba(255,255,255,0.04) inset;">
            <h3 style="color:#EEE4EF; font-family:'Montserrat',sans-serif; margin-top:0;">O que muda com a Reforma (CBS)</h3>
            <p style="color:#cfcfcf; font-size:15px; line-height:1.5;">
                • <b>PIS/COFINS</b> serão substituídos pela <b>CBS (Contribuição sobre Bens e Serviços)</b>. <br/>
                • A CBS será <b>não cumulativa</b> para todos os regimes, permitindo <b>créditos</b> amplos de insumos/serviços. <br/>
                • A alíquota da CBS será <b>única</b> (definição final depende de regulamentação), e a carga efetiva tenderá a diminuir quando houver muitos créditos recuperáveis. <br/><br/>
                <b>Transição:</b> coexistência entre sistema atual e CBS ao longo de 2026–2032. Planejamento e simulação tornam-se essenciais.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ====== BLOCO ESPECÍFICO PARA HINES ======
st.markdown(
    """
    <div style="
        background-color:#101010;
        border:1px solid #333;
        border-radius:12px;
        padding:18px;
        margin-top:18px;">
        <h3 style="color:#EEE4EF; font-family:'Montserrat',sans-serif; margin-top:0;">Impacto prático para a Hines (patrimonial/imobiliária)</h3>
        <ul style="color:#cfcfcf; font-size:15px; line-height:1.6;">
            <li><b>Locação:</b> receita passa a ter CBS com <b>direito a crédito</b> sobre despesas diretamente vinculadas (manutenção, serviços, gestão, etc.).</li>
            <li><b>Venda de imóveis:</b> regra da reforma foca na <b>diferença entre preço de venda e custo do terreno</b>, com crédito abrangente sobre insumos/serviços de obra.</li>
            <li><b>Lucro Presumido x Lucro Real:</b> a grande diferença seguirá em <b>IRPJ/CSLL</b>; como a CBS concede crédito para todos, a escolha do regime deve considerar a margem efetiva e o perfil de custos.</li>
            <li><b>Governança:</b> necessário <b>mapear despesas elegíveis</b> e reforçar a <b>rastreabilidade por ativo/obra</b> para maximizar créditos.</li>
        </ul>
        <p style="color:#aaa; font-size:13px; margin-top:8px;">
            <i>Dica:</i> detalhe custos por empreendimento/ativo e formalize contratos de serviços para documentar créditos da CBS.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ====== MINI-SIMULADOR DIDÁTICO ======
st.markdown(
    """
    <h3 style="color:#EEE4EF; font-family:'Montserrat',sans-serif; margin-top:24px;">Comparativo didático – Carga atual vs. CBS</h3>
    <p style="color:#cfcfcf; font-size:14px;">
        Ajuste os parâmetros para ver o efeito potencial. <br/>
        <b>Atenção:</b> este simulador é apenas ilustrativo; a alíquota final e regras dependerão de regulamentação.
    </p>
    """,
    unsafe_allow_html=True
)

col_sim1, col_sim2, col_sim3 = st.columns(3)
with col_sim1:
    cbs = st.number_input("CBS estimada (%)", min_value=0.0, max_value=30.0, value=8.0, step=0.1)
with col_sim2:
    creditos = st.number_input("Créditos recuperáveis (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
with col_sim3:
    carga_atual = 3.65  # PIS 0,65% + COFINS 3,00% (cumulativo no presumido)
    st.metric("Carga atual (PIS+COFINS)", f"{carga_atual:.2f}%")

# Fórmula didática: CBS líquida de créditos
carga_cbs_liquida = cbs * (1 - creditos/100.0)

df_comp = pd.DataFrame({
    "Cenário": ["Atual (PIS+COFINS)", "CBS (líquida de créditos)"],
    "Carga_%": [carga_atual, carga_cbs_liquida]
})
st.bar_chart(df_comp.set_index("Cenário"))

# Observação final
st.markdown(
    """
    <div style="background-color:#111; border:1px solid #333; border-radius:10px; padding:14px; margin-top:14px;">
      <p style="color:#cfcfcf; font-size:13px; line-height:1.5;">
        <b>Observação:</b> no <b>Lucro Real</b>, a carga atual de PIS/COFINS é diferente, porém com créditos. A CBS tende a <b>uniformizar</b> o direito a créditos para todos,
        então a <b>carga efetiva</b> dependerá fortemente do seu mix de        então a <b>carga efetiva</b> dependerá fortemente do seu mix de despesas elegíveis e da eficiência na gestão de créditos.
      </p>
    </div>
    """,
    unsafe_allow_html=True
