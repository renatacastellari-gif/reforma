
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

    # ---- LOGO HINES (opcional) ----
    from PIL import Image, UnidentifiedImageError
    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)
    if logo_path:
        try:
            st.image(str(logo_path), width=220)
        except Exception:
            st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3>🟪 Hines – Painel Tributário</h3>", unsafe_allow_html=True)

    # ---- Título ----
    st.markdown(
        "<h2 style='color:#B22222;font-family:Times New Roman,sans-serif;font-weight:700;"
        "text-align:center;border-bottom:2px solid #B22222;padding-bottom:8px;margin-bottom:20px;'>"
        "Reforma Tributária</h2>",
        unsafe_allow_html=True
    )
    st.markdown("**`REFORMA TRIBUTÁRIA`**")

    # =========================
    # Leitura do Word: texto e imagens
    # =========================
    from docx import Document
    import zipfile
    import re

    DOCX_FILE = Path("fiscal reforma.docx")

    def ler_texto_docx(docx_path: Path) -> str:
        """
        Lê o .docx e retorna o texto completo (parágrafos + tabelas).
        Mantém o conteúdo sem alterações.
        """
        if not docx_path.exists():
            return ""
        doc = Document(str(docx_path))
        partes = []

        # Parágrafos
        for p in doc.paragraphs:
            t = p.text
            if t is not None:
                t = t.strip()
            if t:
                partes.append(t)

        # Tabelas (se existirem)
        for tb in doc.tables:
            for row in tb.rows:
                for cell in row.cells:
                    t = cell.text
                    if t is not None:
                        t = t.strip()
                    if t:
                        partes.append(t)

        # Junta com quebra dupla para melhorar legibilidade
        texto = "\n\n".join(partes)
        return texto

    def extrair_imagens_docx(docx_path: Path):
        """
        Extrai todas as imagens do .docx usando o pacote ZIP.
        Retorna lista de bytes (cada item é uma imagem).
        """
        imagens = []
        if not docx_path.exists():
            return imagens
        try:
            with zipfile.ZipFile(str(docx_path), 'r') as z:
                # As imagens ficam em /word/media/*
                for name in z.namelist():
                    if name.startswith("word/media/"):
                        with z.open(name) as f:
                            imagens.append(f.read())
        except Exception:
            pass
        return imagens

    def gerar_resumo_didatico(texto: str):
        """
        Gera um resumo didático a partir do próprio conteúdo do arquivo.
        - NÃO altera fatos (usa trechos/orientações do texto original).
        - Organiza para leigos em tópicos curtos.
        """
        if not texto:
            return ["Arquivo não encontrado ou sem conteúdo."]
        linhas = [l.strip() for l in texto.splitlines() if l.strip()]
        txt = "\n".join(linhas)

        # Função auxiliar para buscar uma linha contendo um padrão
        def pick(patterns, default=None):
            for pat in patterns:
                m = re.search(pat, txt, flags=re.IGNORECASE)
                if m:
                    # Pega a linha completa onde o match ocorreu
                    for l in linhas:
                        if re.search(pat, l, flags=re.IGNORECASE):
                            return l
            return default

        pontos = []

        # 1) Documento-base / contexto
        base = pick([r"Ato Conjunto.*RFB.*CGIBS.*001/2025", r"Ato Conjunto.*001/2025"])
        if base:
            pontos.append(f"📄 **Documento-base**: {base}")

        # 2) NFSe recepcionada para IBS/CBS
        nfse = pick([r"NFSe", r"Nota Fiscal de Serviços Eletrônica"])
        if nfse:
            pontos.append(f"🧾 **NFSe**: {nfse}")

        # 3) 2026 informativo / sem efeitos tributários
        p2026_info = pick([r"2026.*apuração.*não terá efeitos tributários", r"apuração.*2026.*informativa"])
        if p2026_info:
            pontos.append(f"ℹ️ **2026 (informativo)**: {p2026_info}")

        # 4) Campos IBS/CBS sem penalidade inicial
        campos = pick([r"não haverá penalidade.*campos.*IBS.*CBS", r"campos.*IBS.*CBS.*sem penalidade"])
        if campos:
            pontos.append(f"🧩 **Campos IBS/CBS na NFSe**: {campos}")

        # 5) Tributos atuais continuam
        continuam = pick([r"Este ato não elimina ISS", r"Tributos existentes continuam normalmente"])
        if continuam:
            pontos.append(f"⚖️ **Tributos atuais**: {continuam}")

        # 6) Transição: 0,9% CBS e 0,1% IBS (teste) e PIS/COFINS extinção 2027
        teste_cbs = pick([r"0,9%.*CBS", r"CBS.*0,9%"])
        teste_ibs = pick([r"0,1%.*IBS", r"IBS.*0,1%"])
        if teste_cbs or teste_ibs:
            pontos.append(f"🔁 **Transição 2026 (teste)**: {teste_cbs or ''} {teste_ibs or ''}".strip())
        extincao = pick([r"PIS.*COFINS.*serão extintos.*2027", r"extintos.*PIS.*Cofins.*2027"])
        if extincao:
            pontos.append(f"🗓️ **A partir de 2027**: {extincao}")

        # 7) Alíquota referencial / CBS ~8,8% (quando fixada)
        aliquota = pick([r"alíquota.*referência.*Senado", r"alíquota.*CBS.*fixará"])
        if aliquota:
            pontos.append(f"📈 **Alíquota da CBS**: {aliquota}")

        # 8) Créditos remanescentes de PIS/COFINS e estoque em 01/01/2027
        creditos = pick([r"créditos.*PIS.*Cofins.*continuarão válidos", r"Saldo Credor.*PIS/PASEP.*COFINS"])
        if creditos:
            pontos.append(f"💳 **Créditos na transição**: {creditos}")
        estoque = pick([r"estoque.*01\.01\.2027", r"estoque.*01/01/2027"])
        if estoque:
            pontos.append(f"📦 **Estoque em 01/01/2027**: {estoque}")

        # 9) Locação por PJ (3,65% atual vs CBS não cumulativa)
        locacao = pick([r"Locação.*pessoa jurídica", r"locação.*3,65%.*PIS.*COFINS"])
        if locacao:
            pontos.append(f"🏢 **Locação por PJ**: {locacao}")

        # 10) Exemplo prático do documento (comparação de valores)
        exemplo = pick([r"EXEMPLO REAL", r"Comparação final"])
        if exemplo:
            pontos.append(f"🧮 **Exemplo do documento**: {exemplo}")

        # Observação de verificação 1:1
        pontos.append("✅ Para conferir sem nenhuma alteração, veja a aba **Conteúdo Completo (1:1)**.")
        return pontos

    # Carrega conteúdo do Word
    texto_plano = ler_texto_docx(DOCX_FILE)
    imagens_bytes = extrair_imagens_docx(DOCX_FILE)

    # =========================
    # Abas
    # =========================
    tab_resumo, tab_completo, tab_transicao, tab_faq = st.tabs([
        "📌 Resumo Didático", "📄 Conteúdo Completo (1:1)", "⏱️ Transição 2026–2027", "❓ Perguntas rápidas"
    ])

    # =========================
    # 📌 RESUMO DIDÁTICO
    # =========================
    with tab_resumo:
        st.subheader("Visão geral em linguagem simples (sem alterar fatos)")
        if not texto_plano:
            st.warning("Arquivo 'fiscal reforma.docx' não encontrado na mesma pasta do app.")
        else:
            pontos = gerar_resumo_didatico(texto_plano)
            for item in pontos:
                st.markdown(f"- {item}")

            st.info(
                "Este resumo apenas reorganiza o conteúdo do arquivo com linguagem simples, "
                "SEM mudar números, prazos ou regras. Valide na aba “Conteúdo Completo (1:1)”."
            )

    # =========================
    # 📄 CONTEÚDO COMPLETO (1:1)
    # =========================
    with tab_completo:
        st.subheader("Conteúdo integral do Word — texto e imagens")
        if texto_plano:
            st.markdown("#### Texto integral")
            st.markdown(texto_plano)
        else:
            st.warning("Não foi possível carregar o texto do documento.")

        if imagens_bytes:
            st.markdown("#### Imagens extraídas do documento")
            cols = st.columns(3)
            for i, blob in enumerate(imagens_bytes):
                try:
                    img = Image.open(BytesIO(blob))
                    with cols[i % 3]:
                        st.image(img, use_column_width=True)
                except UnidentifiedImageError:
                    st.warning("Uma imagem do documento não pôde ser exibida.")
        else:
            st.info("Nenhuma imagem foi encontrada (ou não pôde ser extraída) no documento.")

    # =========================
    # ⏱️ TRANSIÇÃO 2026–2027
    # =========================
    with tab_transicao:
        st.subheader("Linha do tempo (extraída do documento)")
        if texto_plano:
            # Mostra trechos do próprio arquivo que citam 2026 e 2027 (para não alterar conteúdo)
            linhas = [l.strip() for l in texto_plano.splitlines() if l.strip()]
            trecho_2026 = [l for l in linhas if "2026" in l]
            trecho_2027 = [l for l in linhas if "2027" in l]

            st.markdown("**Trechos sobre 2026**")
            if trecho_2026:
                for l in trecho_2026:
                    st.markdown(f"- {l}")
            else:
                st.write("—")

            st.markdown("**Trechos sobre 2027**")
            if trecho_2027:
                for l in trecho_2027:
                    st.markdown(f"- {l}")
            else:
                st.write("—")

            st.info("A linha do tempo acima é composta por trechos do próprio arquivo, sem reescrita.")
        else:
            st.warning("Arquivo não encontrado para exibir a linha do tempo.")

    # =========================
    # ❓ PERGUNTAS RÁPIDAS
    # =========================
    with tab_faq:
        st.subheader("Explicações simples, com base no arquivo")
        st.markdown("**O que é CBS e IBS?** — São os impostos que substituem PIS/COFINS (CBS, federal) e ICMS/ISS (IBS, subnacional), com sistema não cumulativo e direito a crédito. (ver conteúdo completo)")
        st.markdown("**Em 2026 eu já pago CBS/IBS cheio?** — Não. 2026 é fase informativa/teste com alíquotas de 0,9% (CBS) e 0,1% (IBS), com compensação e possibilidade de dispensa parcial, conforme o documento. (ver conteúdo completo)")
        st.markdown("**Locação por PJ hoje paga o quê? E depois?** — Hoje: PIS/COFINS 3,65% (cumulativo). Após reforma: CBS não cumulativa com alíquota referencial mais alta; setores com poucos créditos sentem aumento. (ver conteúdo completo)")
        st.caption("Para qualquer decisão, consulte sempre o texto integral na aba ao lado.")
