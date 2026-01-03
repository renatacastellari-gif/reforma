import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Reforma Tributária – CBS",
    page_icon="🟪",
    layout="centered"
)

# =========================
# LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.title("🔒 Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# APP
# =========================
else:

    # =========================
    # CSS GLOBAL
    # =========================
    st.markdown("""
    <style>
    body { background-color: #000000; }

    .titulo {
        font-size: 34px;
        font-weight: bold;
        color: #B91E27;
        margin-bottom: 12px;
    }

    .subtitulo {
        font-size: 22px;
        font-weight: bold;
        color: #EBBFC1;
        margin-top: 35px;
    }

    .texto {
        font-size: 16px;
        color: #EDEDED;
        line-height: 1.6;
    }

    .card {
        background-color: #111111;
        padding: 22px;
        border-radius: 14px;
        margin-top: 15px;
        border: 1px solid #2a2a2a;
    }

    .highlight {
        color: #F2D5D7;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='texto'>Resumo prático da Reforma Tributária aplicado a empresas de serviços.</div>",
        unsafe_allow_html=True
    )

    # =========================
    # 2026
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card texto">
    ✔ Entrada da <b>CBS em fase piloto</b><br>
    ✔ Alíquota teste: <span class="highlight">0,9%</span><br>
    ✔ Valor compensado com PIS e COFINS<br>
    ✔ Possível dispensa se cumprir obrigações acessórias<br><br>
    ❗ <b>Não há aumento real de carga tributária em 2026</b>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 2027+
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card texto">
    ❌ PIS e COFINS são extintos<br>
    ✔ Entra a <b>CBS definitiva</b><br><br>

    <b>Características da CBS:</b><br>
    • Não cumulativa (modelo IVA)<br>
    • Crédito financeiro amplo<br>
    • Alíquota estimada: <span class="highlight">~8,8%</span><br><br>

    ⚠️ Empresas de serviços com poucos insumos
    tendem a sentir <b>aumento real da carga tributária</b>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CONCLUSÃO
    # =========================
    st.markdown("<div class='subtitulo'>🧾 Conclusão Prática</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card texto">
    ✔ 2026 é um ano de adaptação<br>
    ✔ Impacto financeiro real inicia em 2027<br>
    ✔ Revisão de preços e contratos será essencial
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # FUNÇÃO EXCEL → IMAGEM
    # =========================
    def gerar_imagem_tabela(df, caminho):
        fig, ax = plt.subplots(figsize=(len(df.columns)*2.2, len(df)*0.6))
        ax.axis('off')

        tabela = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            cellLoc='center',
            loc='center'
        )

        tabela.auto_set_font_size(False)
        tabela.set_fontsize(11)
        tabela.scale(1, 1.4)

        for (row, col), cell in tabela.get_celld().items():
            if row == 0:
                cell.set_facecolor("#B91E27")
                cell.set_text_props(color="white", weight="bold")
            else:
                cell.set_facecolor("#F9EEEF" if row % 2 == 0 else "#F2D5D7")
                cell.set_text_props(color="#2B2B2B")
            cell.set_edgecolor("#EBBFC1")

        plt.savefig(caminho, dpi=200, bbox_inches='tight', transparent=True)
        plt.close()

    # =========================
    # DADOS DO EXCEL (IMAGEM)
    # =========================
    st.markdown("<div class='subtitulo'>📊 Dados Detalhados</div>", unsafe_allow_html=True)

    excel_path = Path("dados_cbs.xlsx")
    imagem_path = Path("tabela_cbs.png")

    if excel_path.exists():
        df = pd.read_excel(excel_path)
        gerar_imagem_tabela(df, imagem_path)

        st.image(
            str(imagem_path),
            caption="Tabela gerada automaticamente a partir do Excel",
            use_container_width=True
        )
    else:
        st.error("Arquivo dados_cbs.xlsx não encontrado.")
