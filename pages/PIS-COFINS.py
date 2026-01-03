
import streamlit as st
import pandas as pd

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(page_title="Painel IBS/CBS – Serviços", page_icon="🟪", layout="centered")

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

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

    # Título
    st.markdown(
        "<h2 style='color:#1A3E5A;font-family:Segoe UI,Inter,Helvetica,Arial;font-weight:800;"
        "letter-spacing:.3px;text-align:center;border-bottom:2px solid #1A3E5A;"
        "padding-bottom:8px;margin:8px 0 20px 0;'>Reforma Tributária – IBS/CBS (Serviços / Empresa Patrimonial)</h2>",
        unsafe_allow_html=True
    )

    # =========================
    # TABELA – Cabeçalho agrupado (igual à imagem), sem índice
    # =========================
    st.markdown("**Tabela – Transição PIS/COFINS → CBS (SERVIÇOS)**")

    # Cabeçalho agrupado
    cols = pd.MultiIndex.from_tuples([
        ("Ano", ""),
        ("Tributos Atuais", "PIS/PASEP"),
        ("Tributos Atuais", "COFINS"),
        ("Novos Tributos", "CBS"),
    ])

    # Linhas conforme sua imagem
    data = [
        ["2024", "", "", ""],
        ["2025", "Sem mudanças", "", "-"],
        ["2026", "Alíquotas mantidas; com a possibilidade de compensação de 1% dos novos tributos (CBS 0,9% e IBS 0,1%).", "", "Alíquota teste: 0,9%"],
        ["2027", "", "", "Alíquota estabelecida (-) 0,1%"],
        ["2028", "", "", ""],
        ["2029", "", "", ""],
        ["2030", "Extinção", "", "Alíquota estabelecida"],
        ["2031", "", "", ""],
        ["2032", "", "", ""],
        ["2033", "", "", ""],
    ]

    df = pd.DataFrame(data, columns=cols)

    # Estilos iguais à imagem: cabeçalho azul claro, corpo branco, sem índice
    header_bg   = "#cfe0ef"   # azul claro
    header_text = "#000000"
    body_bg     = "#FFFFFF"
    body_text   = "#222222"
    border      = "#D0D0D0"

    styled = (
        df.style
        .hide(axis="index")  # sem índice
        .set_table_styles([
            {"selector": "th", "props": [
                ("background-color", header_bg),
                ("color", header_text),
                ("font-weight", "700"),
                ("text-align", "center"),
                ("border", f"1px solid {border}"),
                ("padding", "10px")
            ]},
            {"selector": "td", "props": [
                ("background-color", body_bg),
                ("color", body_text),
                ("border", f"1px solid {border}"),
                ("padding", "12px"),
                ("vertical-align", "middle"),
                ("text-align", "center")
            ]},
            {"selector": "table", "props": [
                ("border-collapse", "separate"),
                ("border-spacing", "0"),
                ("border", f"1px solid {border}"),
                ("border-radius", "12px"),
                ("overflow", "hidden")
            ]},
        ])
        # Evita quebra no "Ano" e define largura
        .set_properties(subset=pd.IndexSlice[:, ("Ano", "")], **{
            "white-space": "nowrap", "width": "100px", "min-width": "100px", "max-width": "100px"
        })
        # Larguras das outras colunas
        .set_properties(subset=pd.IndexSlice[:, ("Tributos Atuais", "PIS/PASEP")], **{"width": "360px"})
        .set_properties(subset=pd.IndexSlice[:, ("Tributos Atuais", "COFINS")], **{"width": "160px"})
        .set_properties(subset=pd.IndexSlice[:, ("Novos Tributos", "CBS")], **{"width": "220px"})
    )

    st.table(styled)
