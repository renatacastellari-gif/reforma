
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
    # TIPOGRAFIA
    # =========================
    BODY_FONT = "'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    HEADING_FONT = "'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

    # =========================
    # CSS GLOBAL
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

        /* Ajuste para espaçamento e fonte do primeiro card */
        .card ul {{
            margin: 10px 0 0 18px;
            padding: 0;
            list-style-type: none;
        }}

        .card li {{
            font-size: 18px;
            line-height: 1.8;
            margin-bottom: 18px; /* Espaçamento maior entre itens */
            color: #ffffff;
        }}

        .card li b {{
            font-weight: 700;
            color: #ffffff;
        }}
    </style>
    """
    st.markdown(style_str, unsafe_allow_html=True)

    # =========================
    # CONTEÚDO
    # =========================
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    st.markdown("<div class='titulo-principal'>Reforma Tributária | Emissão de Nota </div>", unsafe_allow_html=True)

    # =========================
    # PRIMEIRO CARD (MELHORADO)
    # =========================
    st.markdown(
        """
        <div class='card'>
            <h3>NF Prefeitura de São Paulo – CBS - IBS</h3>
            <ul>
                <li><b>Código de Classificação Tributária Principal:</b> <b>200052</b> - <b>Prestação de serviços das seguintes profissões intelectuais de natureza científica, literária ou artística, submetidas à fiscalização por conselho profissional:</b> administradores, advogados, arquitetos e urbanistas, assistentes sociais, bibliotecários, biólogos, contabilistas, economistas, economistas domésticos, profissionais de educação física, engenheiros e agrônomos, estatísticos, médicos veterinários e zootecnistas, museólogos, químicos, profissionais de relações públicas, técnicos industriais e técnicos agrícolas, observado o art. 127 da Lei Complementar nº 214, de 2025.</li>
                
                <li><b>Código do Indicador de Operação:</b> <b>20301</b> - <b>Serviço de administração e intermediação de bem imóvel</b></li>
                
                <li><b>Código NBS:</b> <b>114011100</b> - <b>Serviços de consultoria em gestão estratégica</b></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # RESTANTE IGUAL
    # =========================
    img_path = Path("imagem.png")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Visualização</h3>", unsafe_allow_html=True)

    if img_path.exists():
        st.markdown("<div class='img-container'>", unsafe_allow_html=True)
        st.image(str(img_path), caption="Imagem referência", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Arquivo 'imagem.png' não encontrado na pasta do aplicativo.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Tabela Exemplo</h3>", unsafe_allow_html=True)

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

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>✅ BASE LEGAL — REDUÇÃO DE 30% CBS E IBS</h3>", unsafe_allow_html=True)

    base_legal_html = """
    <div class="texto">
        A Lei Complementar nº 214/2025, art. 127, determina:<br><br>
        <i>“Ficam reduzidas em 30% as alíquotas do IBS e da CBS incidentes sobre a prestação de serviços por
        profissionais que exerçam atividades intelectuais de natureza científica, literária ou artística,
        submetidas à fiscalização por conselho profissional.”</i><br><br>
        <span class="badge"><b>CBS:</b> 0,90%</span>
        <span class="badge"><b>IBS:</b> 0,10%</span>
    </div>
    """
    st.markdown(base_legal_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
