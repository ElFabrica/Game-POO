"""
Memory Game — Linguagens de Programação
Landing page + jogo embutido via st.components.v1.html

Rodar:
    streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Memory Game — Linguagens",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #root > div:first-child { padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header, footer { display: none !important; }
    [data-testid="stAppViewContainer"] { background: #080818; }
</style>
""", unsafe_allow_html=True)

FULL_HTML = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Memory Game — Linguagens de Programação</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:        #080818;
    --surface:   #0f0f2a;
    --surface2:  #13132e;
    --border:    #1e2048;
    --border2:   #2a2d6a;
    --primary:   #6366f1;
    --primary2:  #818cf8;
    --accent:    #a855f7;
    --success:   #22c55e;
    --danger:    #ef4444;
    --warning:   #f59e0b;
    --text:      #e2e8ff;
    --muted:     #4a5080;
    --muted2:    #6b7280;
    --gold:      #ffd700;
    --glow:      rgba(99,102,241,0.4);
    --glow2:     rgba(168,85,247,0.3);
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Rajdhani', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── Partículas ── */
  #particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
  .particle {
    position: absolute;
    background: var(--primary);
    border-radius: 50%;
    animation: float-up linear infinite;
    opacity: 0;
  }
  @keyframes float-up {
    0%   { transform: translateY(100vh) scale(0); opacity: 0; }
    10%  { opacity: 0.5; }
    90%  { opacity: 0.2; }
    100% { transform: translateY(-40px) scale(1.5); opacity: 0; }
  }

  /* ═══════════════════════════════════
     LANDING PAGE
  ═══════════════════════════════════ */
  #landing {
    position: relative; z-index: 1;
    min-height: 100vh;
    display: flex; flex-direction: column;
  }

  /* ── Nav ── */
  nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 48px;
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(12px);
    background: rgba(8,8,24,0.7);
    position: sticky; top: 0; z-index: 100;
  }
  .nav-logo {
    font-family: 'Orbitron', monospace;
    font-size: 1rem; font-weight: 900;
    letter-spacing: 0.15em;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .nav-badge {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem; letter-spacing: 0.1em;
    color: var(--muted2);
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 4px 12px; border-radius: 20px;
  }

  /* ── Hero ── */
  .hero {
    flex: 1;
    display: flex; flex-direction: column; align-items: center;
    justify-content: center;
    padding: 80px 24px 60px;
    text-align: center;
    position: relative;
  }

  /* Grade decorativa de fundo */
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background-image:
      linear-gradient(var(--border) 1px, transparent 1px),
      linear-gradient(90deg, var(--border) 1px, transparent 1px);
    background-size: 48px 48px;
    opacity: 0.3;
    mask-image: radial-gradient(ellipse 80% 60% at 50% 50%, black, transparent);
  }

  /* Orbe brilhante */
  .hero-orb {
    width: 320px; height: 320px;
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, rgba(168,85,247,0.08) 40%, transparent 70%);
    border-radius: 50%;
    animation: orb-pulse 4s ease-in-out infinite;
    pointer-events: none;
  }
  @keyframes orb-pulse {
    0%, 100% { transform: translate(-50%,-50%) scale(1); opacity: 0.8; }
    50%       { transform: translate(-50%,-50%) scale(1.15); opacity: 1; }
  }

  .hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem; letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--primary2);
    border: 1px solid rgba(99,102,241,0.35);
    background: rgba(99,102,241,0.08);
    padding: 6px 16px; border-radius: 20px;
    margin-bottom: 28px;
    position: relative; z-index: 1;
    animation: fade-down 0.6s ease both;
  }

  .hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.8rem, 7vw, 5.5rem);
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.01em;
    background: linear-gradient(160deg, #ffffff 0%, #a5b4fc 40%, #c084fc 70%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 40px rgba(99,102,241,0.5));
    margin-bottom: 12px;
    position: relative; z-index: 1;
    animation: fade-down 0.7s 0.1s ease both;
  }

  .hero-title span {
    display: block;
    font-size: 0.45em;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 6px;
    filter: none;
  }

  .hero-desc {
    font-size: clamp(1rem, 2.5vw, 1.25rem);
    color: var(--muted2);
    max-width: 520px;
    line-height: 1.7;
    letter-spacing: 0.03em;
    margin: 20px 0 40px;
    position: relative; z-index: 1;
    animation: fade-down 0.7s 0.2s ease both;
  }

  .hero-cta {
    display: flex; gap: 16px; flex-wrap: wrap; justify-content: center;
    position: relative; z-index: 1;
    animation: fade-down 0.7s 0.3s ease both;
  }

  .cta-primary {
    display: flex; align-items: center; gap: 10px;
    height: 60px; padding: 0 36px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border: 1px solid rgba(99,102,241,0.6);
    border-radius: 12px;
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem; font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #fff;
    cursor: pointer;
    transition: all 0.25s;
    position: relative; overflow: hidden;
  }
  .cta-primary::after {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, transparent 40%, rgba(255,255,255,0.12));
    opacity: 0; transition: opacity 0.2s;
  }
  .cta-primary:hover { transform: translateY(-3px); box-shadow: 0 12px 40px rgba(99,102,241,0.5); }
  .cta-primary:hover::after { opacity: 1; }
  .cta-primary:active { transform: translateY(-1px); }

  .cta-secondary {
    display: flex; align-items: center; gap: 10px;
    height: 60px; padding: 0 32px;
    background: transparent;
    border: 1px solid var(--border2);
    border-radius: 12px;
    font-family: 'Orbitron', monospace;
    font-size: 0.8rem; font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted2);
    cursor: pointer;
    transition: all 0.25s;
  }
  .cta-secondary:hover { border-color: var(--primary); color: var(--text); background: rgba(99,102,241,0.08); }

  @keyframes fade-down {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── Counters ── */
  .hero-stats {
    display: flex; gap: 48px; flex-wrap: wrap; justify-content: center;
    margin-top: 64px;
    position: relative; z-index: 1;
    animation: fade-down 0.7s 0.4s ease both;
  }
  .hero-stat { text-align: center; }
  .hero-stat-value {
    font-family: 'Orbitron', monospace;
    font-size: 2rem; font-weight: 900;
    background: linear-gradient(135deg, var(--gold), #ffa500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-stat-label {
    font-size: 0.7rem; letter-spacing: 0.2em;
    text-transform: uppercase; color: var(--muted);
    margin-top: 4px;
  }

  /* ── Features ── */
  .features {
    padding: 80px 24px;
    position: relative; z-index: 1;
  }
  .features-inner { max-width: 860px; margin: 0 auto; }
  .section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem; letter-spacing: 0.35em;
    text-transform: uppercase; color: var(--primary2);
    text-align: center; margin-bottom: 12px;
  }
  .section-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.4rem, 3.5vw, 2.2rem);
    font-weight: 700; text-align: center;
    letter-spacing: 0.04em;
    margin-bottom: 48px;
  }

  .feat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
  }
  .feat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 24px;
    transition: all 0.25s;
    position: relative; overflow: hidden;
  }
  .feat-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--card-accent, linear-gradient(90deg, #6366f1, #a855f7));
    opacity: 0; transition: opacity 0.25s;
  }
  .feat-card:hover { transform: translateY(-4px); border-color: var(--border2); }
  .feat-card:hover::before { opacity: 1; }

  .feat-icon {
    font-size: 1.8rem; margin-bottom: 16px;
    display: flex; align-items: center; justify-content: center;
    width: 52px; height: 52px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
  }
  .feat-title {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem; font-weight: 700;
    letter-spacing: 0.08em; margin-bottom: 8px;
  }
  .feat-desc { font-size: 0.9rem; color: var(--muted2); line-height: 1.6; }

  /* ── Dificuldades preview ── */
  .diff-preview {
    padding: 0 24px 80px;
    position: relative; z-index: 1;
  }
  .diff-preview-inner { max-width: 860px; margin: 0 auto; }

  .diff-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }
  .diff-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px 20px;
    display: flex; flex-direction: column; gap: 8px;
    transition: all 0.2s;
  }
  .diff-item:hover { transform: translateY(-3px); }
  .diff-item.easy  { --dc: #22c55e; }
  .diff-item.medium { --dc: #f59e0b; }
  .diff-item.hard  { --dc: #ef4444; }
  .diff-item:hover { border-color: var(--dc); box-shadow: 0 0 24px rgba(var(--dc-raw), 0.15); }
  .diff-item.easy:hover  { box-shadow: 0 0 24px rgba(34,197,94,0.15); }
  .diff-item.medium:hover { box-shadow: 0 0 24px rgba(245,158,11,0.15); }
  .diff-item.hard:hover  { box-shadow: 0 0 24px rgba(239,68,68,0.15); }

  .diff-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--dc); }
  .diff-item-name {
    font-family: 'Orbitron', monospace; font-size: 1rem; font-weight: 700;
    color: var(--dc);
  }
  .diff-item-info { font-size: 0.82rem; color: var(--muted2); line-height: 1.6; }
  .diff-item-mult {
    font-family: 'Space Mono', monospace; font-size: 0.75rem;
    color: var(--dc); background: rgba(255,255,255,0.05);
    border: 1px solid var(--border); border-radius: 6px;
    padding: 3px 10px; align-self: flex-start; margin-top: 4px;
  }

  /* ── Linguagens showcase ── */
  .langs-section {
    padding: 0 24px 80px;
    position: relative; z-index: 1;
  }
  .langs-inner { max-width: 860px; margin: 0 auto; }
  .langs-scroll {
    display: flex; gap: 12px; flex-wrap: wrap; justify-content: center;
    margin-top: 40px;
  }
  .lang-chip {
    display: flex; align-items: center; gap: 10px;
    padding: 8px 16px;
    border-radius: 100px;
    border: 1px solid var(--border);
    background: var(--surface);
    font-family: 'Orbitron', monospace; font-size: 0.72rem;
    font-weight: 700; letter-spacing: 0.1em;
    transition: all 0.2s;
    animation: chip-in 0.4s ease both;
  }
  .lang-chip:hover { transform: translateY(-2px) scale(1.04); border-color: var(--border2); }
  .lang-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }

  @keyframes chip-in {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── CTA final ── */
  .final-cta {
    padding: 80px 24px 100px;
    text-align: center;
    position: relative; z-index: 1;
    border-top: 1px solid var(--border);
  }
  .final-cta-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.6rem, 4vw, 2.8rem);
    font-weight: 900;
    background: linear-gradient(135deg, #fff 30%, #a5b4fc 70%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 16px;
  }
  .final-cta-sub { color: var(--muted2); font-size: 1rem; margin-bottom: 40px; }

  /* ══════════════════════════════════════════
     GAME SECTION
  ══════════════════════════════════════════ */
  #game-section {
    display: none;
    position: relative; z-index: 1;
    animation: section-in 0.5s ease;
  }
  #game-section.visible { display: block; }
  @keyframes section-in {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .back-bar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 32px;
    border-bottom: 1px solid var(--border);
    background: rgba(8,8,24,0.8);
    backdrop-filter: blur(12px);
    position: sticky; top: 0; z-index: 100;
  }
  .back-btn {
    display: flex; align-items: center; gap: 8px;
    font-family: 'Orbitron', monospace; font-size: 0.75rem;
    font-weight: 700; letter-spacing: 0.1em;
    color: var(--muted2); background: transparent;
    border: 1px solid var(--border); border-radius: 8px;
    padding: 8px 16px; cursor: pointer;
    transition: all 0.2s;
  }
  .back-btn:hover { border-color: var(--primary); color: var(--text); background: rgba(99,102,241,0.08); }

  /* ══════════════════════════════════════════
     GAME EMBED (igual ao original)
  ══════════════════════════════════════════ */
  #game-wrap { padding: 0; }

  .btn {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    width: 280px; height: 56px;
    border: 1px solid var(--border);
    border-radius: 10px;
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem; font-weight: 700;
    letter-spacing: 0.12em;
    cursor: pointer;
    transition: all 0.2s;
    position: relative; overflow: hidden;
    margin: 8px 0;
    text-transform: uppercase;
  }
  .btn::before {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, transparent 30%, rgba(255,255,255,0.05));
    opacity: 0; transition: opacity 0.2s;
  }
  .btn:hover::before { opacity: 1; }
  .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 32px var(--glow); }
  .btn:active { transform: translateY(0); }
  .btn-primary { background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; border-color: #6366f1; }
  .btn-secondary { background: var(--surface); color: var(--text); }
  .btn-success { background: linear-gradient(135deg, #15803d, #16a34a); color: #fff; border-color: #22c55e; }
  .btn-danger  { background: linear-gradient(135deg, #991b1b, #dc2626); color: #fff; border-color: #ef4444; }
  .btn-warning { background: linear-gradient(135deg, #92400e, #d97706); color: #fff; border-color: #f59e0b; }
  .btn-sm { width: 160px; height: 44px; font-size: 0.75rem; }
  .btn-xs { width: 120px; height: 36px; font-size: 0.7rem; margin: 4px; }

  /* ── GAME SCREENS ── */
  .screen { display: none; width: 100%; max-width: 860px; padding: 24px 20px; flex-direction: column; align-items: center; }
  .screen.active { display: flex; }

  #game-app { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; min-height: 80vh; }

  .logo {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 900;
    letter-spacing: 0.05em; text-align: center;
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 24px rgba(99,102,241,0.6));
    margin-bottom: 8px;
    animation: pulse-glow 3s ease-in-out infinite;
  }
  @keyframes pulse-glow {
    0%, 100% { filter: drop-shadow(0 0 24px rgba(99,102,241,0.6)); }
    50%       { filter: drop-shadow(0 0 48px rgba(168,85,247,0.9)); }
  }
  .logo-sub {
    font-size: 1rem; letter-spacing: 0.3em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 48px;
  }
  .diff-grid { display: flex; flex-direction: column; gap: 16px; width: 100%; max-width: 420px; margin: 16px 0 32px; }
  .diff-card {
    padding: 20px 24px; border-radius: 12px; border: 1px solid var(--border);
    background: var(--surface); cursor: pointer; transition: all 0.2s;
    display: flex; align-items: center; justify-content: space-between;
  }
  .diff-card:hover { transform: translateX(6px); border-color: var(--primary); box-shadow: -4px 0 0 var(--primary); }
  .diff-card.easy:hover  { border-color: var(--success); box-shadow: -4px 0 0 var(--success); }
  .diff-card.hard:hover  { border-color: var(--danger);  box-shadow: -4px 0 0 var(--danger); }
  .diff-card.medium:hover { border-color: var(--warning); box-shadow: -4px 0 0 var(--warning); }
  .diff-name { font-family: 'Orbitron', monospace; font-size: 1rem; font-weight: 700; }
  .diff-desc { font-size: 0.8rem; color: var(--muted); margin-top: 4px; }
  .diff-badge { font-family: 'Orbitron', monospace; font-size: 0.7rem; padding: 4px 10px; border-radius: 20px; font-weight: 700; }
  .input-wrap { position: relative; width: 100%; max-width: 360px; margin: 16px 0 32px; }
  .input-field {
    width: 100%; height: 56px;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; color: var(--text);
    font-family: 'Rajdhani', sans-serif; font-size: 1.2rem;
    padding: 0 16px; outline: none;
    transition: border-color 0.2s, box-shadow 0.2s; letter-spacing: 0.05em;
  }
  .input-field:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(99,102,241,0.2); }
  .hud {
    width: 100%; display: grid; grid-template-columns: repeat(4,1fr);
    gap: 10px; margin-bottom: 16px;
  }
  .hud-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; padding: 10px 14px;
    display: flex; flex-direction: column; align-items: center;
  }
  .hud-label { font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); margin-bottom: 2px; }
  .hud-value { font-family: 'Orbitron', monospace; font-size: 1.1rem; font-weight: 700; }
  .turn-timer { font-family: 'Orbitron', monospace; font-size: 0.85rem; text-align: center; height: 24px; margin-bottom: 8px; transition: color 0.3s; }
  .board { display: grid; gap: 10px; margin: 0 auto; }
  .card { aspect-ratio: 1; perspective: 600px; cursor: pointer; }
  .card-inner {
    width: 100%; height: 100%; position: relative;
    transform-style: preserve-3d;
    transition: transform 0.4s cubic-bezier(0.4,0,0.2,1);
    border-radius: 10px;
  }
  .card.flipped .card-inner { transform: rotateY(180deg); }
  .card.matched .card-inner { transform: rotateY(180deg); }
  .card-face {
    position: absolute; inset: 0; border-radius: 10px;
    backface-visibility: hidden;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    border: 2px solid var(--border); overflow: hidden; transition: border-color 0.2s;
  }
  .card-back { background: linear-gradient(135deg, #0f0f2a 0%, #1a1a3e 100%); }
  .card-back::before { content: '?'; font-family: 'Orbitron', monospace; font-size: 1.8rem; font-weight: 900; color: rgba(99,102,241,0.4); }
  .card-back::after {
    content: ''; position: absolute; inset: 0;
    background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(99,102,241,0.04) 8px, rgba(99,102,241,0.04) 9px);
  }
  .card-front { transform: rotateY(180deg); }
  .card-abbr { font-family: 'Orbitron', monospace; font-weight: 900; line-height: 1; }
  .card-name { font-size: 0.6rem; letter-spacing: 0.08em; text-transform: uppercase; margin-top: 4px; opacity: 0.85; }
  .card:hover:not(.flipped):not(.matched) .card-back { border-color: var(--primary); box-shadow: 0 0 16px var(--glow); }
  .card.matched .card-face { border-color: var(--success); box-shadow: 0 0 16px rgba(34,197,94,0.4); }
  .card.error   .card-inner { animation: shake 0.4s ease-in-out; }
  .card.error   .card-face  { border-color: var(--danger); }
  .card.pulse   .card-face  { animation: match-pulse 0.5s ease-out; }
  @keyframes shake {
    0%, 100% { transform: rotateY(180deg) translateX(0); }
    20% { transform: rotateY(180deg) translateX(-5px); }
    40% { transform: rotateY(180deg) translateX(5px); }
    60% { transform: rotateY(180deg) translateX(-4px); }
    80% { transform: rotateY(180deg) translateX(4px); }
  }
  @keyframes match-pulse {
    0%   { box-shadow: 0 0 0   rgba(34,197,94,0); }
    50%  { box-shadow: 0 0 28px rgba(34,197,94,0.8); }
    100% { box-shadow: 0 0 16px rgba(34,197,94,0.4); }
  }
  .score-display {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.5rem, 8vw, 4.5rem); font-weight: 900;
    background: linear-gradient(135deg, var(--gold), #ffa500);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 20px rgba(255,215,0,0.5));
    margin: 8px 0 24px;
    animation: score-in 0.6s cubic-bezier(0.34,1.56,0.64,1);
  }
  @keyframes score-in {
    from { transform: scale(0.3); opacity: 0; }
    to   { transform: scale(1);   opacity: 1; }
  }
  .stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; width: 100%; max-width: 360px; margin-bottom: 32px; }
  .stat-item { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 14px; text-align: center; }
  .stat-label { font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); }
  .stat-value { font-family: 'Orbitron', monospace; font-size: 1.2rem; font-weight: 700; margin-top: 4px; }
  .rank-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  .rank-table th { text-align: left; padding: 8px 12px; font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); border-bottom: 1px solid var(--border); }
  .rank-table td { padding: 10px 12px; border-bottom: 1px solid rgba(30,32,72,0.5); }
  .rank-table tr:hover td { background: rgba(99,102,241,0.05); }
  .screen-title { font-family: 'Orbitron', monospace; font-size: clamp(1.2rem, 3vw, 1.8rem); font-weight: 700; letter-spacing: 0.08em; text-align: center; margin-bottom: 8px; }
  .screen-sub { font-size: 0.9rem; color: var(--muted); text-align: center; letter-spacing: 0.1em; margin-bottom: 32px; }
  .btn-row { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; margin-top: 8px; }
  .hs-banner { font-family: 'Orbitron', monospace; font-size: 0.9rem; color: var(--gold); letter-spacing: 0.1em; animation: hs-glow 1.2s ease-in-out infinite alternate; margin-bottom: 8px; }
  @keyframes hs-glow {
    from { text-shadow: 0 0 8px rgba(255,215,0,0.4); }
    to   { text-shadow: 0 0 20px rgba(255,215,0,0.9); }
  }
  @media (max-width: 520px) {
    .hud { grid-template-columns: repeat(2, 1fr); }
    .stats-grid { grid-template-columns: 1fr; }
    nav { padding: 16px 20px; }
  }
</style>
</head>
<body>

<div id="particles"></div>

<!-- ══════════════════════════════════════════
     LANDING PAGE
══════════════════════════════════════════ -->
<div id="landing">

  <!-- Nav -->
  <nav>
    <div class="nav-logo">MEMORY.DEV</div>
    <div class="nav-badge">v2.0 · HTML5 · Web Audio</div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-orb"></div>
    <div class="hero-eyebrow">🧠 Treine sua memória</div>
    <h1 class="hero-title">
      MEMORY GAME
      <span>Linguagens de Programação</span>
    </h1>
    <p class="hero-desc">
      Encontre todos os pares de linguagens antes que o tempo acabe.
      Escolha a dificuldade, marque seu recorde e dispute o ranking.
    </p>
    <div class="hero-cta">
      <button class="cta-primary" onclick="launchGame()">
        ▶ &nbsp;JOGAR AGORA
      </button>
      <button class="cta-secondary" onclick="scrollToFeatures()">
        ↓ &nbsp;SAIBA MAIS
      </button>
    </div>
    <div class="hero-stats">
      <div class="hero-stat">
        <div class="hero-stat-value">12</div>
        <div class="hero-stat-label">Linguagens</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-value">3</div>
        <div class="hero-stat-label">Dificuldades</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-value">∞</div>
        <div class="hero-stat-label">Replayability</div>
      </div>
    </div>
  </section>

  <!-- Features -->
  <section class="features" id="features">
    <div class="features-inner">
      <div class="section-label">// funcionalidades</div>
      <h2 class="section-title">POR QUE JOGAR?</h2>
      <div class="feat-grid">
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#6366f1,#a855f7)">
          <div class="feat-icon">🎯</div>
          <div class="feat-title">3 NÍVEIS</div>
          <div class="feat-desc">Fácil, Médio e Difícil — cada nível com tabuleiro e multiplicador de pontuação diferente.</div>
        </div>
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#f59e0b,#ef4444)">
          <div class="feat-icon">⏱️</div>
          <div class="feat-title">TIMER DE JOGADA</div>
          <div class="feat-desc">No modo Difícil você tem apenas 5 segundos para virar a segunda carta. Pressão total.</div>
        </div>
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#22c55e,#06b6d4)">
          <div class="feat-icon">🏆</div>
          <div class="feat-title">RANKING LOCAL</div>
          <div class="feat-desc">Pontuação salva no navegador. Competição com você mesmo e com quem usar a mesma máquina.</div>
        </div>
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#ec4899,#8b5cf6)">
          <div class="feat-icon">🔊</div>
          <div class="feat-title">SOM GENERATIVO</div>
          <div class="feat-desc">Feedback sonoro em tempo real com Web Audio API — sem arquivos externos.</div>
        </div>
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#0ea5e9,#6366f1)">
          <div class="feat-icon">📱</div>
          <div class="feat-title">RESPONSIVO</div>
          <div class="feat-desc">Tabuleiro se adapta ao tamanho da tela. Funciona em mobile, tablet e desktop.</div>
        </div>
        <div class="feat-card" style="--card-accent: linear-gradient(90deg,#ffd700,#f59e0b)">
          <div class="feat-icon">⚡</div>
          <div class="feat-title">SEM INSTALAÇÃO</div>
          <div class="feat-desc">100% HTML, CSS e JavaScript puro. Roda direto no navegador, sem dependências.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Dificuldades -->
  <section class="diff-preview">
    <div class="diff-preview-inner">
      <div class="section-label">// modos de jogo</div>
      <h2 class="section-title">ESCOLHA SEU DESAFIO</h2>
      <div class="diff-row">
        <div class="diff-item easy">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="diff-dot" style="background:#22c55e"></div>
            <div class="diff-item-name">FÁCIL</div>
          </div>
          <div class="diff-item-info">
            Grade 4×3 · 6 pares<br>
            Sem timer de jogada<br>
            Cartas fecham em 1.2s
          </div>
          <div class="diff-item-mult">Multiplicador ×1.0</div>
        </div>
        <div class="diff-item medium">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="diff-dot" style="background:#f59e0b"></div>
            <div class="diff-item-name">MÉDIO</div>
          </div>
          <div class="diff-item-info">
            Grade 6×4 · 12 pares<br>
            Sem timer de jogada<br>
            Cartas fecham em 0.9s
          </div>
          <div class="diff-item-mult">Multiplicador ×1.5</div>
        </div>
        <div class="diff-item hard">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="diff-dot" style="background:#ef4444"></div>
            <div class="diff-item-name">DIFÍCIL</div>
          </div>
          <div class="diff-item-info">
            Grade 6×4 · 12 pares<br>
            5 segundos por carta<br>
            Cartas fecham em 0.6s
          </div>
          <div class="diff-item-mult">Multiplicador ×2.0</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Linguagens -->
  <section class="langs-section">
    <div class="langs-inner">
      <div class="section-label">// baralho completo</div>
      <h2 class="section-title">AS 12 LINGUAGENS</h2>
      <div class="langs-scroll" id="lang-chips"></div>
    </div>
  </section>

  <!-- CTA final -->
  <section class="final-cta">
    <div class="final-cta-title">PRONTO PARA JOGAR?</div>
    <div class="final-cta-sub">Teste sua memória e conquiste o topo do ranking.</div>
    <button class="cta-primary" style="margin:0 auto" onclick="launchGame()">
      ▶ &nbsp;INICIAR JOGO
    </button>
  </section>

</div><!-- /landing -->


<!-- ══════════════════════════════════════════
     GAME SECTION
══════════════════════════════════════════ -->
<div id="game-section">

  <div class="back-bar">
    <button class="back-btn" onclick="backToLanding()">← VOLTAR À LANDING</button>
    <div class="nav-logo">MEMORY.DEV</div>
  </div>

  <div id="game-wrap">
    <div id="game-app">

      <!-- Menu -->
      <div id="screen-menu" class="screen active">
        <div style="height:80px"></div>
        <div class="logo">MEMORY GAME</div>
        <div class="logo-sub">Linguagens de Programação</div>
        <button class="btn btn-primary" onclick="goTo('difficulty')">▶ &nbsp;JOGAR</button>
        <button class="btn btn-secondary" onclick="goTo('ranking')" style="margin-top:4px">🏆 &nbsp;RANKING</button>
      </div>

      <!-- Dificuldade -->
      <div id="screen-difficulty" class="screen">
        <div style="height:60px"></div>
        <div class="screen-title">DIFICULDADE</div>
        <div class="screen-sub">Escolha o desafio</div>
        <div class="diff-grid">
          <div class="diff-card easy" onclick="selectDiff('Fácil')">
            <div>
              <div class="diff-name" style="color:#22c55e">FÁCIL</div>
              <div class="diff-desc">4×3 &nbsp;·&nbsp; Sem timer &nbsp;·&nbsp; ×1.0 pts</div>
            </div>
            <div class="diff-badge" style="background:rgba(34,197,94,0.15);color:#22c55e;border:1px solid #22c55e">×1.0</div>
          </div>
          <div class="diff-card medium" onclick="selectDiff('Médio')">
            <div>
              <div class="diff-name" style="color:#f59e0b">MÉDIO</div>
              <div class="diff-desc">6×4 &nbsp;·&nbsp; Sem timer &nbsp;·&nbsp; ×1.5 pts</div>
            </div>
            <div class="diff-badge" style="background:rgba(245,158,11,0.15);color:#f59e0b;border:1px solid #f59e0b">×1.5</div>
          </div>
          <div class="diff-card hard" onclick="selectDiff('Difícil')">
            <div>
              <div class="diff-name" style="color:#ef4444">DIFÍCIL</div>
              <div class="diff-desc">6×4 &nbsp;·&nbsp; 5s por carta &nbsp;·&nbsp; ×2.0 pts</div>
            </div>
            <div class="diff-badge" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid #ef4444">×2.0</div>
          </div>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="goTo('menu')">← VOLTAR</button>
      </div>

      <!-- Nome -->
      <div id="screen-name" class="screen">
        <div style="height:80px"></div>
        <div class="screen-title">SEU NOME</div>
        <div class="screen-sub" id="name-diff-label"></div>
        <div class="input-wrap">
          <input id="player-name" class="input-field"
                 maxlength="16" placeholder="Digite seu nome..."
                 onkeydown="if(event.key==='Enter') startGame()">
        </div>
        <button class="btn btn-primary" onclick="startGame()">COMEÇAR ▶</button>
        <div style="height:16px"></div>
        <button class="btn btn-secondary btn-sm" onclick="goTo('difficulty')">← VOLTAR</button>
      </div>

      <!-- Jogo -->
      <div id="screen-playing" class="screen">
        <div class="hud" id="hud"></div>
        <div class="turn-timer" id="turn-timer"></div>
        <div class="board" id="board"></div>
      </div>

      <!-- Resultado -->
      <div id="screen-result" class="screen">
        <div style="height:40px"></div>
        <div class="screen-title">🎉 JOGO CONCLUÍDO</div>
        <div id="hs-banner"></div>
        <div class="score-display" id="final-score"></div>
        <div class="stats-grid" id="final-stats"></div>
        <div class="btn-row">
          <button class="btn btn-secondary btn-sm" onclick="goTo('menu')">◀ MENU</button>
          <button class="btn btn-primary btn-sm" onclick="playAgain()">↩ JOGAR NOVAMENTE</button>
        </div>
      </div>

      <!-- Ranking -->
      <div id="screen-ranking" class="screen">
        <div style="height:40px"></div>
        <div class="screen-title">🏆 RANKING</div>
        <div class="screen-sub">Top 20 partidas</div>
        <div id="rank-content" style="width:100%;overflow-x:auto"></div>
        <div style="height:24px"></div>
        <button class="btn btn-secondary btn-sm" onclick="goTo('menu')">← VOLTAR</button>
      </div>

    </div><!-- /game-app -->
  </div><!-- /game-wrap -->

</div><!-- /game-section -->


<script>
// ═══════════════════════════════════════════════
// LANDING → JOGO
// ═══════════════════════════════════════════════
function launchGame() {
  document.getElementById("landing").style.display = "none";
  const gs = document.getElementById("game-section");
  gs.classList.add("visible");
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function backToLanding() {
  document.getElementById("game-section").classList.remove("visible");
  document.getElementById("landing").style.display = "flex";
  document.getElementById("landing").style.flexDirection = "column";
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function scrollToFeatures() {
  document.getElementById("features").scrollIntoView({ behavior: "smooth" });
}

// ── Language chips ─────────────────────────────
const LANGUAGES = [
  { name:"Python",     abbr:"Py",  bg:"#3572a5", fg:"#ffd43b" },
  { name:"JavaScript", abbr:"JS",  bg:"#f0db4f", fg:"#323330" },
  { name:"TypeScript", abbr:"TS",  bg:"#3178c6", fg:"#ffffff" },
  { name:"Rust",       abbr:"Rs",  bg:"#222222", fg:"#ce5c1e" },
  { name:"Go",         abbr:"Go",  bg:"#00aed8", fg:"#ffffff" },
  { name:"Java",       abbr:"Jv",  bg:"#ed7516", fg:"#ffffff" },
  { name:"C++",        abbr:"C++", bg:"#00599c", fg:"#ffffff" },
  { name:"Swift",      abbr:"Sw",  bg:"#f05138", fg:"#ffffff" },
  { name:"Kotlin",     abbr:"Kt",  bg:"#7f52ff", fg:"#ffffff" },
  { name:"Ruby",       abbr:"Rb",  bg:"#a81111", fg:"#ffffff" },
  { name:"PHP",        abbr:"PHP", bg:"#777bb3", fg:"#ffffff" },
  { name:"Dart",       abbr:"Dt",  bg:"#00b4d8", fg:"#ffffff" },
];

(function renderChips() {
  const container = document.getElementById("lang-chips");
  LANGUAGES.forEach((l, i) => {
    const chip = document.createElement("div");
    chip.className = "lang-chip";
    chip.style.animationDelay = (i * 0.05) + "s";
    chip.innerHTML = `<div class="lang-dot" style="background:${l.bg}"></div>${l.name}`;
    container.appendChild(chip);
  });
})();

// ═══════════════════════════════════════════════
// GAME STATE
// ═══════════════════════════════════════════════
const DIFFICULTIES = {
  "Fácil":   { cols:4, rows:3, flipDelay:1200, turnTime:null,  mult:1.0 },
  "Médio":   { cols:6, rows:4, flipDelay:900,  turnTime:null,  mult:1.5 },
  "Difícil": { cols:6, rows:4, flipDelay:600,  turnTime:5000,  mult:2.0 },
};

let state = {
  screen:"menu", difficulty:"Médio", playerName:"Jogador",
  cards:[], flipped:[], waitTimer:null, turnTimer:null, turnLeft:0,
  pairsFound:0, totalPairs:0, errors:0,
  startTime:0, elapsedSec:0, clockInterval:null, gameOver:false,
};

// ── Ranking ────────────────────────────────────
function loadRanking() { try { return JSON.parse(localStorage.getItem("memory_ranking")||"[]"); } catch { return []; } }
function saveRanking(e) { localStorage.setItem("memory_ranking", JSON.stringify(e)); }
function addRankingEntry(entry) {
  let e = loadRanking(); e.push(entry);
  e.sort((a,b) => b.score - a.score); e = e.slice(0,20); saveRanking(e); return e;
}
function isHighscore(score) {
  const e = loadRanking(); if (e.length < 20) return true;
  return score > e[e.length-1].score;
}

// ── Nav ────────────────────────────────────────
function goTo(screenId) {
  document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
  document.getElementById("screen-"+screenId).classList.add("active");
  state.screen = screenId;
  if (screenId === "ranking") renderRanking();
}
function selectDiff(diff) {
  state.difficulty = diff;
  document.getElementById("name-diff-label").textContent = "Dificuldade: " + diff;
  document.getElementById("player-name").value = "";
  goTo("name");
  setTimeout(() => document.getElementById("player-name").focus(), 100);
}

// ── Game ───────────────────────────────────────
function startGame() {
  const name = document.getElementById("player-name").value.trim();
  state.playerName = name || "Jogador";
  buildGame(); goTo("playing");
}
function playAgain() { buildGame(); goTo("playing"); }

function buildGame() {
  const cfg = DIFFICULTIES[state.difficulty];
  const pairs = (cfg.cols * cfg.rows) / 2;
  let pool = [...LANGUAGES];
  while (pool.length < pairs) pool = [...pool, ...LANGUAGES];
  pool = pool.slice(0, pairs); shuffleArray(pool);
  const deck = [...pool, ...pool]; shuffleArray(deck);
  state.cards=deck; state.flipped=[]; state.pairsFound=0;
  state.totalPairs=pairs; state.errors=0; state.startTime=Date.now();
  state.elapsedSec=0; state.gameOver=false;
  state.waitTimer=null; state.turnTimer=null; state.turnLeft=0;
  clearInterval(state.clockInterval);
  state.clockInterval = setInterval(() => {
    if (!state.gameOver) { state.elapsedSec = (Date.now()-state.startTime)/1000; updateHUD(); updateTurnTimer(); }
  }, 100);
  renderBoard(); updateHUD();
}

function renderBoard() {
  const cfg = DIFFICULTIES[state.difficulty];
  const board = document.getElementById("board");
  const available = Math.min(window.innerWidth - 40, 820);
  const cardSize = Math.floor((available - cfg.cols*10) / cfg.cols);
  const clamped = Math.min(Math.max(cardSize,60),115);
  board.style.gridTemplateColumns = `repeat(${cfg.cols}, ${clamped}px)`;
  board.innerHTML = state.cards.map((lang,i) => `
    <div class="card" id="card-${i}" onclick="flipCard(${i})">
      <div class="card-inner">
        <div class="card-face card-back"></div>
        <div class="card-face card-front" style="background:${lang.bg};color:${lang.fg}">
          <div class="card-abbr" style="font-size:${clamped>90?1.6:1.1}rem">${lang.abbr}</div>
          <div class="card-name">${lang.name}</div>
        </div>
      </div>
    </div>
  `).join("");
}

function flipCard(index) {
  if (state.gameOver||state.waitTimer||state.flipped.length>=2) return;
  const el = document.getElementById("card-"+index);
  if (!el||el.classList.contains("flipped")||el.classList.contains("matched")) return;
  el.classList.add("flipped"); playSound("flip"); state.flipped.push(index);
  if (state.flipped.length===1) {
    const cfg = DIFFICULTIES[state.difficulty];
    if (cfg.turnTime) {
      state.turnLeft=cfg.turnTime;
      state.turnTimer=setInterval(()=>{
        state.turnLeft-=100;
        if (state.turnLeft<=0) {
          clearInterval(state.turnTimer); state.turnTimer=null;
          const idx=state.flipped[0];
          const cardEl=document.getElementById("card-"+idx);
          if(cardEl){cardEl.classList.remove("flipped");cardEl.classList.add("error");setTimeout(()=>cardEl.classList.remove("error"),500);}
          state.errors++; state.flipped=[]; updateHUD();
        }
        updateTurnTimer();
      },100);
    }
  }
  if (state.flipped.length===2){clearInterval(state.turnTimer);state.turnTimer=null;checkPair();}
}

function checkPair() {
  const [a,b]=state.flipped;
  const elA=document.getElementById("card-"+a), elB=document.getElementById("card-"+b);
  const cfg=DIFFICULTIES[state.difficulty];
  if (state.cards[a].name===state.cards[b].name) {
    state.pairsFound++;
    elA.classList.add("matched","pulse"); elB.classList.add("matched","pulse");
    setTimeout(()=>{elA.classList.remove("pulse");elB.classList.remove("pulse");},500);
    playSound("match"); state.flipped=[]; updateHUD();
    if (state.pairsFound===state.totalPairs) endGame();
  } else {
    state.errors++;
    elA.classList.add("error"); elB.classList.add("error");
    playSound("error"); updateHUD();
    state.waitTimer=setTimeout(()=>{
      elA.classList.remove("flipped","error"); elB.classList.remove("flipped","error");
      state.flipped=[]; state.waitTimer=null;
    },cfg.flipDelay);
  }
}

function endGame() {
  state.gameOver=true; clearInterval(state.clockInterval); clearInterval(state.turnTimer);
  state.elapsedSec=(Date.now()-state.startTime)/1000;
  const score=calcScore(), hs=isHighscore(score);
  addRankingEntry({name:state.playerName,score,pairs:state.pairsFound,errors:state.errors,timeSec:Math.round(state.elapsedSec),difficulty:state.difficulty,date:new Date().toLocaleDateString("pt-BR")});
  playSound("victory"); showResult(score,hs);
}

function calcScore() {
  const cfg=DIFFICULTIES[state.difficulty];
  return Math.round(Math.max(0,state.pairsFound*1000-state.errors*100-Math.floor(state.elapsedSec*2))*cfg.mult);
}

function updateHUD() {
  const elapsed=state.gameOver?state.elapsedSec:(Date.now()-state.startTime)/1000;
  const m=Math.floor(elapsed/60).toString().padStart(2,"0");
  const s=Math.floor(elapsed%60).toString().padStart(2,"0");
  document.getElementById("hud").innerHTML=`
    <div class="hud-card"><div class="hud-label">Jogador</div><div class="hud-value" style="font-size:0.85rem;font-family:'Rajdhani',sans-serif">${state.playerName}</div></div>
    <div class="hud-card"><div class="hud-label">Pares</div><div class="hud-value" style="color:#22c55e">${state.pairsFound}/${state.totalPairs}</div></div>
    <div class="hud-card"><div class="hud-label">Erros</div><div class="hud-value" style="color:#ef4444">${state.errors}</div></div>
    <div class="hud-card"><div class="hud-label">Tempo</div><div class="hud-value" style="color:#f59e0b">${m}:${s}</div></div>
  `;
}

function updateTurnTimer() {
  const el=document.getElementById("turn-timer"); if(!el) return;
  if(state.turnTimer&&state.flipped.length===1){
    const secs=(state.turnLeft/1000).toFixed(1);
    const color=state.turnLeft>2000?"#f59e0b":"#ef4444";
    el.innerHTML=`<span style="color:${color}">Vire a 2ª carta em ${secs}s</span>`;
  } else { el.innerHTML=""; }
}

function showResult(score,isHs) {
  document.getElementById("final-score").textContent=score.toLocaleString("pt-BR")+" pts";
  document.getElementById("hs-banner").innerHTML=isHs?'<div class="hs-banner">★ NOVO RECORDE! ★</div>':"";
  const m=Math.floor(state.elapsedSec/60).toString().padStart(2,"0");
  const s=Math.floor(state.elapsedSec%60).toString().padStart(2,"0");
  document.getElementById("final-stats").innerHTML=`
    <div class="stat-item"><div class="stat-label">Dificuldade</div><div class="stat-value" style="font-size:0.9rem">${state.difficulty}</div></div>
    <div class="stat-item"><div class="stat-label">Pares</div><div class="stat-value" style="color:#22c55e">${state.pairsFound}/${state.totalPairs}</div></div>
    <div class="stat-item"><div class="stat-label">Erros</div><div class="stat-value" style="color:#ef4444">${state.errors}</div></div>
    <div class="stat-item"><div class="stat-label">Tempo</div><div class="stat-value" style="color:#f59e0b">${m}:${s}</div></div>
  `;
  goTo("result");
}

function renderRanking() {
  const entries=loadRanking();
  const medals=["🥇","🥈","🥉"];
  const diffColor={"Fácil":"#22c55e","Médio":"#f59e0b","Difícil":"#ef4444"};
  if (!entries.length) {
    document.getElementById("rank-content").innerHTML='<p style="color:var(--muted);text-align:center;padding:40px">Nenhuma partida registrada ainda.</p>';
    return;
  }
  const rows=entries.map((e,i)=>{
    const m=Math.floor(e.timeSec/60).toString().padStart(2,"0");
    const s=(e.timeSec%60).toString().padStart(2,"0");
    const dc=diffColor[e.difficulty]||"#fff";
    return `<tr>
      <td>${medals[i]||(i+1)}</td>
      <td><strong>${e.name}</strong></td>
      <td style="color:#ffd700;font-family:'Orbitron',monospace">${(e.score||0).toLocaleString("pt-BR")}</td>
      <td style="color:${dc}">${e.difficulty}</td>
      <td style="color:#22c55e">${e.pairs}</td>
      <td style="color:#ef4444">${e.errors}</td>
      <td style="color:#f59e0b">${m}:${s}</td>
      <td style="color:var(--muted)">${e.date||""}</td>
    </tr>`;
  }).join("");
  document.getElementById("rank-content").innerHTML=`
    <table class="rank-table">
      <thead><tr><th>#</th><th>Nome</th><th>Pts</th><th>Dif.</th><th>Pares</th><th>Erros</th><th>Tempo</th><th>Data</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

// ── Sound ──────────────────────────────────────
let audioCtx=null;
function getAudio(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();return audioCtx;}
function playTone(freq,dur,type="sine",vol=0.3){
  try{const ctx=getAudio(),osc=ctx.createOscillator(),gain=ctx.createGain();
  osc.connect(gain);gain.connect(ctx.destination);
  osc.type=type;osc.frequency.value=freq;
  gain.gain.setValueAtTime(vol,ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+dur);
  osc.start();osc.stop(ctx.currentTime+dur);}catch{}
}
function playSound(name){
  if(name==="flip"){playTone(440,0.05,"sine",0.15);}
  if(name==="match"){playTone(523,0.08);setTimeout(()=>playTone(659,0.15),80);}
  if(name==="error"){playTone(330,0.08,"square",0.2);setTimeout(()=>playTone(220,0.15,"square",0.2),80);}
  if(name==="victory"){[523,659,784].forEach((f,i)=>setTimeout(()=>playTone(f,0.18),i*120));}
}

// ── Particles ──────────────────────────────────
(function spawnParticles(){
  const c=document.getElementById("particles");
  for(let i=0;i<30;i++){
    const p=document.createElement("div");p.className="particle";
    p.style.left=Math.random()*100+"vw";
    p.style.animationDuration=(8+Math.random()*12)+"s";
    p.style.animationDelay=(Math.random()*15)+"s";
    p.style.width=p.style.height=(1+Math.random()*3)+"px";
    c.appendChild(p);
  }
})();

window.addEventListener("resize",()=>{
  if(state.screen==="playing"&&state.cards.length) renderBoard();
});
</script>
</body>
</html>
"""

components.html(FULL_HTML, height=900, scrolling=True)
