import streamlit as st

# ── Core Logic ────────────────────────────────────────────
def encrypt(text, rails):
    if rails < 2 or rails >= len(text):
        return text
    fence = [""] * rails
    rail, d = 0, 1
    for ch in text:
        fence[rail] += ch
        if rail == 0: d = 1
        elif rail == rails - 1: d = -1
        rail += d
    return "".join(fence)

def decrypt(cipher, rails):
    n = len(cipher)
    if rails < 2 or rails >= n:
        return cipher
    pattern = []
    rail, d = 0, 1
    for _ in range(n):
        pattern.append(rail)
        if rail == 0: d = 1
        elif rail == rails - 1: d = -1
        rail += d
    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [""] * n
    for pos, idx in enumerate(indices):
        result[idx] = cipher[pos]
    return "".join(result)

def build_fence(text, rails):
    grid = [["·"] * len(text) for _ in range(rails)]
    rail, d = 0, 1
    for col, ch in enumerate(text):
        grid[rail][col] = ch
        if rail == 0: d = 1
        elif rail == rails - 1: d = -1
        rail += d
    return grid

# ── Page Config ───────────────────────────────────────────
st.set_page_config(page_title="RAILFENCE//SYS", page_icon="⬡", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap');

:root {
  --green: #00ff41;
  --green2: #00cc33;
  --dim: #004d14;
  --bg: #020a04;
  --bg2: #040e06;
  --red: #ff2244;
  --border: #00ff4133;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
  background: var(--bg) !important;
  font-family: 'Share Tech Mono', monospace !important;
  color: var(--green) !important;
}

/* Scanline overlay */
.stApp::after {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.08) 2px, rgba(0,0,0,0.08) 4px
  );
  pointer-events: none;
  z-index: 9999;
}

/* CRT edge glow */
.stApp::before {
  content: '';
  position: fixed;
  inset: 0;
  box-shadow: inset 0 0 120px rgba(0,0,0,0.8), inset 0 0 40px rgba(0,255,65,0.03);
  pointer-events: none;
  z-index: 9998;
}

.sys-header {
  border-bottom: 1px solid var(--green2);
  padding: 1rem 0 0.8rem;
  margin-bottom: 1.5rem;
}
.sys-header-title {
  font-family: 'VT323', monospace;
  font-size: 1.4rem;
  color: var(--green);
  letter-spacing: 0.1em;
}
.sys-header-sub {
  font-size: 0.68rem;
  color: var(--dim);
  letter-spacing: 0.12em;
  margin-top: 0.3rem;
}
.blink {
  display: inline-block;
  width: 10px; height: 1em;
  background: var(--green);
  margin-left: 4px;
  vertical-align: middle;
  animation: blink 1s step-end infinite;
}
@keyframes blink { 50% { opacity: 0; } }

.glitch-wrap { text-align: center; padding: 1rem 0 1.8rem; }
.glitch {
  font-family: 'VT323', monospace;
  font-size: clamp(3.5rem, 10vw, 7rem);
  color: var(--green);
  text-shadow: 0 0 10px rgba(0,255,65,0.8), 0 0 30px rgba(0,255,65,0.4), 0 0 60px rgba(0,255,65,0.2);
  letter-spacing: 0.08em;
  position: relative;
  display: inline-block;
  animation: glitch 4s infinite;
}
.glitch::before, .glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font-family: 'VT323', monospace;
  font-size: inherit;
  letter-spacing: inherit;
}
.glitch::before {
  color: #ff2244;
  animation: glitch-r 4s infinite;
  clip-path: polygon(0 0, 100% 0, 100% 30%, 0 30%);
}
.glitch::after {
  color: #00ffff;
  animation: glitch-b 4s infinite;
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
}
@keyframes glitch {
  0%,90%,100% { transform: translate(0); }
  92% { transform: translate(-2px, 1px); }
  94% { transform: translate(2px, -1px); }
  96% { transform: translate(-1px, 2px); }
}
@keyframes glitch-r {
  0%,90%,100% { transform: translate(0); opacity: 0; }
  92% { transform: translate(3px, 0); opacity: 0.7; }
  94% { transform: translate(-3px, 0); opacity: 0.7; }
  96% { opacity: 0; }
}
@keyframes glitch-b {
  0%,90%,100% { transform: translate(0); opacity: 0; }
  93% { transform: translate(-3px, 0); opacity: 0.7; }
  95% { transform: translate(3px, 0); opacity: 0.7; }
  97% { opacity: 0; }
}

/* ── Textarea override ── */
.stTextArea > div > div > textarea {
  background: #000 !important;
  border: 1px solid var(--green2) !important;
  border-radius: 0 !important;
  color: var(--green) !important;
  font-family: 'Share Tech Mono', monospace !important;
  font-size: 1rem !important;
  caret-color: var(--green) !important;
  padding: 0.8rem !important;
}
.stTextArea > div > div > textarea:focus {
  border-color: var(--green) !important;
  box-shadow: 0 0 12px rgba(0,255,65,0.2) !important;
  outline: none !important;
}
.stTextArea > div > div > textarea::placeholder { color: var(--dim) !important; }

