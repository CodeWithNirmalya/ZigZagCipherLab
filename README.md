🔐 Rail Fence Cipher — Streamlit App
<div align="center">
Rail Fence Cipher Banner
Streamlit
Python
License: MIT

A production-grade cryptography visualization tool featuring real-time encryption, interactive fence visualization, and comprehensive rail breakdown analytics
🚀 Live Demo • 📖 Documentation • ✨ Features • 🤝 Contributing

<img src="https://via.placeholder.com/800x450/1a1a2e/6C63FF?text=Rail+Fence+Cipher+Dashboard" alt="Rail Fence Cipher Dashboard" />
Modern glassmorphic dark UI with real-time cipher visualization

</div>
🎯 Overview
The Rail Fence Cipher is a classical transposition cipher that writes plaintext in a zigzag pattern across multiple "rails" (rows), then reads off the ciphertext row by row. This educational tool brings this historical cipher to life with:

🎨 Beautiful Dark Glassmorphic UI — Modern design with animated mesh gradients
🔄 Real-time Encryption/Decryption — Instant cipher conversion as you type
📊 Interactive Visualizations — See the zigzag pattern come alive
📈 Detailed Analytics — Character breakdowns, cycle analysis, and statistics
🎓 Educational Focus — Perfect for learning classical cryptography
✨ Features
<table> <tr> <td width="50%">
🔒 Dual-Mode Cipher Engine
Encrypt Mode: Transform plaintext into ciphertext
Decrypt Mode: Reverse engineering with index reconstruction
Support for 2-10 rails configuration
Handles spaces and special characters
</td> <td width="50%">
📊 Live Fence Visualization
Character-level zigzag grid rendering
Color-coded rail identification
Rail index tracking
Cycle length calculation
</td> </tr> <tr> <td width="50%">
🧩 Rail Breakdown Analytics
Per-rail character grouping
Position index mapping
Color-coded segments
Character frequency analysis
</td> <td width="50%">
📈 Statistics Dashboard
Total character count
Unique character tracking
Cycle length computation
Rail distribution metrics
</td> </tr> </table>
🎬 Demo
<div align="center">
Encryption in Action
<img src="https://via.placeholder.com/700x400/0f0f23/6C63FF?text=Encryption+Demo+GIF" alt="Encryption Demo" />
Real-time encryption with live fence visualization

Rail Visualization & Breakdown
<img src="https://via.placeholder.com/700x400/0f0f23/FF6B6B?text=Visualization+Demo+GIF" alt="Visualization Demo" />
Interactive zigzag pattern and rail-by-rail breakdown

</div>
🚀 Quick Start
Prerequisites
Bash

Python 3.8 or higher
pip package manager
Installation
1️⃣ Clone the repository

Bash

git clone https://github.com/nirmalyaraja/railfence-cipher.git
cd railfence-cipher
2️⃣ Install dependencies

Bash

pip install -r requirements.txt
3️⃣ Launch the application

Bash

streamlit run railfence_ui.py
4️⃣ Open your browser

text

🌐 Local URL: http://localhost:8501
🌍 Network URL: http://192.168.x.x:8501
Docker Installation (Optional)
Bash

# Build the Docker image
docker build -t railfence-cipher .

# Run the container
docker run -p 8501:8501 railfence-cipher
🧠 How It Works
The Rail Fence Algorithm
The Rail Fence cipher creates a zigzag pattern by writing the message diagonally across a set number of "rails" (rows), then reading horizontally to generate the ciphertext.

<div align="center">
📝 Example: Encrypting "WEAREDISCOVERED" with 3 rails
</div>
text

Position:  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
           ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

Rail 1:    W · · · E · · · I · · · V · · ·
           ↘           ↗ ↘           ↗ ↘

Rail 2:    · E · R · D · S · O · E · E · D
             ↘   ↗ ↘   ↗ ↘   ↗ ↘   ↗ ↘

Rail 3:    · · A · · · C · · · R · · · · ·
               ↗           ↗           ↗
Reading row-by-row:

text

Rail 1: W E I V
Rail 2: E R D S O E E D
Rail 3: A C R
Ciphertext: WEIVERDSOEEEDACR

Encryption Process
Python

# Pseudo-code
for each character in plaintext:
    place in current_rail
    if at top_rail:
        direction = DOWN
    elif at bottom_rail:
        direction = UP
    move to next_rail based on direction

ciphertext = concatenate all rails left-to-right
Decryption Process
Python

# Pseudo-code
1. Calculate character count per rail
2. Reconstruct zigzag index pattern
3. Map ciphertext positions to original positions
4. Sort by original position
5. Extract plaintext
📁 Project Structure
text

