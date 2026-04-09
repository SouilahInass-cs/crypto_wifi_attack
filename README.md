🚀 WPA/WPA2 Offline Brute Force Simulation






📌 Overview

This project is an educational simulation of a WPA/WPA2 offline brute force attack.

It demonstrates how attackers can recover passwords from a captured handshake without interacting with the network, using hash comparison techniques.

⚠️ This project is strictly for educational and lab environments only.

🎯 Objectives
Understand how WPA/WPA2 authentication works
Learn how offline brute force attacks operate
Demonstrate the importance of strong passwords
Simulate password cracking using hashing techniques
Practice secure coding and cybersecurity fundamentals
🧠 How It Works
A password is selected as the "target"
The password is hashed using SHA-256
This hash simulates a captured WPA/WPA2 handshake
A brute force script:
Generates candidate passwords
Hashes each candidate
Compares it with the target hash
When a match is found → password is recovered
📁 Project Structure
crypto_wifi_attack/
│
├── demo/
│   ├── 1_setup_handshake.py      # Generates simulated handshake (hash)
│   ├── 2_bruteforce_attack.py    # Performs brute force attack
│   ├── utils.py                  # Helper functions
│
└── README.md
⚙️ Requirements
Python 3.x
No external dependencies required
▶️ Installation & Usage
1. Clone the repository
git clone https://github.com/your-username/crypto_wifi_attack.git
cd crypto_wifi_attack/demo
2. Run handshake generation
python 1_setup_handshake.py
3. Run brute force attack
python 2_bruteforce_attack.py
🧪 Demo Workflow
Step 1 → Generate a hashed password (simulated handshake)
Step 2 → Run brute force attack
Step 3 → Observe password recovery through hash comparison
🔐 Key Concepts
Hashing (SHA-256): One-way cryptographic function
Offline Attack: No interaction with the target system
Brute Force: Systematic guessing of possible passwords
Handshake Simulation: Represents captured authentication data
📊 Why This Matters
WPA/WPA2 networks rely on password strength
Weak passwords are vulnerable to brute force attacks
Offline attacks bypass rate limiting and lockout protections
Strong, random passwords significantly increase security
⚠️ Ethical & Legal Notice

This project is intended strictly for educational purposes in controlled environments.

✔ Allowed:

Personal learning
Academic demonstrations
Authorized lab environments

❌ Not allowed:

Attacking systems you do not own
Unauthorized penetration testing
Real-world malicious use
🧾 Author
Project created for cybersecurity learning and academic demonstration.
⭐ Future Improvements
Add GPU acceleration simulation
Integrate wordlist-based attacks
Improve attack performance visualization
Add GUI interface for demonstrations
📌 Notes
Designed for clarity and educational explanation
Keep the project lightweight and easy to run
No external dependencies required
🔥 Comment faire les mises à jour sur GitHub (important)

Après modification du README ou du code :

git add .
git commit -m "Update README and improvements"
git push
💡 Pro tip (très important)

Si tu modifies seulement le README :

git add README.md
git commit -m "Improve README documentation"
git push