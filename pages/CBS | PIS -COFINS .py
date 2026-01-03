
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Reforma Tributária – PIS/COFINS",
    page_icon="🟪",
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
    st.markdown(
        "<style>[data-testid='stSidebar']{display:none;}</style>",
        unsafe_allow_html=True
    )

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
    # CSS GLOBAL (FUNDO PRETO)
    # =========================
    st.markdown(
        """
        <style>
            html, body, [class*="css"]  { background-color: #000000; }

            /* Título principal na cor #B91E27 */
            .titulo-principal {
                font-size: 34px;
                font-weight: bold;
                color: #B91E27;
                margin-bottom: 10px;
            }

            /* Subtítulos na cor #D96569 */
            .subtitulo {
                font-size: 22px;
                font-weight: bold;
                color: #D96569;
                margin-top: 30px;
            }

            .texto {
                font-size: 16px;
                color: #dddddd;
                line-height: 1.6;
            }

            .box {
                background-color: #111111;
                padding: 20px;
                border-radius: 12px;
                margin-top: 15px;
                border: 1px solid #2a2a2a;
            }

            /* Tabela comparativa (tema escuro) */
            .tabela {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            .tabela thead th {
                background-color: #6b1f3a; /* vinho */
                color: #ffffff;
                padding: 10px;
                text-align: center;
            }
            .tabela tbody td {
                background-color: #0f0f0f;
                color: #eaeaea;
                padding: 10px;
                text-align: center;
                border-bottom: 1px solid #333333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TÍTULO PRINCIPAL
    # =========================
    st.markdown("<div class='titulo-principal'>PIS e COFINS → CBS</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='texto'>
        Resumo prático da Reforma Tributária aplicado a
        <b>empresas prestadoras de serviços de consultoria e assessoria patrimonial imobiliária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2026 – PERÍODO DE TESTE
    # =========================
    st.markdown("<div class='subtitulo'>📅 Ano de 2026 — Período de Teste</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ Entrada da <b>CBS em fase piloto</b><br>
        ✔ Alíquota teste: <b>0,9%</b><br>
        ✔ Valor recolhido é <b>compensado com PIS e COFINS</b><br>
        ✔ Possível <b>dispensa de recolhimento</b> se cumprir obrigações acessórias<br><br>
        ❗ <b>Não há aumento real de carga tributária em 2026</b>.  
        O objetivo é apenas informativo e de adaptação dos sistemas.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # 2027 EM DIANTE
    # =========================
    st.markdown("<div class='subtitulo'>🚨 A partir de 2027</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ❌ <b>PIS e COFINS são extintos</b><br>
        ✔ Entra a <b>CBS</b> de forma definitiva<br><br>

        <b>Características da CBS:</b><br>
        • Não cumulativa (modelo IVA)<br>
        • Crédito financeiro amplo<br>
        • Alíquota estimada: <b>~8,8%</b><br><br>

        ⚠️ Empresas de serviços com poucos insumos
        tendem a sentir <b>aumento real da carga tributária</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TABELA COMPARATIVA (GERAL)
    # =========================
    st.markdown("<div class='subtitulo'>📊 Comparativo Geral</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <table class="tabela">
            <thead>
                <tr>
                    <th>Período</th>
                    <th>Tributo</th>
                    <th>Alíquota</th>
                    <th>Crédito</th>
                    <th>Impacto Financeiro</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Até 2025</td>
                    <td>PIS + COFINS</td>
                    <td>3,65%</td>
                    <td>Não</td>
                    <td>Baixo</td>
                </tr>
                <tr>
                    <td>2026</td>
                    <td>CBS (teste)</td>
                    <td>0,9%</td>
                    <td>Sim (compensado)</td>
                    <td>Neutro</td>
                </tr>
                <tr>
                    <td>2027+</td>
                    <td>CBS definitiva</td>
                    <td>~8,8%</td>
                    <td>Sim (pleno)</td>
                    <td>Mais elevado</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # CONCLUSÃO
    # =========================
    st.markdown("<div class='subtitulo'>🧾 Conclusão Prática</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box texto'>
        ✔ 2026 é um ano de adaptação<br>
        ✔ A mudança financeira começa em 2027<br>
        ✔ Revisão de preços e contratos será essencial para serviços
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # TABELA FINAL — IDÊNTICA AO PRINT (SEM LINHAS INTERNAS)
    # Implementada com CSS GRID para controlar bordas dos blocos
    # ==========================================================
    st.markdown("<div class='subtitulo'>🗂️ Tabela – Linha do Tempo</div>", unsafe_allow_html=True)

    html_grid = """
    <style>
      .grid-table {
        display: grid;
        /* 4 colunas com as mesmas larguras do seu print */
        grid-template-columns: 10% 22% 22% 46%;
        /* 2 linhas de cabeçalho + 10 linhas dos anos (2024–2033) */
        grid-template-rows:
          48px   /* header 1 */
          48px   /* header 2 */
          repeat(10, 56px); /* cada ano */
        width: 100%;
        background: #ffffff;
        font-family: Arial, Helvetica, sans-serif;
        border: 1px solid #d6d6d6; /* borda externa da tabela */
        box-sizing: border-box;
      }
      .cell {
        padding: 12px 10px;
        color: #222;
        background: #fff;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        border: 1px solid #d6d6d6;       /* borda padrão */
        box-sizing: border-box;
      }
      .center { justify-content: center; text-align: center; }
      .muted  { color: #3b3b3b; }

      /* Cabeçalho (azul claro) */
      .header { background: #cfe0f1; font-weight: 700; }

      /* Remover bordas duplicadas da moldura externa */
      .no-border { border: none; }

      /* ====== BLOCO PIS/PASEP 2027–2033 (sem linhas internas) ====== */
      .pis-block {
        grid-column: 2 / 3;   /* segunda coluna (PIS/PASEP) */
        grid-row: 3 + 4 / span 7; /* inicia na linha do ano 2027; span 7 anos (2027–2033) */
        /* Como não temos cálculo aqui, vamos posicionar com números absolutos: */
      }
      /* OBS: Vamos posicionar explicitamente sem usar '3 + 4':
         Cabeçalho ocupa rows 1 e 2; 2024 é row 3; então:
         2024 -> row 3
         2025 -> row 4
         2026 -> row 5
         2027 -> row 6
         2028 -> row 7
         2029 -> row 8
         2030 -> row 9
         2031 -> row 10
         2032 -> row 11
         2033 -> row 12
      */

      /* Reposicionamento manual */
      .r1  { grid-row: 1; }
      .r2  { grid-row: 2; }
      .r3  { grid-row: 3; }  /* 2024 */
      .r4  { grid-row: 4; }  /* 2025 */
      .r5  { grid-row: 5; }  /* 2026 */
      .r6  { grid-row: 6; }  /* 2027 */
      .r7  { grid-row: 7; }  /* 2028 */
      .r8  { grid-row: 8; }  /* 2029 */
      .r9  { grid-row: 9; }  /* 2030 */
      .r10 { grid-row: 10; } /* 2031 */
      .r11 { grid-row: 11; } /* 2032 */
      .r12 { grid-row: 12; } /* 2033 */

      .c1 { grid-column: 1; } /* Ano */
      .c2 { grid-column: 2; } /* PIS/PASEP */
      .c3 { grid-column: 3; } /* COFINS */
      .c4 { grid-column: 4; } /* CBS */

      /* BLOCO PIS (grande) 2027–2033 */
      .pis-merge {
        grid-column: 2;
        grid-row: 6 / span 7; /* 2027–2033 */
        border: 1px solid #d6d6d6;
      }

      /* BLOCO CBS #1 (2027–2028) com texto */
      .cbs-merge-1 {
        grid-column: 4;
        grid-row: 6 / span 2; /* 2027–2028 */
        border: 1px solid #d6d6d6;
      }

      /* BLOCO CBS #2 (2029–2030) vazio */
      .cbs-merge-2 {
        grid-column: 4;
        grid-row: 8 / span 2; /* 2029–2030 */
        border: 1px solid #d6d6d6;
      }

      /* BLOCO CBS #3 (2031–2033) com texto */
      .cbs-merge-3 {
        grid-column: 4;
        grid-row: 10 / span 3; /* 2031–2033 */
        border: 1px solid #d6d6d6;
      }

      /* Células "normais" (sem mesclagem) — anos e COFINS, etc. */
      .year { justify-content: center; }
    </style>

    <div class="grid-table">

      <!-- Cabeçalho linha 1 -->
      <div class="cell header r1 c1 center">Ano</div>
      <div class="cell header r1" style="grid-column: 2 / span 2; justify-content:center;">Tributos Atuais</div>
      <div class="cell header r1 c4 center">Novos Tributos</div>

      <!-- Cabeçalho linha 2 -->
      <div class="cell header r2 c1"></div>
      <div class="cell header r2 c2 center">PIS/PASEP</div>
      <div class="cell header r2 c3 center">COFINS</div>
      <div class="cell header r2 c4 center">CBS</div>

      <!-- Coluna Ano -->
      <div class="cell year r3 c1">2024</div>
      <div class="cell year r4 c1">2025</div>
      <div class="cell year r5 c1">2026</div>
      <div class="cell year r6 c1">2027</div>
      <div class="cell year r7 c1">2028</div>
      <div class="cell year r8 c1">2029</div>
      <div class="cell year r9 c1">2030</div>
      <div class="cell year r10 c1">2031</div>
      <div class="cell year r11 c1">2032</div>
      <div class="cell year r12 c1">2033</div>

      <!-- PIS/PASEP: bloco mesclado 2027–2033 (vazio) -->
      <div class="cell pis-merge"></div>

      <!-- COFINS (células padrão) -->
      <div class="cell r3 c3"></div>
      <div class="cell r4 c3 muted center">Sem mudanças</div>
      <div class="cell r5 c3 muted center">Alíquotas mantidas; com a possibilidade de compensação de 1% dos novos tributos (CBS 0,9% e IBS 0,1%).</div>
      <div class="cell r6 c3"></div>
      <div class="cell r7 c3"></div>
      <div class="cell r8 c3"></div>
      <div class="cell r9 c3 muted center">Extinção</div>
      <div class="cell r10 c3"></div>
      <div class="cell r11 c3"></div>
      <div class="cell r12 c3"></div>

      <!-- CBS: 2024–2026 individuais -->
      <div class="cell r3 c4"></div>
      <div class="cell r4 c4 center">-</div>
      <div class="cell r5 c4 muted center">Alíquota teste: 0,9%</div>

      <!-- CBS: bloco #1 (2027–2028) -->
      <div class="cell cbs-merge-1 muted center">Alíquota estabelecida (-) 0,1%</div>

      <!-- CBS: bloco #2 (2029–2030) vazio -->
      <div class="cell cbs-merge-2"></div>

      <!-- CBS: bloco #3 (2031–2033) -->
      <div class="cell cbs-merge-3 muted center">Alíquota estabelecida</div>

    </div>
    """

    # Renderização via HTML puro (CSS Grid) — sem linhas internas nos blocos
    components.html(html_grid, height=820, scrolling=True)