/* ── Labels ── */
.stTextArea label, .stSlider label, p, div[data-testid="stMarkdownContainer"] p {
  color: var(--green) !important;
  font-family: 'Share Tech Mono', monospace !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.1em !important;
}

/* ── Slider ── */
[data-baseweb="slider"] [role="slider"] { background: var(--green) !important; border-color: #000 !important; }
[data-baseweb="slider"] > div > div:first-child { background: var(--dim) !important; }
[data-baseweb="slider"] > div > div:nth-child(2) { background: var(--green) !important; }

/* ── Button ── */
.stButton > button {
  background: transparent !important;
  border: 1px solid var(--green) !important;
  color: var(--green) !important;
  font-family: 'VT323', monospace !important;
  font-size: 1.5rem !important;
  letter-spacing: 0.2em !important;
  padding: 0.5rem 2rem !important;
  border-radius: 0 !important;
  width: 100% !important;
  text-shadow: 0 0 8px rgba(0,255,65,0.6) !important;
  box-shadow: 0 0 10px rgba(0,255,65,0.1) !important;
  transition: all 0.15s !important;
}
.stButton > button:hover {
  background: rgba(0,255,65,0.08) !important;
  box-shadow: 0 0 25px rgba(0,255,65,0.3) !important;
}

/* ── Radio ── */
.stRadio > div[role="radiogroup"] { flex-direction: row !important; gap: 2rem !important; }
.stRadio label {
  color: var(--dim) !important;
  font-family: 'Share Tech Mono', monospace !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.12em !important;
}

/* ── Output ── */
.out-box {
  border: 1px solid var(--green);
  background: #000;
  padding: 1.2rem 1.4rem;
  margin-top: 1rem;
  box-shadow: 0 0 20px rgba(0,255,65,0.15), inset 0 0 30px rgba(0,255,65,0.03);
  position: relative;
}
.out-label { font-size: 0.65rem; letter-spacing: 0.25em; color: var(--dim); margin-bottom: 0.5rem; }
.out-text { font-size: 1.35rem; color: var(--green); word-break: break-all; line-height: 1.6; text-shadow: 0 0 8px rgba(0,255,65,0.5); }
.out-meta { position: absolute; top: 0.6rem; right: 0.8rem; font-size: 0.6rem; letter-spacing: 0.12em; color: var(--dim); }

/* ── Stats ── */
.stat-row { display: flex; gap: 0.7rem; margin: 1rem 0; flex-wrap: wrap; }
.stat { flex: 1; min-width: 90px; border: 1px solid var(--border); background: #000; padding: 0.75rem; text-align: center; }
.sv { font-family: 'VT323', monospace; font-size: 2rem; color: var(--green); line-height: 1; text-shadow: 0 0 10px rgba(0,255,65,0.5); }
.sk { font-size: 0.58rem; letter-spacing: 0.18em; color: var(--dim); margin-top: 0.2rem; }

/* ── Fence ── */
.fence-wrap {
  background: #000; border: 1px solid var(--border);
  padding: 1rem 1.2rem; overflow-x: auto; margin-top: 0.4rem;
  font-size: 0.82rem; line-height: 2;
  font-family: 'Share Tech Mono', monospace;
}
.f-rail { color: var(--dim); margin-right: 0.4rem; }
.f-ch { color: var(--green); font-weight: bold; text-shadow: 0 0 5px rgba(0,255,65,0.7); }
.f-dot { color: #071509; }

/* ── Rail chips ── */
.rail-chips { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.4rem; }
.rail-chip { border: 1px solid var(--border); background: #000; padding: 0.55rem 0.75rem; min-width: 80px; text-align: center; }
.rc-num { font-size: 0.58rem; letter-spacing: 0.18em; color: var(--dim); }
.rc-txt { font-size: 0.9rem; color: var(--green); word-break: break-all; line-height: 1.5; text-shadow: 0 0 4px rgba(0,255,65,0.4); }
.rc-len { font-size: 0.58rem; color: #051209; margin-top: 0.15rem; }

/* ── Algo panel ── */
.algo-panel {
  border: 1px solid var(--border); background: var(--bg2);
  padding: 1.2rem; margin-bottom: 1rem;
}
.algo-panel pre { color: #004d14; font-size: 0.75rem; line-height: 1.9; font-family: 'Share Tech Mono', monospace; }

hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.5rem 0 !important; }
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
[data-testid="stToolbar"] { visibility: hidden !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ──
st.markdown("""
<div class="sys-header">
  <div class="sys-header-title">RAILFENCE//CIPHER//SYS v2.4.1<span class="blink"></span></div>
  <div class="sys-header-sub">&gt; TRANSPOSITION ENCRYPTION MODULE — OPERATIONAL</div>
</div>
<div class="glitch-wrap">
  <span class="glitch" data-text="RAIL//FENCE">RAIL//FENCE</span>
</div>
""", unsafe_allow_html=True)

# ── Mode ──
_, col_mid, _ = st.columns([1, 2, 1])
with col_mid:
    mode = st.radio("", ["[ ENCRYPT ]", "[ DECRYPT ]"], horizontal=True, label_visibility="collapsed")

is_encrypt = "ENCRYPT" in mode
st.markdown("<br>", unsafe_allow_html=True)

# ── Main layout ──
L, R = st.columns([3, 2], gap="large")

with L:
    prompt_lbl = "> ENTER PLAINTEXT_" if is_encrypt else "> ENTER CIPHERTEXT_"
    st.markdown(f'<div style="font-size:.68rem;letter-spacing:.2em;color:#00cc33;margin-bottom:.35rem">{prompt_lbl}</div>', unsafe_allow_html=True)
    user_text = st.text_area("input_area", placeholder="TYPE MESSAGE HERE...", height=160, label_visibility="collapsed", key="user_text")
    st.markdown('<div style="font-size:.68rem;letter-spacing:.2em;color:#00cc33;margin:.8rem 0 .3rem">> RAIL COUNT_</div>', unsafe_allow_html=True)
    rails = st.slider("rails_slider", 2, 10, 3, label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)
    run = st.button("[ EXECUTE CIPHER ]")

with R:
    st.markdown("""
<div class="algo-panel">
<pre>STEP 01  Write chars diagonally
         across N rails in a
         Z-I-G-Z-A-G pattern.

STEP 02  Read each rail row
         left to right.

STEP 03  JOIN all rows →
         CIPHERTEXT output.

STEP 04  INDEX reconstruction
         reverses the cipher.</pre>
</div>""", unsafe_allow_html=True)

    cycle = 2 * (rails - 1)
    st.markdown(f"""
<div class="stat-row">
  <div class="stat"><div class="sv">{rails}</div><div class="sk">RAILS</div></div>
  <div class="stat"><div class="sv">{cycle}</div><div class="sk">CYCLE</div></div>
  <div class="stat"><div class="sv">{rails**2}</div><div class="sk">KEYSPACE</div></div>
</div>""", unsafe_allow_html=True)

# ── Results ──
if run and user_text.strip():
    clean = user_text.strip()
    result = encrypt(clean, rails) if is_encrypt else decrypt(clean, rails)
    out_type = "CIPHERTEXT OUTPUT" if is_encrypt else "PLAINTEXT OUTPUT"

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
<div class="out-box">
  <div class="out-label">&gt; {out_type}</div>
  <div class="out-text">{result}</div>
  <div class="out-meta">[ {len(result)} CHARS ]</div>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="stat-row">
  <div class="stat"><div class="sv">{len(clean)}</div><div class="sk">INPUT LEN</div></div>
  <div class="stat"><div class="sv">{len(result)}</div><div class="sk">OUTPUT LEN</div></div>
  <div class="stat"><div class="sv">{len(set(clean.upper()))}</div><div class="sk">UNIQUE</div></div>
  <div class="stat"><div class="sv">{2*(rails-1)}</div><div class="sk">CYCLE</div></div>
</div>""", unsafe_allow_html=True)

    # Fence visualization
    st.markdown('<div style="font-size:.65rem;letter-spacing:.2em;color:#004d14;margin:1.2rem 0 .3rem">&gt; FENCE DIAGRAM</div>', unsafe_allow_html=True)
    source = clean if is_encrypt else result
    grid = build_fence(source, rails)
    rows_html = []
    for r, row in enumerate(grid):
        cells = [f'<span class="f-ch">{ch}</span>' if ch != "·" else f'<span class="f-dot">·</span>' for ch in row]
        rows_html.append(f'<span class="f-rail">R{r+1}</span>' + " ".join(cells))
    st.markdown(f'<div class="fence-wrap">{"<br>".join(rows_html)}</div>', unsafe_allow_html=True)

    # Rail breakdown
    st.markdown('<div style="font-size:.65rem;letter-spacing:.2em;color:#004d14;margin:1.2rem 0 .3rem">&gt; RAIL BREAKDOWN</div>', unsafe_allow_html=True)
    fence = [""] * rails
    rail, d = 0, 1
    for ch in (clean if is_encrypt else result):
        fence[rail] += ch
        if rail == 0: d = 1
        elif rail == rails - 1: d = -1
        rail += d

    chips = "".join(f'<div class="rail-chip"><div class="rc-num">RAIL {i+1}</div><div class="rc-txt">{rc}</div><div class="rc-len">{len(rc)}c</div></div>' for i, rc in enumerate(fence))
    st.markdown(f'<div class="rail-chips">{chips}</div>', unsafe_allow_html=True)

elif run:
    st.markdown('<div style="color:#ff2244;font-size:.78rem;letter-spacing:.1em;padding:.75rem;border:1px solid #ff2244;background:rgba(255,34,68,0.05)">ERR: NO INPUT DETECTED — ENTER TEXT TO PROCESS.</div>', unsafe_allow_html=True)

st.markdown('<hr><div style="text-align:center;font-size:.58rem;letter-spacing:.2em;color:#04150a;padding:.8rem">RAILFENCE//SYS — TRANSPOSITION CIPHER MODULE — ALL OPERATIONS LOGGED</div>', unsafe_allow_html=True)