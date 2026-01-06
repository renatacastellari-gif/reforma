
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

        /* Tabela Exemplo */
        .tabela-exemplo {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 6px;
        }}
        .tabela-exemplo td {{
            padding: 8px 10px;
            border-bottom: 1px solid #2a2a2a;
            color: #e6e6e6;
            font-size: 16px;
        }}
        .tabela-exemplo td:first-child {{
            width: 160px;
            text-align: right;
            font-variant-numeric: tabular-nums;
        }}
        .tabela-exemplo td:last-child {{
            text-align: left;
        }}
        .negrito {{
            font-weight: 700;
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
    # TABELA EXEMPLO (SUBSTITUI A TABELA RESUMO)
    # =========================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Tabela Exemplo</h3>", unsafe_allow_html=True)

    # Conteúdo da tabela exatamente como solicitado, com 888,50 em negrito
    tabela_html = """
    <table class="tabela-exemplo">
        <tr>
            <td class="negrito">1.000,00</td>
            <td class="negrito">VALOR BRUTO</td>
        </tr>
        <tr>
            <td>15,00</td>
            <td>IRRF 1,5%</td>
        </tr>
        <tr>
            <td>46,50</td>
            <td>PCC 4,65%</td>
        </tr>
        <tr>
            <td>50,00</td>
            <td>ISS 5%</td>
        </tr>
        <tr>
            <td class="negrito">888,50</td>
            <td class="negrito">Base de Calculo IBS CBS</td>
        </tr>
        <tr>
            <td>0,62</td>
            <td>IBS 0,07%</td>
        </tr>
        <tr>
            <td>5,60</td>
            <td>CBS 0,63%</td>
        </tr>
    </table>
    """
    st.markdown(tabela_html, unsafe_allow_html=True)

    # Callout opcional com destaque
    st.markdown(
        """
        <div class='callout'>
            <b>Resumo</b><br>
            Valor Bruto: <b>R$ 1.000,00</b><br>
            Base de Cálculo IBS/CBS: <b>R$ 888,50</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fecha wrapper
    st.markdown("</div>", unsafe_allow_html=True)