railfence-cipher/
│
├── 📄 railfence_ui.py              # Main Streamlit application
├── 🔐 cipher_text_convert.py       # Core cipher logic (standalone)
├── 🎨 assets/                      # Images, GIFs, icons
│   ├── banner.png
│   ├── demo.gif
│   └── logo.svg
│
├── 🐳 Dockerfile                   # Docker configuration
├── 📦 requirements.txt             # Python dependencies
├── 📝 README.md                    # This file
├── 📜 LICENSE                      # MIT License
└── 🧪 tests/                       # Unit tests
    └── test_cipher.py
🎨 UI/UX Design
<div align="center">
Design Philosophy
Dark Glassmorphism • Responsive Layout • Smooth Animations

<img src="https://via.placeholder.com/800x100/1a1a2e/6C63FF?text=Glassmorphic+Design+Elements" alt="Design Elements" /></div>
Color Palette
Color	Hex	Usage
🟣 Primary	#6C63FF	Accent, buttons, highlights
🔵 Secondary	#3F3D56	Cards, containers
⚫ Background	#1a1a2e	Main background
🔴 Danger	#FF6B6B	Errors, warnings
🟢 Success	#51CF66	Success states
Typography
Headings: Inter, SF Pro Display
Body: Roboto, system-ui
Monospace: Fira Code, Consolas
🔐 Security Note
⚠️ Educational Purpose Only

The Rail Fence cipher is a classical transposition cipher from the pre-computer era. It provides NO real security and should NEVER be used for protecting sensitive information.

Why it's insecure:

❌ Key space is tiny (only N rails)
❌ Vulnerable to frequency analysis
❌ Easily broken with brute force
❌ Pattern recognition reveals structure
Use modern encryption instead:

✅ AES-256 for symmetric encryption
✅ RSA-4096 for asymmetric encryption
✅ bcrypt/Argon2 for password hashing
📦 Dependencies
txt

streamlit>=1.32.0          # Web framework
pandas>=2.0.0              # Data manipulation (optional)
numpy>=1.24.0              # Numerical operations (optional)
Development Dependencies
txt

pytest>=7.4.0              # Testing framework
black>=23.0.0              # Code formatting
flake8>=6.0.0              # Linting
mypy>=1.0.0                # Type checking
🧪 Testing
Run the test suite:

Bash

# Run all tests
pytest

# Run with coverage
pytest --cov=./ --cov-report=html

# Run specific test file
pytest tests/test_cipher.py -v
🛠️ API Reference
RailFenceCipher Class
Python

from cipher_text_convert import RailFenceCipher

# Initialize cipher with 3 rails
cipher = RailFenceCipher(rails=3)

# Encrypt
ciphertext = cipher.encrypt("HELLO WORLD")
# Returns: "HOLELWRDLO "

# Decrypt
plaintext = cipher.decrypt("HOLELWRDLO ")
# Returns: "HELLO WORLD"

# Get fence visualization
fence = cipher.get_fence_pattern("HELLO")
# Returns: 2D array of the zigzag pattern
Methods
Method	Parameters	Returns	Description
encrypt(text)	text: str	str	Encrypts plaintext
decrypt(text)	text: str	str	Decrypts ciphertext
get_fence_pattern(text)	text: str	list[list]	Returns zigzag grid
get_rail_breakdown(text)	text: str	dict	Returns rail-wise chars
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Contribution Guidelines
Follow PEP 8 style guide
Add unit tests for new features
Update documentation as needed
Keep commits atomic and well-described
🗺️ Roadmap
 🌍 Multi-language support (i18n)
 📱 Mobile-responsive design improvements
 🎯 More cipher algorithms (Caesar, Vigenère)
 💾 Export results as PDF/PNG
 🔊 Audio visualization of cipher patterns
 🎮 Gamification - cipher challenges
 🌐 REST API for programmatic access
 📚 Comprehensive tutorial mode
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

text

MIT License

Copyright (c) 2024 Nirmalya Raja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
👨‍💻 Author
<div align="center">
Nirmalya Raja
GitHub
LinkedIn
Twitter
Portfolio

Crafted with ❤️ and Python

</div>
🙏 Acknowledgments
Inspired by classical cryptography textbooks
Streamlit community for amazing framework
Contributors and testers
Historical cryptographers who paved the way
📊 Project Stats
<div align="center">
GitHub Stars
GitHub Forks
GitHub Watchers

GitHub Issues
GitHub Pull Requests
GitHub Last Commit
GitHub Code Size

</div>
<div align="center">
⭐ Star this repository if you find it helpful!
Made with 🔐 for cryptography enthusiasts and learners

</div>
