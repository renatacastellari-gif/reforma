
import streamlit as st
from pathlib import Path
import pandas as pd

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Reforma Tributária – PIS/COFINS",
    page_icon="🟥",
    layout="centered"
)

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Esconde sidebar se não estiver logado
if not st.session_state.logged_in:
    st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# =========================
# TELA DE LOGIN
# =========================
if not st.session_state.logged_in:
    st.title("🔒 Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar", use_container_width=True):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado!")
            st.rerun()
        else:
            st.error("Senha incorreta.")

# =========================
# CONTEÚDO PROTEGIDO
# =========================
else:

    # =========================
    # TIPOGRAFIA (ajuste aqui se quiser trocar)
    # =========================
    BODY_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"
    # Ex.: para visual “clean”:
    # BODY_FONT = "'Segoe UI', Roboto, Helvetica, Arial, system-ui, -apple-system, sans-serif"
    # HEADING_FONT = "Consolas, Menlo, Monaco, 'Courier New', monospace"

    # =========================
    # CSS GLOBAL (FUNDO PRETO + CARDS + TIPOGRAFIA)
    # =========================
    style_str = f"""
    <style>
        html, body, [class*="css"] {{
            background-color: #000000;
        }}
        body {{
            font-family: {BODY_FONT};
        }}

        .content-wrapper {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        .titulo-principal {{
            font-family: {HEADING_FONT};
            font-size: 34px;
            font-weight: 800;
            color: #B91E27;
            margin-bottom: 10px;
            text-align: left;
            border-bottom: 2px solid #B91E27;
            padding-bottom: 8px;
            letter-spacing: 0.2px;
        }}

        .subtitulo {{
            font-size: 22px;
            font-weight: 700;
            color: #D96569;
            margin-top: 30px;
        }}

        .texto {{
            font-size: 16px;
            color: #dddddd;
            line-height: 1.65;
        }}

        .card {{
            background-color: #1e1e1e;
            color: #f0f0f0;
            padding: 26px 28px;
            border-radius: 14px;
            margin: 22px 0;
            border-left: 6px solid #B91E27;
            box-shadow: 0 2px 0 #111111;
        }}

        .card h3 {{
            font-family: {HEADING_FONT};
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 0.2px;
        }}

        .card ul {{
            margin: 10px 0 0 18px;
            padding: 0;
            list-style-type: disc;
        }}

        .card li {{
            font-size: 17px;
            line-height: 1.7;
            margin-bottom: 6px;
            color: #e6e6e6;
        }}

        .card li b {{
            color: #ffffff;
            font-weight: 700;
        }}

        .card p {{
            margin: 0;
            color: #dcdcdc;
            font-size: 16px;
            line-height: 1.65;
        }}

        .img-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 12px;
        }}

        .callout {{
            background: #101010;
            border: 1px dashed #B91E27;
            border-radius: 10px;
            padding: 14px 16px;
            margin-top: 12px;
            color: #dddddd;
            font-size: 16px;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # Wrapper
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # =========================
    # TÍTULO
    # =========================
    st.markdown("<div class='titulo-principal'>Reforma Tributária | Emissão de Nota </div>", unsafe_allow_html=True)

    # =========================
    # CARD: CBS / IBS
    # =========================
    st.markdown(
        "<div class='card'>"
        "<h3>NF Prefeitura de São Paulo – CBS - IBS</h3>"
        "<ul>"
        "<li>Código de Classificação Tributária Principal: <b>200052 - Prestação de serviços das seguintes profissões "
        "intelectuais de natureza científica, literária ou artística, submetidas à fiscalização por conselho profissional: "
        "administradores, advogados, arquitetos e urbanistas, assistentes sociais, bibliotecários, biólogos, contabilistas, "
        "economistas, economistas domésticos, profissionais de educação física, engenheiros e agrônomos, estatísticos, médicos veterinários e "
        "zootecnistas, museólogos, químicos, profissionais de relações públicas, "
        "técnicos industriais e técnicos agrícolas, observado o art. 127 da Lei Complementar nº 214, de 2025.</b></li>"
        "<li>Código do Indicador de Operação: <b>20301 - Serviço de administração e intermediação de bem imóvel</b></li>"
        "<li>Código NBS: <b>114011100 - Serviços de consultoria em gestão estratégica</b> </li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    # =========================
    # IMAGEM: imagem.png
    # =========================
    img_path = Path("imagem.png")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Visualização</h3>", unsafe_allow_html=True)

    if img_path.exists():
        # Exibe imagem centralizada
        st.markdown("<div class='img-container'>", unsafe_allow_html=True)
        st.image(str(img_path), caption="Imagem referência", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Arquivo 'imagem.png' não encontrado na pasta do aplicativo.")

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # TABELA MELHORADA (VALORES INFORMADOS)
    # =========================
    # Dados conforme solicitado
    bruto = 287_870.13
    linhas = [
        {"Percentual": 0.0150, "Valor (R$)": 4318.05, "Tributo / Item": "IRRF"},
        {"Percentual": 0.0465, "Valor (R$)": 13385.96, "Tributo / Item": "PCC"},
        {"Percentual": 0.0500, "Valor (R$)": 14393.51, "Tributo / Item": "ISS"},
        # Totais e itens sem percentual
        {"Percentual": None,   "Valor (R$)": bruto,      "Tributo / Item": "VALOR BRUTO"},
        {"Percentual": None,   "Valor (R$)": 255_772.61, "Tributo / Item": "VALOR LÍQUIDO"},
        {"Percentual": 0.0007, "Valor (R$)": 0.62,       "Tributo / Item": "IBS"},
        {"Percentual": 0.0063, "Valor (R$)": 5.60,       "Tributo / Item": "CBS"},
    ]

    df = pd.DataFrame(linhas, columns=["Tributo / Item", "Percentual", "Valor (R$)"])

    # Ordena para ficar próximo da visualização do exemplo
    ordem = ["VALOR BRUTO", "IRRF", "PCC", "ISS", "VALOR LÍQUIDO", "IBS", "CBS"]
    df["ordem_aux"] = df["Tributo / Item"].apply(lambda x: ordem.index(x) if x in ordem else 999)
    df = df.sort_values("ordem_aux").drop(columns=["ordem_aux"]).reset_index(drop=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Tabela Resumo</h3>", unsafe_allow_html=True)

    # Configuração de colunas com formatação
    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "Tributo / Item": st.column_config.TextColumn("Tributo / Item"),
            "Percentual": st.column_config.NumberColumn(
                "Percentual",
                format="%.2f%%",
            ),
            "Valor (R$)": st.column_config.NumberColumn(
                "Valor (R$)",
                format="R$ %.2f",
            ),
        }
    )

    # Callout com totais destacados
    st.markdown(
        f"""
        <div class='callout'>
            <b>Resumo</b><br>
            Valor Bruto: <b>R$ {bruto:,.2f}</b><br>
            Valor Líquido: <b>R$ {255_772.61:,.2f}</b>
        </div>
        """.replace(",", "X").replace(".", ",").replace("X", "."),
        unsafe_allow_html=True
    )

    # Fecha wrapper
    st.markdown("</div>", unsafe_allow_html=True)
