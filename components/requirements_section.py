"""
=============================================================
  COMPONENT: streamlit_app/components/requirements_section.py
  Seção de requisitos técnicos do projeto
=============================================================
"""

import streamlit as st
import streamlit_shadcn_ui as ui


REQS = [
    ("Linguagem",    "Python 3.10+"),
    ("Jogo",         "pygame + Pillow"),
    ("Backend",      "FastAPI + uvicorn"),
    ("Ranking",      "Google Sheets API"),
    ("Plataformas",  "Win · macOS · Linux"),
    ("Licença",      "MIT"),
    ("Frontend",     "Streamlit"),
    ("Auth",         "OAuth2 Google"),
]


def render():
    st.markdown("""
        <p style='color:#7a7a90;font-size:0.72rem;font-weight:600;
                  letter-spacing:0.18em;text-transform:uppercase;
                  font-family:monospace;margin-bottom:20px'>
            // Requisitos técnicos
        </p>
    """, unsafe_allow_html=True)

    cols = st.columns(4, gap="small")

    for i, (key, val) in enumerate(REQS):
        with cols[i % 4]:
            st.markdown(f"""
                <div style='
                    background:#131318;
                    border:1px solid #252530;
                    border-radius:8px;
                    padding:18px 16px;
                    margin-bottom:8px;
                '>
                    <p style='color:#3a3a48;font-size:0.62rem;font-weight:600;
                              letter-spacing:0.14em;text-transform:uppercase;
                              font-family:monospace;margin-bottom:4px'>{key}</p>
                    <p style='color:#e8e8f0;font-size:0.85rem;margin:0;
                              font-family:monospace'>{val}</p>
                </div>
            """, unsafe_allow_html=True)
