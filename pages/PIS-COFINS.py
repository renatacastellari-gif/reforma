
import streamlit as st
import pandas as pd
from pathlib import Path

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

    # ---- Estilo global (fundo escuro, tipografia clean, vinho da marca) ----
    st.markdown(
        """
        <style>
        :root {
            --wine: #B22222; /* vinho principal */
            --wine-dark: #7A0C16; /* vinho escuro para detalhes */
            --bg-card: #121212; /* cards sobre fundo preto */
            --text: #EDEDED; /* texto em claro */
            --muted: #B0B0B0; /* texto secundário */
        }
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', 'Inter', 'Helvetica Neue', Arial, sans-serif;
        }
        .wine-title {
            color: var(--wine);
            font-weight: 800;
            letter-spacing: .5px;
            text-align:center;
            border-bottom: 2px solid var(--wine);
            padding-bottom: 8px; margin: 8px 0 18px 0;
        }
        .badge {
            display:inline-block; background: var(--wine-dark); color:#fff; padding:6px 10px; border-radius:999px; font-weight:600; font-size:13px;
        }
        .card {background: var(--bg-card); border:1px solid #222; border-radius:14px; padding:16px;}
        .card h3 {color:#fff; margin-top:0}
        .card p, .card li {color: var(--text);}
        .muted {color: var(--muted);}
        /* Tabela */
        .rt-thead .rt-th {background: var(--wine); color:#fff; font-weight:700}
        table {border-collapse: separate; border-spacing: 0; border-radius: 10px; overflow: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---- Cabeçalho com logo (opcional) ----
    logo_candidates = [Path("logo.png"), Path("logo.jpg"), Path("logo.jpeg"), Path("logo_vinho.png")]
    logo_path = next((p for p in logo_candidates if p.exists()), None)
    if logo_path:
        st.image(str(logo_path), width=160)

    st.markdown("<h2 class='wine-title'>Reforma Tributária – IBS/CBS (Serviços / Empresa Patrimonial)</h2>", unsafe_allow_html=True)

    # ---- Corpo do texto em cards minimalistas ----
    st.markdown("<span class='badge'>RESUMO</span>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
    <h3>1. O que muda para quem presta serviços (consultoria, assessoria)</h3>
    <ul>
      <li>Continuar emitindo <b>NFS‑e</b> (padrão nacional).</li>
      <li>Visualizar <b>campos de IBS e CBS</b> na nota.</li>
      <li><b>Sem multa</b> nos primeiros meses se não preencher esses campos.</li>
      <li><b>Sem pagamento</b> de IBS/CBS em 2026.</li>
    </ul>
    <p><b>Resumo:</b> você continua com a NFS‑e; 2026 é fase de teste sem aumento de custo; o governo quer apenas as informações.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>2. Por que existe a fase de teste em 2026?</h3>
    <ul>
      <li>Testar comunicação das notas</li>
      <li>Testar cálculo automático</li>
      <li>Validar leiaute</li>
    </ul>
    <p><b>CBS = 0,9%</b> · <b>IBS = 0,1%</b>. Esse 1% é <b>compensado</b> com PIS/COFINS; e, conforme a LC 214/2025 (art. 348, §1º), pode haver <b>dispensa do recolhimento</b> em 2026 para quem cumprir obrigações acessórias.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>3. O que muda de verdade a partir de 2027</h3>
    <ul>
      <li>PIS + COFINS deixam de existir</li>
      <li>Entra a <b>CBS</b> (alíquota estimada ~8,8%)</li>
      <li>IBS continua (mais relevante para municípios/estados)</li>
    </ul>
    <p><b>Serviços puros</b> tendem a ter impacto maior (poucos créditos para descontar).</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>4. Por que a alíquota sobe (3,65% → ~8,8%)?</h3>
    <ul>
      <li>PIS/COFINS (3,65%) é <b>cumulativo</b> → tributa receita bruta.</li>
      <li>CBS (~8,8%) é <b>não cumulativo</b> → tributa valor agregado.</li>
      <li>Serviços têm pouco insumo → <b>crédito baixo</b>.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>5. O essencial para empresa patrimonial</h3>
    <p><b>2026:</b> NFS‑e normal · IBS/CBS sem pagamento real · sem multa inicial · obrigação informativa.</p>
    <p><b>2027:</b> fim de PIS/COFINS · entra CBS · serviços pagam mais por baixo crédito · IBS conforme atividade.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>6. Créditos de PIS/COFINS</h3>
    <ul>
      <li>Não desaparecem</li>
      <li>Abatem CBS</li>
      <li>Podem ser ressarcidos ou compensados</li>
      <li>Depreciação vira crédito presumido de CBS</li>
    </ul>
    <p class='muted'>Protege quem acumulou crédito no regime antigo.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<span class='badge'>TABELA</span>", unsafe_allow_html=True)

    # =========================
    # TABELA – sem índice; fundo branco; cabeçalho vinho; coluna "Ano" sem quebra
    # =========================
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

    df = pd.DataFrame(data, columns=["Ano", "PIS/PASEP", "COFINS", "CBS"])

    wine   = "#B22222"  # vinho igual ao título
    white  = "#FFFFFF"
    border = "#D0D0D0"

    styled = (
        df.style
        .hide(axis="index")
        .set_table_styles([
            {"selector": "th", "props": [
                ("background-color", wine),
                ("color", white),
                ("font-weight", "700"),
                ("text-align", "center"),
                ("border", f"1px solid {border}"),
                ("padding", "10px")
            ]},
            {"selector": "td", "props": [
                ("background-color", white),
                ("color", "#222"),
                ("border", f"1px solid {border}"),
                ("padding", "12px"),
                ("vertical-align", "middle")
            ]},
            {"selector": "table", "props": [
                ("border-collapse", "separate"),
                ("border-spacing", "0"),
                ("border", f"1px solid {border}"),
                ("border-radius", "12px"),
                ("overflow", "hidden")
            ]},
        ])
        .set_properties(subset=["Ano", "PIS/PASEP", "COFINS", "CBS"], **{
            "text-align": "center"
        })
        .set_properties(subset=["Ano"], **{
            "white-space": "nowrap",
            "width": "110px",
            "min-width": "110px",
            "max-width": "110px"
        })
        .set_properties(subset=["PIS/PASEP"], **{"width": "380px"})
        .set_properties(subset=["COFINS"], **{"width": "160px"})
        .set_properties(subset=["CBS"], **{"width": "220px"})
    )

    st.table(styled)
