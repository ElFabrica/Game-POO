"""
=============================================================
  COMPONENT: streamlit_app/components/hero.py
  Seção Hero — título principal e botão de iniciar o jogo
=============================================================
"""
import streamlit as st
import streamlit_shadcn_ui as ui


def render(game_root: str = ""):
    ui.badges(badge_list=[("Projeto Acadêmico · Python · 2026", "secondary")], class_name="mb-2", key="hero_tag")
    st.markdown("""
        <p style='color:#7a7a90;font-size:0.85rem;margin-bottom:4px;letter-spacing:0.06em;font-family:monospace'>
            Aprenda programação
        </p>
        <h1 style='font-size:clamp(2.4rem,6vw,4rem);font-weight:800;line-height:1.05;color:#e8e8f0;margin-bottom:0'>
            Jogando a <span style='color:#5b8dee'>memória.</span>
        </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='color:#7a7a90;font-size:0.95rem;max-width:520px;line-height:1.85;margin:18px 0 36px'>
            Um jogo da memória onde os pares são linguagens de programação reais.
            Compete com outros jogadores e sobe no ranking global salvo no Google Drive.
        </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        play = ui.button("▶  Jogar agora", key="btn_play", class_name="w-full")
    with col2:
        ui.link_button(text="Ver no GitHub", url="https://github.com/ElFabrica/Game-POO", key="btn_gh", variant="outline")

    if play:
        st.switch_page("pages/jogo.py")
