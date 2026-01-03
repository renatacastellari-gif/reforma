
import streamlit as st
from pathlib import Path
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

    # ---- Título enxuto ----
    st.markdown(
        "<h2 style='color:#B22222;font-family:Times New Roman,sans-serif;font-weight:700;"
        "text-align:center;border-bottom:2px solid #B22222;padding-bottom:8px;margin-bottom:20px;'>"
        "Reforma Tributária – IBS/CBS (Serviços/Empresa Patrimonial)</h2>",
        unsafe_allow_html=True
    )

    # =========================
    # TEXTO PRINCIPAL (sem a palavra 'didático')
    # =========================
    st.markdown("""
📘 **RESUMO – REFORMA TRIBUTÁRIA (IBS/CBS) PARA EMPRESA PATRIMONIAL / SERVIÇOS**

### ✅ 1. O que muda para quem presta serviços (consultoria, assessoria)
**A partir de 2026**, toda empresa que presta serviços deve:
- Continuar emitindo **NFS‑e** (padrão nacional).
- Começar a visualizar **campos de IBS e CBS** na nota.
- **Sem multa** se você não preencher esses campos nos primeiros meses.
- **Sem pagamento de IBS/CBS em 2026.**

**Resumo simples:**
- Você continua emitindo a mesma **NFS‑e**.
- **2026 é só teste**, sem aumento de custo tributário.
- O governo quer apenas **receber as informações**.

### ✅ 2. Por que existe a fase “de teste” em 2026?
Para que os sistemas nacionais (Receita Federal + Comitê do IBS) possam:
- Testar comunicação das notas;
- Testar cálculo automático;
- Conferir se o leiaute funciona.

Por isso:
- **CBS = 0,9%**
- **IBS = 0,1%**

**Esse 1% é compensado** com **PIS/COFINS**; e conforme art. 348, §1º da LC 214/2025, **pode haver dispensa de recolhimento** em 2026 para quem **cumprir obrigações acessórias**.
**Na prática:** você **não paga nada a mais** em 2026.

### ✅ 3. O que muda de verdade só começa em 2027
A partir de **1º de janeiro de 2027**:
- **PIS + COFINS** deixam de existir;
- Entra a **CBS**, com alíquota estimada em **~8,8%**;
- Continua o **IBS** (mais relevante para municípios/estados).

Para quem presta **serviços puros** (consultoria, assessoria, administração, holdings patrimoniais):
- O **impacto tende a ser maior**, porque esse setor tem **poucos créditos** para descontar.
- A **alíquota aumenta** porque o modelo novo é **não cumulativo** e serviços têm **pouco crédito** a abater.

### ✅ 4. Por que a alíquota "sobe" (ex.: de **3,65%** → **~8,8%**)?
- O **PIS/COFINS** atual (**3,65%**) é **cumulativo** → tributa a **receita bruta** inteira.
- A **CBS** (**~8,8%**) é **não cumulativa** → tributa **valor agregado**.
- Setor de **serviços** tem pouco **insumo** → **crédito** quase **zero**.

**Conclusão:** a alíquota sobe porque o **crédito** do modelo novo é **baixo** para empresas de serviço.

### ✅ 5. O que uma empresa patrimonial realmente precisa saber
**2026**
- Continua emitindo **NFS‑e**;
- **IBS/CBS** não geram pagamento real;
- Sem **multa** pelo não preenchimento imediato;
- Obrigação é **somente informativa**.

**2027**
- **Acaba PIS/COFINS**;
- Entra a **CBS**;
- Serviços tendem a **pagar mais imposto**, porque não geram crédito;
- **IBS** também entra no cálculo (depende do tipo de serviço/atividade).

### ✅ 6. Créditos de PIS/COFINS
Se a empresa tiver **créditos acumulados**:
- Eles **não desaparecem**;
- Podem ser usados para **abater a CBS**;
- Podem ser **ressarcidos ou compensados**;
- Créditos por **depreciação** continuam como **crédito presumido de CBS**.

Isso **protege** quem acumulou crédito no regime antigo.

### 🔎 Resumo final em 30 segundos
- **2026:** muda nada no bolso → tudo **informativo**;
- **2027:** acaba **PIS/COFINS**; começa **CBS**;
- Em **serviços puros**, a carga **federal tende a subir**;
- Emissão continua sendo **NFS‑e**;
- Campos de **IBS/CBS** ficam **obrigatórios**;
- **Créditos antigos** continuam **válidos**.
""")

    # =========================
    # TABELA (exatamente como enviada)
    # =========================
    st.markdown("\n---\n\n**Tabela – Transição PIS/COFINS → CBS (SERVIÇOS)**")

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

    # Cabeçalho visual
    st.table(df)

