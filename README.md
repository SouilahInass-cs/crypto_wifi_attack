<div align="center">

# 🔐 WPA/WPA2 Offline Brute Force Simulation

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Purpose-Educational-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>

<br/>

> **An educational simulation of a WPA/WPA2 offline brute force attack demonstrating how password hashing and hash comparison work in practice.**

<br/>

```
⚠️  FOR EDUCATIONAL & LAB ENVIRONMENTS ONLY — DO NOT USE ON UNAUTHORIZED SYSTEMS  ⚠️
```

</div>

---

## 📌 Overview

This project is an **educational simulation** of a WPA/WPA2 offline brute force attack. It demonstrates how attackers can recover passwords from a captured handshake **without interacting with the network**, using SHA-256 hash comparison techniques.

It is designed for students, researchers, and cybersecurity enthusiasts who want to understand real attack vectors in a **safe, controlled environment**.

---

## 🎯 Objectives

- Understand how WPA/WPA2 authentication works
- Learn how offline brute force attacks operate
- Demonstrate the critical importance of strong passwords
- Simulate password cracking using hashing techniques
- Practice secure coding and cybersecurity fundamentals

---

## 🧠 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                      SIMULATION WORKFLOW                        │
│                                                                 │
│  1. Target password selected                                    │
│       ↓                                                         │
│  2. Password hashed with SHA-256  →  "Captured Handshake"      │
│       ↓                                                         │
│  3. Brute force script runs:                                    │
│       • Generates candidate passwords                           │
│       • Hashes each candidate                                   │
│       • Compares hash to target hash                            │
│       ↓                                                         │
│  4. Match found  →  ✅ Password Recovered!                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
crypto_wifi_attack/
│
├── demo/
│   ├── 1_setup_handshake.py      # Generates simulated handshake (hash)
│   ├── 2_bruteforce_attack.py    # Performs the brute force attack
│   └── utils.py                  # Helper / utility functions
│
└── README.md
```

---

## ⚙️ Requirements

| Requirement | Details |
|---|---|
| **Python** | 3.x or higher |
| **Dependencies** | None — standard library only |
| **OS** | Windows / Linux / macOS |

---

## ▶️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto_wifi_attack.git
cd crypto_wifi_attack/demo
```

### 2. Generate the simulated handshake

```bash
python 1_setup_handshake.py
```

### 3. Run the brute force attack

```bash
python 2_bruteforce_attack.py
```

---

## 🧪 Demo Workflow

```
Step 1  →  Generate a hashed password (simulates captured handshake)
Step 2  →  Launch the brute force attack script
Step 3  →  Observe password recovery via hash comparison
```

---

## 🔐 Key Concepts

| Concept | Description |
|---|---|
| **Hashing (SHA-256)** | One-way cryptographic function — cannot be reversed |
| **Offline Attack** | No interaction with the live target network |
| **Brute Force** | Systematic enumeration of all possible passwords |
| **Handshake Simulation** | Represents captured WPA/WPA2 authentication data |

---

## 📊 Why This Matters

- WPA/WPA2 network security relies **entirely** on password strength
- Weak passwords are highly vulnerable to offline brute force attacks
- Offline attacks **bypass rate limiting and lockout protections**
- Strong, random passwords dramatically increase the time required to crack

> 💡 *A 12-character random password can take thousands of years to brute force — a 6-character simple password can fall in seconds.*

---

## ⚠️ Ethical & Legal Notice

<div align="center">

| ✅ **Allowed** | ❌ **Not Allowed** |
|---|---|
| Personal learning & research | Attacking systems you don't own |
| Academic demonstrations | Unauthorized penetration testing |
| Authorized lab environments | Real-world malicious use of any kind |

</div>

> This project is intended **strictly for educational purposes** in controlled environments. The author assumes **no responsibility** for any misuse of this material.

---

## 🔄 Git Workflow — Pushing Updates to GitHub

After modifying code or the README:

```bash
git add .
git commit -m "Update README and improvements"
git push
```

If you only modified the README:

```bash
git add README.md
git commit -m "Improve README documentation"
git push
```

---

## ⭐ Future Improvements

- [ ] Add GPU acceleration simulation
- [ ] Integrate wordlist-based (dictionary) attacks
- [ ] Improve attack performance visualization
- [ ] Add a GUI interface for demonstrations
- [ ] Add benchmark mode to measure speed

---

## 👤 Author

**Project created for cybersecurity learning and academic demonstration.**

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-your--username-181717?style=for-the-badge&logo=github)](https://github.com/your-username)

<br/>

*⭐ If you found this project useful, please consider giving it a star!*

</div>

---

<div align="center">
<sub>Built with 🔒 for educational cybersecurity awareness</sub>
</div>