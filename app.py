"""
=============================================================
MODULE: app.py
Landing Page principal do CodeMemory — streamlit-shadcn-ui
Rodar: streamlit run app.py
=============================================================
"""
import os
import sys

# ── Resolve paths para funcionar local e no Streamlit Cloud ──
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(THIS_DIR)

for p in [THIS_DIR, ROOT_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

import streamlit as st

# ── Configuração da página ───────────────────────────────────
st.set_page_config(
    page_title="CodeMemory — Jogo da Memória de Programação",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Redireciona se algum componente pediu navegação ──────────
if st.session_state.get("_goto"):
    dest = st.session_state.pop("_goto")
    st.switch_page(dest)

# ── Estilos globais ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Exo+2:wght@300;400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0c0c0f !important;
    color: #e8e8f0 !important;
}

[data-testid="stSidebar"] { background-color: #131318 !important; }
.block-container { max-width: 960px !important; padding: 2rem 2rem !important; }
h1, h2, h3, h4 { color: #e8e8f0 !important; font-family: 'Rajdhani', sans-serif !important; }
hr { border-color: #252530 !important; margin: 48px 0 !important; }

[data-testid="metric-container"] {
    background: #131318;
    border: 1px solid #252530;
    border-radius: 8px;
    padding: 16px;
}
[data-testid="stMetricValue"] { color: #5b8dee !important; }
[data-testid="stMetricLabel"] { color: #7a7a90 !important; }

.stButton > button {
    background: #5b8dee !important;
    border: none !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0 24px;
    border-bottom: 1px solid #252530;
    margin-bottom: 48px;
}
.nav-logo {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #e8e8f0;
}
.nav-logo span { color: #5b8dee; }

.footer-bar {
    border-top: 1px solid #252530;
    margin-top: 60px;
    padding-top: 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-text {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #3a3a48;
}
</style>
""", unsafe_allow_html=True)

# ── Imports dos componentes ──────────────────────────────────
from components.hero               import render as render_hero
from components.value_prop         import render as render_value_prop
from components.cards_preview      import render as render_cards
from components.about              import render as render_about
from components.requirements_section import render as render_requirements

# ── NAV ─────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
    <span class="nav-logo">Code<span>Memory</span></span>
    <div style="display:flex;gap:32px">
        <a href="#" style="font-family:'Rajdhani',sans-serif;font-size:0.82rem;
            letter-spacing:0.1em;text-transform:uppercase;
            color:#7a7a90;text-decoration:none">Proposta</a>
        <a href="#" style="font-family:'Rajdhani',sans-serif;font-size:0.82rem;
            letter-spacing:0.1em;text-transform:uppercase;
            color:#7a7a90;text-decoration:none">Sobre</a>
        <a href="https://github.com/ElFabrica/Game-POO" target="_blank"
            style="font-family:'Rajdhani',sans-serif;font-size:0.82rem;
            letter-spacing:0.1em;text-transform:uppercase;
            color:#7a7a90;text-decoration:none">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────
render_hero(game_root=THIS_DIR)

st.markdown("<hr>", unsafe_allow_html=True)

# ── PROPOSTA DE VALOR ────────────────────────────────────────
render_value_prop()

st.markdown("<hr>", unsafe_allow_html=True)

# ── CARDS PREVIEW ────────────────────────────────────────────
render_cards()

st.markdown("<hr>", unsafe_allow_html=True)

# ── SOBRE ────────────────────────────────────────────────────
render_about()

st.markdown("<hr>", unsafe_allow_html=True)

# ── REQUISITOS ───────────────────────────────────────────────
render_requirements()

# ── FOOTER ───────────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
    <span class="footer-text">CodeMemory &copy; 2026 &ensp;·&ensp; Projeto acadêmico</span>
    <span class="footer-text">
        <a href="https://github.com/ElFabrica/Game-POO" style="color:#3a3a48;text-decoration:none">GitHub</a>
    </span>
</div>
""", unsafe_allow_html=True)
