
import streamlit as st
from pathlib import Path
from io import BytesIO
import pandas as pd

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
        from PIL import Image, UnidentifiedImageError
    except Exception:
        Image, UnidentifiedImageError = None, Exception

    candidatos = [Path("hines.svg"), Path("hines.png"), Path("hines.jpg"), Path("hines.jpeg")]
    logo_path = next((p for p in candidatos if p.exists()), None)
    if logo_path:
        try:
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
    # ABAS PRINCIPAIS
    # =========================
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Resumo Didático", "NFS-e e Ato Conjunto", "Linha do Tempo", "Calculadora de Locação", "Créditos PIS/COFINS → CBS", "Imagens e Tabelas"
    ])

    # -------------------------
    # 1) RESUMO DIDÁTICO
    # -------------------------
    with tab1:
        st.subheader("📌 O que muda para prestadores de serviços (2026)")
        st.markdown(
            """
            **Pontos-chave 2026 (fase informativa/teste):**
            - Emissão **obrigatória** de documento fiscal eletrônico nas operações com bens e serviços. Para serviços, a **NFS-e** continua sendo o documento padrão.  
            - Os **campos de IBS/CBS** nos documentos fiscais **não geram penalidade** inicialmente: a tolerância vai até o **1º dia do 4º mês** após a publicação da parte comum dos regulamentos do IBS/CBS.  
            - **Não há efeitos tributários** de apuração de IBS/CBS em 2026 (caráter educativo), **desde que** cumpridas as obrigações acessórias.  
            - A NFS-e **nacional** segue sob governança do **CGNFS-e** (padronização e leiaute).  
            - Tributos atuais (ISS, IRPJ, CSLL, PIS/COFINS etc.) **permanecem vigentes** conforme a legislação de transição.  
            """
        )
        st.info("Referências: Ato Conjunto RFB/CGIBS nº 1/2025 e LC 214/2025 (arts. 343, 346, 348).")

    # -------------------------
    # 2) NFS-e E ATO CONJUNTO
    # -------------------------
    with tab2:
        st.subheader("📄 Documentos fiscais recepcionados pelo IBS e pela CBS")
        docs = [
            ["NF-e (modelo 55)", "Mercadorias"],
            ["NFC-e (modelo 65)", "Varejo/consumo"],
            ["NFS-e (padrão nacional)", "Serviços"],
            ["CT-e (modelo 57)", "Transporte"],
            ["CT-e OS (modelo 67)", "Outros serviços de transporte"],
            ["BP-e (modelo 63)", "Bilhete de passagem"],
            ["MDF-e (modelo 58)", "Manifesto de documentos"],
            ["GTV-e (modelo 64)", "Transporte de valores"],
            ["NF3e (modelo 66)", "Energia elétrica"],
            ["NFCom (modelo 62)", "Serviços de comunicação"],
            ["DC-e", "Declaração de conteúdo"],
            ["NFS-e Via", "Exploração de via"],
        ]
        st.table(pd.DataFrame(docs, columns=["Documento", "Uso principal"]))

        st.markdown("**Novos documentos a serem instituídos:**")
        novos_docs = [
            ["NFAg (modelo 75)", "Água e saneamento"],
            ["DeRE", "Declaração de Regimes Específicos"],
            ["NF-e ABI (modelo 77)", "Alienação de bens imóveis"],
            ["NFGas (modelo 76)", "Gás"],
        ]
        st.table(pd.DataFrame(novos_docs, columns=["Documento", "Descrição"]))

        st.markdown("**NFS-e nacional e campos IBS/CBS:** Leiaute padronizado pelo CGNFS-e com grupos específicos para IBS/CBS (DPS e NFS-e). No início de 2026 há tolerância para não preenchimento dos novos campos, sem multa, dentro do período de adaptação.")

        st.caption("Fontes: Ato Conjunto RFB/CGIBS nº 1/2025; Notas Técnicas CGNFS-e (NT 004/2025) – grupos IBS/CBS.")

        st.divider()
        st.subheader("🧱 Leiautes municipais de NFS-e em 2026")
        st.markdown("Alguns municípios anunciaram convivência de dois leiautes:")
        leiautes = [
            ["Layout 1 (atual)", "ISS apenas", "Aceito em 2026 (online/webservice/TXT)"],
            ["Layout 2 (novo)", "ISS + IBS + CBS", "Válido a partir de 01/01/2026"],
        ]
        st.table(pd.DataFrame(leiautes, columns=["Modalidade", "Conteúdo", "Situação 2026"]))
        st.caption("Observação: a adoção do layout com IBS/CBS é recomendada para testes e adaptação; o período inicial pode dispensar penalidades.")

    # -------------------------
    # 3) LINHA DO TEMPO
    # -------------------------
    with tab3:
        st.subheader("📆 Transição (2024–2033): tributos atuais x novos tributos")
        timeline = [
            ["2024", "Sem mudanças", "-"] ,
            ["2025", "Sem mudanças", "-"] ,
            ["2026", "Mantidos ICMS/ISS/PIS/COFINS", "Alíquotas teste: IBS 0,1% e CBS 0,9% (compensáveis/dispensáveis se obrigações acessórias cumpridas)"],
            ["2027", "Início da extinção de PIS/COFINS", "CBS passa a vigorar plenamente (alíquota a ser fixada) com redução de 0,1 p.p nos anos 2027-2028"],
            ["2028", "Conviver com ICMS/ISS", "CBS com redução de 0,1 p.p em relação à referência"],
            ["2029", "Redução progressiva ICMS/ISS (9/10)", "IBS em transição"],
            ["2030", "Redução progressiva ICMS/ISS (8/10)", "IBS em transição"],
            ["2031", "Redução progressiva ICMS/ISS (7/10)", "IBS em transição"],
            ["2032", "Redução progressiva ICMS/ISS (6/10)", "IBS em transição"],
            ["2033", "Extinção completa ICMS/ISS", "Sistema IBS/CBS pleno"],
        ]
        st.table(pd.DataFrame(timeline, columns=["Ano", "Tributos atuais", "Novos tributos (IBS/CBS)"]))
        st.caption("Notas: 2026 é ano informativo com alíquotas de teste; a CBS entra plenamente em 2027; ICMS/ISS reduzem gradualmente até 2033.")

    # -------------------------
    # 4) CALCULADORA – LOCAÇÃO
    # -------------------------
    with tab4:
        st.subheader("🧮 Simulador didático – locação empresarial (exemplo)")
        st.markdown("Parâmetros padrão do exemplo realista (edite conforme seu cenário):")
        colA, colB = st.columns(2)
        with colA:
            aluguel = st.number_input("Aluguel mensal (R$)", min_value=0.0, value=12000.0, step=100.0)
            aliquota_referencial = st.slider("Alíquota referencial IBS+CBS (padrão)", min_value=20.0, max_value=30.0, value=27.0, step=0.1)
            reducao_media = st.slider("Redução média setorial (%)", min_value=0.0, max_value=80.0, value=40.0, step=1.0)
            redutor_social = st.number_input("Redutor Social mensal (R$)", min_value=0.0, value=400.0, step=50.0)
        with colB:
            energia = st.number_input("Energia elétrica (R$)", min_value=0.0, value=1200.0, step=50.0)
            contabilidade = st.number_input("Contabilidade (R$)", min_value=0.0, value=1000.0, step=50.0)
            telecom = st.number_input("Internet + telefone (R$)", min_value=0.0, value=300.0, step=10.0)
            papelaria = st.number_input("Material de escritório (R$)", min_value=0.0, value=150.0, step=10.0)

        # Cálculos
        aliquota_efetiva = aliquota_referencial * (1 - reducao_media/100.0) / 100.0  # em fração
        base_apos_redutor = max(aluguel - redutor_social, 0.0)
        imposto_bruto = base_apos_redutor * aliquota_efetiva
        despesas_total = energia + contabilidade + telecom + papelaria
        creditos = despesas_total * aliquota_efetiva
        imposto_final = max(imposto_bruto - creditos, 0.0)

        # Exibição
        st.markdown("**Passos do cálculo**")
        passos = [
            ["Alíquota efetiva (após redução)", f"{aliquota_referencial:.1f}% × (1 - {reducao_media:.0f}%) = {aliquota_efetiva*100:.2f}%"],
            ["Base após Redutor Social", f"R$ {aluguel:,.2f} - R$ {redutor_social:,.2f} = R$ {base_apos_redutor:,.2f}"],
            ["Imposto bruto", f"R$ {base_apos_redutor:,.2f} × {aliquota_efetiva*100:.2f}% = R$ {imposto_bruto:,.2f}"],
            ["Créditos (despesas × alíquota efetiva)", f"R$ {despesas_total:,.2f} × {aliquota_efetiva*100:.2f}% = R$ {creditos:,.2f}"],
            ["Imposto final (após créditos)", f"R$ {imposto_bruto:,.2f} - R$ {creditos:,.2f} = R$ {imposto_final:,.2f}"],
        ]
        st.table(pd.DataFrame(passos, columns=["Etapa", "Cálculo"]))

        st.success(
            f"Total de impostos estimado após a reforma (parâmetros atuais): **R$ {imposto_final:,.2f}**\n\n"
            "Observação: em 2026, aplica-se a alíquota teste de **CBS 0,9%** e **IBS 0,1%**, com **compensação** junto ao PIS/COFINS do período, sem efeito tributário líquido se as obrigações acessórias forem cumpridas."
        )

        st.caption("Este simulador é ilustrativo e não substitui a análise do regime específico e dos redutores previstos na LC 214/2025.")

    # -------------------------
    # 5) CRÉDITOS PIS/COFINS → CBS
    # -------------------------
    with tab5:
        st.subheader("🔁 Tratamento dos créditos de PIS/COFINS na transição para a CBS")
        st.markdown(
            """
            **Regras principais (LC 214/2025 – Arts. 378 a 383):**
            - **Créditos permanecem válidos** após a extinção de PIS/COFINS (01/01/2027).  
            - Podem ser **usados para compensar a CBS**, e, quando permitido pela legislação anterior, **ressarcidos em dinheiro** ou **compensados** com outros tributos federais.  
            - **Devoluções após 2027** de operações anteriores geram **crédito de CBS**, limitado ao abatimento da própria CBS.  
            - Créditos vinculados a **depreciação/amortização** seguem como **créditos presumidos de CBS**, mantendo condições originais.  
            - **Crédito presumido sobre estoques (01/01/2027)**: bens novos adquiridos no País (ou importados) – uso exclusivo para compensar CBS, em 12 parcelas mensais.  
            - **Ordem de utilização:** preferência para **créditos antigos (PIS/COFINS)** antes dos **créditos da CBS**.  
            """
        )
        regras = [
            ["Validade dos créditos", "Creditos não apropriados/Utilizados continuam válidos"],
            ["Formas de uso", "Compensar CBS; ressarcimento/compensação conforme regras anteriores"],
            ["Devoluções pós-2027", "Geram crédito de CBS para abatimento da própria CBS"],
            ["Imobilizado", "Apropriação continua como crédito presumido de CBS"],
            ["Estoques 01/01/2027", "Crédito presumido (12 parcelas), uso exclusivo na CBS"],
            ["Preferência", "Usar primeiro créditos de PIS/COFINS"],
        ]
        st.table(pd.DataFrame(regras, columns=["Tópico", "Resumo"]))
        st.caption("Atenção à escrituração correta dos créditos na EFD-Contribuições antes da migração.")

    # -------------------------
    # 6) IMAGENS E TABELAS
    # -------------------------
    with tab6:
        st.subheader("🖼️ Use suas imagens para compor o painel")
        st.markdown(
            "Faça upload das imagens com seus quadros/infográficos. Elas serão exibidas ao lado das tabelas reproduzidas no painel.")
        imgs = st.file_uploader("Envie imagens (PNG/JPG)", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
        if imgs:
            for i, img in enumerate(imgs, start=1):
                st.image(img, caption=f"Imagem {i}", use_column_width=True)
        st.info("As tabelas do painel foram construídas com base nas informações consolidadas do seu material e na legislação vigente.")

    # -------------------------
    # RODAPÉ / DOWNLOAD
    # -------------------------
    st.divider()
    st.markdown("**Referências legais e técnicas resumidas no painel**")
    refs = [
        ["Ato Conjunto RFB/CGIBS nº 1/2025", "Documentos recepcionados; tolerância no preenchimento dos campos IBS/CBS; caráter informativo em 2026"],
        ["LC 214/2025 (arts. 343, 346, 348)", "Alíquotas de teste em 2026; dispensa/compensação; exceções ao Simples"],
        ["LC 214/2025 (art. 347)", "Redução de 0,1 p.p na CBS em 2027–2028"],
        ["LC 214/2025 (arts. 378–383)", "Créditos PIS/COFINS – regras de transição e uso na CBS"],
        ["CGNFS-e – NT 004/2025", "Novos grupos/Leiaute da NFS-e para IBS/CBS"],
    ]
    st.table(pd.DataFrame(refs, columns=["Norma", "Assunto"]))

