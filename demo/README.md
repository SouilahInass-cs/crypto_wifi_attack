
---

# 📄 2. demo/README.md

```markdown
# Demo Instructions

## Step 1 — Generate the simulated handshake

Run:
python 1_setup_handshake.py

This will:
- Define a secret password
- Generate its SHA-256 hash
- Save it as the "captured handshake"

## Step 2 — Run brute force attack

Run:
python 2_bruteforce_attack.py

This script:
- Generates candidate passwords
- Hashes them
- Compares with the captured handshake
- Stops when the password is found

## Notes
- Charset and length are limited for demo purposes
- You can modify charset in the script