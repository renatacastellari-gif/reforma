import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="PIS", page_icon="🟣")

# Cabeçalho
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("hines.svg", width=300)


# Título principal
st.markdown("""
<h2 style="
    color:#EEE4EF;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
PIS
</h2>
""", unsafe_allow_html=True)
st.markdown("**`PIS`**")










