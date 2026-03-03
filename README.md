# 🔐 Rail Fence Cipher — Streamlit App

A production-grade cryptography tool featuring encrypt/decrypt, live fence visualization, and rail breakdown analytics — all in a dark glassmorphic UI.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔒 Encryption | Zigzag plaintext across N rails, read row-by-row |
| 🔓 Decryption | Index-pattern reconstruction for exact reversal |
| 📊 Fence Visualizer | Character-level zigzag grid rendered inline |
| 🧩 Rail Breakdown | Per-rail character groups with color coding |
| 📈 Stats Panel | Character count, cycle length, unique chars |
| 🎨 Dark UI | Glassmorphism, animated mesh gradients, custom fonts |

---

## 🚀 Quick Start
```bash
# 1. Clone / download the project
git clone https://github.com/yourname/railfence-cipher

# 2. Install dependencies
pip install streamlit

# 3. Launch the app
streamlit run railfence_app.py
```

Then open your browser at `http://localhost:8501`

---

## 🧠 How Rail Fence Works

**Encryption — 3 rails, text = `WEAREDISCOVERED`**
```
Rail 1:  W · · · E · · · I · · · V · · ·
Rail 2:  · E · R · D · S · O · E · E · D
Rail 3:  · · A · · · C · · · R · · · · ·
```

Reading each rail left-to-right:
```
Rail 1 → WEIV
Rail 2 → ERDSOEEED
Rail 3 → ACR
```
Ciphertext: `WEIVERDSOEEDACR`

**Decryption** reverses this by reconstructing the zigzag index pattern and mapping ciphertext characters back into their original positions.

---

## 📁 Project Structure
```
railfence-cipher/
├── railfence_app.py     # Streamlit UI application
├── railfence_core.py    # Standalone cipher class (importable)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 📦 Requirements
```
streamlit>=1.32.0
```

---

## 🔐 Security Note

Rail Fence is a **classical transposition cipher** with a key space equal only to the number of rails. It is not suitable for any real security use — it exists as a historical and educational cipher.

---

## 📄 License

MIT — free to use, modify, and distribute.
