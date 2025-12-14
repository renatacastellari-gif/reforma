
import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------------------
# Configuração da página (SEM wide)
# ---------------------------
st.set_page_config(page_title="PIS", page_icon="🟣")

# ---------------------------
# Cabeçalho com logo Hines
# ---------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # tenta hines.svg/png/jpg/jpeg
    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)
    if logo_path:
        try:
            st.image(str(logo_path), width=300)
        except Exception as e:
            st.warning(f"Não foi possível exibir a imagem '{logo_path.name}'. Detalhe: {e}")
            st.markdown("<h3>Hines</h3>", unsafe_allow_html=True)
    else:
        st.info("Logo 'hines' não encontrado (hines.svg/png/jpg).")
        st.markdown("<h3>Hines</h3>", unsafe_allow_html=True)

# ---------------------------
# Título principal estilizado
# ---------------------------
 st.markdown(
        "<h2 style='color:#B22222;font-family:Times New Roman,sans-serif;font-weight:700;text-align:center;border-bottom:2px solid #B22222;padding-bottom:8px;margin-bottom:20px;'>Reforma Tributária</h2>",
        unsafe_allow_html=True
    )
st.markdown("**`REFORMA TRIBUTÁRIA`**")

# ---------------------------
# Cards de conteúdo (Resumo e Reforma)
# ---------------------------
cA, cB = st.columns(2)

with cA:
    st.markdown(
        "<div style='background-color:#1f1f1f;border:1px solid #333;border-radius:12px;"
        "padding:18px;box-shadow:0 0 0 1px rgba(255,255,255,0.04) inset;'>"
        "<h3 style='color:#EEE4EF;font-family:Montserrat,sans-serif;margin-top:0;'>"
        "Resumo – PIS e COFINS (situação atual)</h3>"
        "<p style='color:#cfcfcf;font-size:15px;line-height:1.6;'>"
        "<b>PIS</b> e <b>COFINS</b> incidem sobre a receita das empresas.<br>"
        "• <b>Lucro Presumido (cumulativo):</b> PIS 0,65% + COFINS 3,00% = <b>3,65%</b> sobre a receita.<br>"
        "• <b>Lucro Real (não cumulativo):</b> PIS 1,65% / COFINS 7,60%, com <b>créditos</b> de insumos/serviços.<br><br>"
        "Para empresas patrimoniais/imobiliárias, incidem sobre <b>receitas de locação</b> e, conforme o caso, sobre <b>receitas de venda</b>."
        "</p></div>",
        unsafe_allow_html=True
    )

with cB:
    st.markdown(
        "<div style='background-color:#1f1f1f;border:1px solid #333;border-radius:12px;"
        "padding:18px;box-shadow:0 0 0 1px rgba(255,255,255,0.04) inset;'>"
        "<h3 style='color:#EEE4EF;font-family:Montserrat,sans-serif;margin-top:0;'>"
        "O que muda com a Reforma (CBS)</h3>"
        "<p style='color:#cfcfcf;font-size:15px;line-height:1.6;'>"
        "• <b>PIS/COFINS</b> serão substituídos pela <b>CBS</b> (não cumulativa).<br>"
        "• <b>Créditos</b> de insumos/serviços passam a ser amplos para todos os regimes.<br>"
        "• Alíquota da CBS será <b>única</b> (definição final depende de regulamentação).<br><br>"
        "<b>Transição:</b> coexistência entre sistema atual e CBS ao longo de 2026–2032; é essencial simular cenários."
        "</p></div>",
        unsafe_allow_html=True
    )

# ---------------------------
# Impacto prático para a Hines
# ---------------------------
st.markdown(
    "<div style='background-color:#101010;border:1px solid #333;border-radius:12px;"
    "padding:18px;margin-top:18px;'>"
    "<h3 style='color:#EEE4EF;font-family:Montserrat,sans-serif;margin-top:0;'>"
    "Impacto prático para a Hines (patrimonial/imobiliária)</h3>"
    "<ul style='color:#cfcfcf;font-size:15px;line-height:1.6;'>"
    "<li><b>Locação:</b> receita com CBS e <b>direito a crédito</b> sobre despesas vinculadas (manutenção, serviços, gestão).</li>"
    "<li><b>Venda de imóveis:</b> foco na <b>diferença</b> entre preço de venda e custo do terreno; créditos de obra reduzem custo efetivo.</li>"
    "<li><b>Regimes:</b> a escolha entre <b>Presumido x Real</b> continua por <b>IRPJ/CSLL</b>; a CBS equaliza créditos, então avalie a margem e o perfil de custos.</li>"
    "<li><b>Governança:</b> mapear <b>despesas elegíveis</b> e reforçar a <b>rastreabilidade por ativo/obra</b> para maximizar créditos.</li>"
    "</ul>"
    "<p style='color:#aaa;font-size:13px;margin-top:8px;'>"
    "<i>Dica:</i> detalhe custos por empreendimento/ativo e formalize contratos de serviços para documentar créditos da CBS."
    "</p></div>",
    unsafe_allow_html=True
)

# ---------------------------
# Mini-simulador didático (carga atual vs. CBS líquida de créditos)
# ---------------------------
st.markdown(
    "<h3 style='color:#EEE4EF;font-family:Montserrat,sans-serif;margin-top:24px;'>"
    "Comparativo didático – Carga atual vs. CBS</h3>"
    "<p style='color:#cfcfcf;font-size:14px;'>"
    "Ajuste os parâmetros para ver o efeito potencial. <b>Observação:</b> este simulador é ilustrativo; a alíquota final depende de regulamentação."
    "</p>",
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

carga_cbs_liquida = cbs * (1 - creditos/100.0)

df_comp = pd.DataFrame({
    "Cenário": ["Atual (PIS+COFINS)", "CBS (líquida de créditos)"],
    "Carga_%": [carga_atual, carga_cbs_liquida]
})
st.bar_chart(df_comp.set_index("Cenário"))

# Observação final (curta para evitar quebra de string)
st.info("No Lucro Real, há créditos atuais de PIS/COFINS; a CBS tende a uniformizar créditos para todos. A carga efetiva dependerá do mix de despesas elegíveis e da eficiência nos créditos.")


