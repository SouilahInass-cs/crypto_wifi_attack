# WPA/WPA2 Offline Brute Force Simulation

## 🎯 Objective
This project simulates a WPA/WPA2 offline brute force attack in a controlled lab environment.

## 🧠 Concept
In real WPA/WPA2 networks:
- Passwords are never tested directly online
- Attackers capture a handshake
- They perform offline brute force by testing password candidates

## 🔬 Simulation
- A password is converted into a SHA-256 hash (simulated handshake)
- A brute force script attempts to recover the password
- The attack compares hashes instead of plaintext

## 📁 Structure
- demo/1_setup_handshake.py → generate handshake
- demo/2_bruteforce_attack.py → perform brute force
- demo/utils.py → helper functions

## ⚙️ Requirements
- Python 3.x
- No external libraries required

## ▶️ How to Run

```bash
cd demo
python 1_setup_handshake.py
python 2_bruteforce_attack.py