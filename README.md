# WPA/WPA2 Offline Brute Force Simulation

In real WPA/WPA2 security:

- Passwords are never tested directly online
- Attackers capture a handshake
- They perform offline brute force attacks
- Each password guess is validated locally using cryptographic hashes

---

## 🔬 Simulation Overview

This project simulates the process:

- A password is converted into a SHA-256 hash (simulated handshake)
- A brute force script tries to recover the original password
- Instead of comparing plaintext passwords, hashes are compared

---

## 📁 Project Structure


demo/
├── 1_setup_handshake.py # Generates a simulated handshake (hash)
├── 2_bruteforce_attack.py # Performs brute force attack
├── utils.py # Helper functions


---

## ⚙️ Requirements

- Python 3.x
- No external libraries required

---

## ▶️ How to Run

Step 1: Generate the handshake

```bash
cd demo
python 1_setup_handshake.py

Step 2: Run the brute force attack

python 2_bruteforce_attack.py
📌 How It Works
A password is hashed using SHA-256
The hash simulates a captured WPA/WPA2 handshake
The brute force script:
Generates candidate passwords
Hashes each candidate
Compares it with the target hash
If a match is found, the password is recovered
## 🎯 Learning Goals
Understand how offline brute force attacks work
Learn the role of cryptographic hashing
Understand why strong passwords matter
See why offline attacks are powerful (no rate limiting)
⚠️ Security Note

Real-world WPA/WPA2 attacks involve:

Capturing handshakes using specialized tools
Using large wordlists (millions of passwords)
GPU acceleration for faster hashing