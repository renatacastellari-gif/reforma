
import streamlit as st
from pathlib import Path
from io import BytesIO

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(page_title="Reforma Tributária", page_icon="🟪" )

# =========================
# SENHA FIXA / LOGIN
# =========================
PASSWORD = "minhasenha123"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    st.markdown("&lt;style&gt;[data-testid='stSidebar']{display:none;}&lt;/style&gt;", unsafe_allow_html=True)

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

    # ---- LOGO HINES (opcional) ----
    try:
        from PIL import Image, UnidentifiedImageError  # pode não existir no ambiente
    except Exception:
        Image, UnidentifiedImageError = None, Exception

    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)
    if logo_path:
        try:
            # streamlit também aceita bytes/paths sem precisar do PIL
            st.image(str(logo_path), width=220)
        except Exception:
            st.markdown("&lt;h3&gt;🟪 Hines – Painel Tributário&lt;/h3&gt;", unsafe_allow_html=True)
    else:
        st.markdown("&lt;h3&gt;🟪 Hines – Painel Tributário&lt;/h3&gt;", unsafe_allow_html=True)

    # ---- Título ----
    st.markdown(
        "&lt;h2 style='color:#B22222;font-family:Times New Roman,sans-serif;font-weight:700;"
        "text-align:center;border-bottom:2px solid #B22222;padding-bottom:8px;margin-bottom:20px;'&gt;"
        "Reforma Tributária&lt;/h2&gt;",
        unsafe_allow_html=True
    )
    st.markdown("**`REFORMA TRIBUTÁRIA`**")

    # =========================
    # Leitura do Word (com e sem python-docx)
    # =========================
    DOCX_FILE = Path("fiscal reforma.docx")

    # Tenta usar python-docx (se existir); senão, faz fallback via zip/xml
    def ler_texto_e_imagens(docx_path: Path):
        """
        Retorna (texto_completo, lista_de_imagens_em_bytes).
        - Se python-docx estiver disponível, usa para texto (parágrafos/tabelas).
        - Imagens sempre por zipfile (word/media/*).
        - Fallback sem python-docx: extrai texto dos nós w:t em word/document.xml.
        """
        texto = ""
        imagens = []

        # Imagens: sempre pelo zip (independe de python-docx)
        import zipfile
        try:
            with zipfile.ZipFile(str(docx_path), 'r') as z:
                for name in z.namelist():
                    if name.startswith("word/media/"):
                        with z.open(name) as f:
                            imagens.append(f.read())
        except Exception:
            pass

        # Texto: tenta python-docx
        try:
            from docx import Document  # pode não existir
            doc = Document(str(docx_path))
            partes = []
            # Parágrafos
            for p in doc.paragraphs:
                t = (p.text or "").strip()
                if t:
                    partes.append(t)
            # Tabelas
            for tb in doc.tables:
                for row in tb.rows:
                    for cell in row.cells:
                        t = (cell.text or "").strip()
                        if t:
                            partes.append(t)
            texto = "\n\n".join(partes)
            if texto.strip():
                return texto, imagens
        except Exception:
            # Fallback: sem python-docx, extrai w:t de word/document.xml
            pass

        # Fallback via XML
        try:
            import xml.etree.ElementTree as ET
            with zipfile.ZipFile(str(docx_path), 'r') as z:
                # documento principal
                xml_bytes = z.read("word/document.xml")
                root = ET.fromstring(xml_bytes)
                ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
                textos = [el.text for el in root.findall(".//w:t", ns) if el.text]
                texto = "\n".join(textos).strip()
        except Exception:
            texto = ""

        return texto, imagens

    texto_plano, imagens_bytes = ("", [])
    if DOCX_FILE.exists():
        texto_plano, imagens_bytes = ler_texto_e_imagens(DOCX_FILE)
    else:
        st.warning("Arquivo 'fiscal reforma.docx' não encontrado na mesma pasta do app.")

    # ===== Utilitários =====
    import re

    def gerar_resumo_didatico(texto: str):
        """
        Resumo didático derivado do próprio texto do arquivo.
        Não altera fatos; apenas organiza em linguagem simples.
        """
        if not texto:
            return ["Arquivo não encontrado ou sem conteúdo."]

        # Normaliza espaçamentos
        base_txt = re.sub(r"\s+", " ", texto).strip()

        def achou(pat):
            return re.search(pat, base_txt, flags=re.IGNORECASE)

        pontos = []
        # Documento-base
        if achou(r"Ato Conjunto.*RFB.*CGIBS.*001/2025"):
            pontos.append("📄 **Documento-base**: Ato Conjunto RFB/CGIBS nº 001/2025 — define documentos fiscais para IBS e CBS e regras de transição em 2026.")
        # NFSe recepcionada
        if achou(r"NFSe|Nota Fiscal de Serviços Eletrônica"):
            pontos.append("🧾 **NFSe**: permanece obrigatória na prestação de serviços e é recepcionada para IBS/CBS.")
        # Sem penalidade inicial de campos IBS/CBS
        if achou(r"não haverá penalidade.*IBS.*CBS"):
            pontos.append("🧩 **Campos IBS/CBS na NFSe**: no início, não há penalidade se os novos campos não forem preenchidos até o prazo indicado.")
        # 2026 informativo
        if achou(r"2026.*apuração.*não.*efeitos tributários") or achou(r"apuração.*2026.*informativa"):
            pontos.append("ℹ️ **2026 (apuração informativa)**: deve enviar informações de IBS/CBS, mas sem efeito tributário de apuração no ano.")
        # Tributos atuais continuam
        if achou(r"não elimina ISS") or achou(r"Tributos existentes continuam"):
            pontos.append("⚖️ **Tributos atuais**: ISS (enquanto vigente), IRPJ, CSLL, PIS/COFINS etc. continuam conforme regras atuais.")
        # Transição 0,9% / 0,1%
        if achou(r"0,9%.*CBS"):
            pontos.append("🔁 **Transição 2026**: CBS de 0,9% (teste) com compensação contra PIS/COFINS.")
        if achou(r"0,1%.*IBS"):
            pontos.append("🔁 **Transição 2026**: IBS de 0,1% (teste) com compensação.")
        # Extinção PIS/COFINS 2027
        if achou(r"2027.*PIS.*Cofins.*extintos"):
            pontos.append("🗓️ **A partir de 2027**: PIS e COFINS são extintos; CBS passa a valer plenamente com alíquota a ser fixada.")
        # Créditos transição
        if achou(r"Saldo Credor.*PIS") or achou(r"créditos.*PIS.*Cofins.*continuarão válidos"):
            pontos.append("💳 **Créditos de PIS/COFINS**: continuam válidos; podem compensar CBS, com regras e prazos específicos.")
        # Estoque 01/01/2027
        if achou(r"estoque.*01.?01.?2027"):
            pontos.append("📦 **Estoque em 01/01/2027**: possibilidade de crédito presumido em condições definidas.")
        # Locação por PJ
        if achou(r"Locação.*pessoa jurídica") or achou(r"3,65%.*PIS.*COFINS"):
            pontos.append("🏢 **Locação por PJ**: hoje paga 3,65% (PIS/COFINS cumulativo); após reforma, CBS não cumulativa (alíquota maior), o que pode elevar a carga quando há poucos créditos.")
        # Exemplo do documento
        if achou(r"EXEMPLO REAL") or achou(r"Comparação final"):
            pontos.append("🧮 **Exemplo prático**: o documento traz um caso de locação comparando antes/depois (mesmo com créditos e redutor).")

        pontos.append("✅ Para validação 1:1, veja a aba **Conteúdo Completo (texto + imagens)**.")
        return pontos

    def show_image_bytes(blob_bytes):
        # Tenta abrir com PIL para melhor compatibilidade; se não tiver, usa bytes direto.
        if Image is not None:
            try:
                img = Image.open(BytesIO(blob_bytes))
                st.image(img, use_column_width=True)
                return
            except Exception:
                pass
        st.image(blob_bytes, use_column_width=True)

    # =========================
    # Abas
    # =========================
    tab_resumo, tab_completo, tab_transicao, tab_faq = st.tabs([
        "📌 Resumo Didático", "📄 Conteúdo Completo (1:1)", "⏱️ Transição 2026–2027", "❓ Perguntas rápidas"
    ])

    # =========================
    # 📌 RESUMO
    # =========================
    with tab_resumo:
        st.subheader("Visão geral em linguagem simples (sem alterar fatos)")
        if not texto_plano:
            st.warning("Não foi possível carregar o texto do documento (verifique se o arquivo está na mesma pasta).")
        else:
            for item in gerar_resumo_didatico(texto_plano):
                st.markdown(f"- {item}")
            st.info("O resumo reorganiza o conteúdo original para leigos, sem mudar números, prazos ou regras.")

    # =========================
    # 📄 CONTEÚDO COMPLETO (1:1)
    # =========================
    with tab_completo:
        st.subheader("Conteúdo integral do Word — texto e imagens")
        if texto_plano:
            st.markdown("#### Texto integral")
            st.markdown(texto_plano)
        else:
            st.warning("Texto não carregado.")
        if imagens_bytes:
            st.markdown("#### Imagens do documento")
            cols = st.columns(3)
            for i, blob in enumerate(imagens_bytes):
                with cols[i % 3]:
                    show_image_bytes(blob)
        else:
            st.info("Nenhuma imagem encontrada ou extraída do documento.")

    # =========================
    # ⏱️ TRANSIÇÃO
    # =========================
    with tab_transicao:
        st.subheader("Trechos do documento que falam da transição")
        if texto_plano:
            linhas = [l.strip() for l in texto_plano.splitlines() if l.strip()]
            trechos_2026 = [l for l in linhas if "2026" in l]
            trechos_2027 = [l for l in linhas if "2027" in l]

            st.markdown("**2026**")
            if trechos_2026:
                for l in trechos_2026:
                    st.markdown(f"- {l}")
            else:
                st.write("—")

            st.markdown("**2027**")
            if trechos_2027:
                for l in trechos_2027:
                    st.markdown(f"- {l}")
            else:
                st.write("—")
            st.caption("Conteúdo acima vem literalmente do arquivo (sem reescrita).")
        else:
            st.warning("Arquivo não carregado para montar a linha do tempo.")

    # =========================
    # ❓ PERGUNTAS RÁPIDAS
    # =========================
    with tab_faq:
        st.subheader("Explicações simples, baseadas no documento")
        st.markdown("**O que são CBS e IBS?** — Substituem PIS/COFINS (CBS, federal) e ICMS/ISS (IBS), com sistema não cumulativo e crédito.")
        st.markdown("**Em 2026 pago CBS/IBS cheio?** — Não. 2026 é fase de teste/informativa com alíquotas reduzidas e compensação.")
        st.markdown("**Locação por PJ** — Hoje: PIS/COFINS 3,65% (cumulativo). Depois: CBS não cumulativa (alíquota mais alta); setores com poucos créditos tendem a perceber aumento.")
        st.caption("Para qualquer decisão, confira o texto integral na aba ao lado.")
