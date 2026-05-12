"""
=============================================================
  COMPONENT: streamlit_app/components/value_prop.py
  Seção "Por que CodeMemory?" — cards de proposta de valor
=============================================================
"""

import streamlit as st
import streamlit_shadcn_ui as ui


def render():
    st.markdown("""
        <p style='color:#5b8dee;font-size:0.72rem;font-weight:600;
                  letter-spacing:0.18em;text-transform:uppercase;
                  font-family:monospace;margin-bottom:24px'>
            // Por que CodeMemory?
        </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with ui.card(key="vp1"):
            ui.element("div", children=[
                ui.element("p", children=["3×"], className="text-4xl font-bold text-blue-400 mb-2", key="vp1_num"),
                ui.element("h4", children=["Mais retenção"], className="text-sm font-semibold uppercase tracking-wide text-white mb-1", key="vp1_title"),
                ui.element("p", children=["Memória ativa por associação é comprovadamente mais eficaz do que leitura passiva de documentação."], className="text-xs text-gray-400 leading-relaxed", key="vp1_text"),
            ], key="vp1_inner")

    with col2:
        with ui.card(key="vp2"):
            ui.element("div", children=[
                ui.element("p", children=["12"], className="text-4xl font-bold text-purple-400 mb-2", key="vp2_num"),
                ui.element("h4", children=["Linguagens reais"], className="text-sm font-semibold uppercase tracking-wide text-white mb-1", key="vp2_title"),
                ui.element("p", children=["Python, JS, TypeScript, Rust, Go, Java, C++, Swift, Kotlin, Ruby, PHP e Dart — linguagens do mercado."], className="text-xs text-gray-400 leading-relaxed", key="vp2_text"),
            ], key="vp2_inner")

    with col3:
        with ui.card(key="vp3"):
            ui.element("div", children=[
                ui.element("p", children=["0"], className="text-4xl font-bold text-green-400 mb-2", key="vp3_num"),
                ui.element("h4", children=["Barreiras de entrada"], className="text-sm font-semibold uppercase tracking-wide text-white mb-1", key="vp3_title"),
                ui.element("p", children=["Sem cadastro, sem instalador complexo. Roda com python main.py em qualquer sistema operacional."], className="text-xs text-gray-400 leading-relaxed", key="vp3_text"),
            ], key="vp3_inner")
