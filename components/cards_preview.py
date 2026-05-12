"""
=============================================================
  COMPONENT: streamlit_app/components/cards_preview.py
  Preview visual das cartas de linguagem
=============================================================
"""

import streamlit as st


CARDS = [
    {"icon": "🐍", "name": "Python",     "color": "#3574a5", "flipped": False},
    {"icon": "⚡", "name": "JavaScript", "color": "#f0db4f", "flipped": True},
    {"icon": "🔷", "name": "TypeScript", "color": "#3178c6", "flipped": False},
    {"icon": "🦀", "name": "Rust",       "color": "#ce5821", "flipped": True},
    {"icon": "🐹", "name": "Go",         "color": "#00add8", "flipped": False},
    {"icon": "☕", "name": "Java",       "color": "#ed751a", "flipped": True},
    {"icon": "⚙️", "name": "C++",        "color": "#00599d", "flipped": False},
    {"icon": "🍎", "name": "Swift",      "color": "#f05138", "flipped": True},
    {"icon": "🎯", "name": "Kotlin",     "color": "#7f52ff", "flipped": False},
    {"icon": "💎", "name": "Ruby",       "color": "#a81111", "flipped": True},
    {"icon": "🐘", "name": "PHP",        "color": "#777bb4", "flipped": False},
    {"icon": "🎯", "name": "Dart",       "color": "#00b4d8", "flipped": True},
]

BACK_STYLE = """
    background: #1a1a22;
    border: 1px solid #252530;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    height: 90px;
    font-size: 1.6rem;
    color: #3a3a48;
"""


def render():
    st.markdown("""
        <p style='color:#7a7a90;font-size:0.72rem;font-weight:600;
                  letter-spacing:0.18em;text-transform:uppercase;
                  font-family:monospace;margin-bottom:20px'>
            // Preview das cartas
        </p>
    """, unsafe_allow_html=True)

    cols = st.columns(6, gap="small")

    for i, card in enumerate(CARDS):
        with cols[i % 6]:
            if card["flipped"]:
                st.markdown(f"""
                    <div style='{BACK_STYLE}'>?</div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style='
                        background: {card["color"]}18;
                        border: 1px solid {card["color"]}55;
                        border-radius: 8px;
                        height: 90px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        gap: 6px;
                        transition: transform 0.2s;
                    '>
                        <span style='font-size:1.5rem'>{card["icon"]}</span>
                        <span style='font-size:0.55rem;color:#7a7a90;
                                     text-transform:uppercase;letter-spacing:0.1em;
                                     font-family:monospace'>
                            {card["name"]}
                        </span>
                    </div>
                """, unsafe_allow_html=True)
