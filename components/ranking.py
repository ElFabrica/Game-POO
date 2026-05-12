"""
=============================================================
  PAGE: streamlit_app/pages/ranking.py
  Página pública do ranking — consome a API FastAPI
=============================================================
"""

import streamlit as st
import urllib.request
import urllib.error
import json

st.set_page_config(page_title="Ranking · CodeMemory", page_icon="🏆", layout="wide")

API_URL = "http://localhost:8000"

MEDAL = {1: "🥇", 2: "🥈", 3: "🥉"}


def fetch_ranking(limit: int = 20) -> list[dict] | None:
    try:
        url = f"{API_URL}/ranking/list?limit={limit}"
        with urllib.request.urlopen(url, timeout=5) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


# ── Header ───────────────────────────────────────────────────
st.markdown("""
    <h1 style='font-size:2.4rem;font-weight:800;color:#e8e8f0;margin-bottom:4px'>
        🏆 Ranking Global
    </h1>
    <p style='color:#7a7a90;font-size:0.9rem;margin-bottom:32px'>
        Pontuações salvas em tempo real no Google Sheets
    </p>
""", unsafe_allow_html=True)

# ── Fetch ────────────────────────────────────────────────────
with st.spinner("Carregando ranking..."):
    entries = fetch_ranking()

if entries is None:
    st.error("⚠️ Backend offline. Rode: `uvicorn backend.main:app --port 8000`")
    st.stop()

if not entries:
    st.info("Nenhuma partida registrada ainda. Seja o primeiro a jogar!")
    st.stop()

# ── Métricas top 3 ───────────────────────────────────────────
top = entries[:3]
cols = st.columns(len(top), gap="medium")

for i, (col, entry) in enumerate(zip(cols, top)):
    with col:
        medal = MEDAL.get(i + 1, "")
        st.metric(
            label=f"{medal} {entry['name']}",
            value=f"{entry['score']:,} pts",
            delta=f"{entry['accuracy']}% precisão",
        )

st.divider()

# ── Tabela completa ──────────────────────────────────────────
st.markdown("### Todos os jogadores")

header = st.columns([0.5, 2, 1.2, 1, 1, 1, 1.5, 2])
labels = ["#", "Nome", "Pontos", "Pares", "Erros", "Precisão", "Tempo", "Data"]
for col, label in zip(header, labels):
    col.markdown(f"**{label}**")

st.markdown("<hr style='margin:6px 0;border-color:#252530'>", unsafe_allow_html=True)

for entry in entries:
    pos    = entry["position"]
    medal  = MEDAL.get(pos, "")
    color  = "#ffd700" if pos == 1 else ("#c0c0c0" if pos == 2 else ("#cd7f32" if pos == 3 else "#e8e8f0"))
    row    = st.columns([0.5, 2, 1.2, 1, 1, 1, 1.5, 2])

    row[0].markdown(f"<span style='color:{color};font-weight:700'>{medal}{pos}</span>", unsafe_allow_html=True)
    row[1].markdown(f"<span style='color:{color};font-weight:{'700' if pos<=3 else '400'}'>{entry['name']}</span>", unsafe_allow_html=True)
    row[2].markdown(f"<span style='color:{color};font-weight:700'>{entry['score']:,}</span>", unsafe_allow_html=True)
    row[3].write(entry["pairs"])
    row[4].write(entry["errors"])
    row[5].write(f"{entry['accuracy']}%")
    row[6].write(entry["time"])
    row[7].markdown(f"<span style='color:#7a7a90;font-size:0.85rem'>{entry['date']}</span>", unsafe_allow_html=True)

# ── Atualizar ────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔄 Atualizar ranking"):
    st.rerun()
