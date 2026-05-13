"""
=============================================================
  COMPONENT: streamlit_app/components/about.py
  Seção Sobre o projeto + lista de features
=============================================================
"""
import streamlit as st
import streamlit_shadcn_ui as ui

FEATURES = [
    ("01", "Linguagens do mercado",   "12 linguagens reais: Python, JS, TS, Rust, Go, Java, C++, Swift, Kotlin, Ruby, PHP e Dart."),
    ("02", "Ranking global",          "Pontuação salva automaticamente no Google Sheets. Veja onde você está entre todos os jogadores."),
    ("03", "Modo cronometrado",       "Pontuação por tempo e precisão — quanto mais rápido e certeiro, maior a pontuação."),
    ("04", "Open source · MIT",       "Código público, comentado e extensível. Perfeito como material de estudo de POO."),
]

def render():
    st.markdown("""
        <p style='color:#7a7a90;font-size:0.72rem;font-weight:600;
                  letter-spacing:0.18em;text-transform:uppercase;
                  font-family:monospace;margin-bottom:16px'>
            // Sobre o projeto
        </p>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown("""
            <h2 style='font-size:2rem;font-weight:800;color:#e8e8f0;
                       line-height:1.15;margin-bottom:16px'>
                Fixar conceitos<br>sem perceber.
            </h2>
            <p style='color:#7a7a90;font-size:0.9rem;line-height:1.9;margin-bottom:12px'>
                CodeMemory é desenvolvido em Python orientado a objetos com Pygame.
                O ranking é centralizado no Google Sheets, acessível por qualquer jogador.
            </p>
            <p style='color:#7a7a90;font-size:0.9rem;line-height:1.9'>
                O código é aberto, comentado e serve como material de estudo
                sobre POO, máquinas de estado e design de jogos.
            </p>
        """, unsafe_allow_html=True)

    with col_right:
        for num, title, desc in FEATURES:
            with ui.card(key=f"feat_{num}"):
                ui.element("span", children=[num], className="text-xs text-gray-600 font-mono", key=f"fn_{num}")
                ui.element("h4", children=[title], className="text-sm font-semibold uppercase tracking-wide text-white mt-1 mb-1", key=f"ft_{num}")
                ui.element("p", children=[desc], className="text-xs text-gray-400 leading-relaxed", key=f"fd_{num}")
