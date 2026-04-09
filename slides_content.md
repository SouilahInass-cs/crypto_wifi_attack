# Slide 1 — Title
WPA/WPA2 Offline Brute Force Attack Simulation

# Slide 2 — Objective
- Understand how attackers recover Wi-Fi passwords
- Simulate offline brute force attack

# Slide 3 — Real WPA/WPA2 Mechanism
- Password not tested directly
- Handshake exchanged
- Captured by attacker

# Slide 4 — Attack Principle
- Attacker works offline
- Tries password candidates
- Compares cryptographic hash

# Slide 5 — Hashing Concept
- Password → SHA-256 → hash
- Same input = same hash

# Slide 6 — Simulation Overview
- Password defined
- Hash generated (handshake)
- Brute force attack

# Slide 7 — Demo Setup
- handshake.txt contains hash
- attacker script reads it

# Slide 8 — Brute Force Algorithm
- Generate combinations
- Hash each candidate
- Compare with target

# Slide 9 — Live Demo
- Run setup script
- Run attack script
- Observe attempts

# Slide 10 — Complexity
- Exponential growth
- Longer password = harder attack

# Slide 11 — Performance
- More characters = more combinations
- Time increases rapidly

# Slide 12 — Limitations
- Simulation only
- Real WPA uses stronger mechanisms

# Slide 13 — Security Best Practices
- Long passwords
- Random characters
- Avoid common patterns

# Slide 14 — Conclusion
- Offline attacks are powerful
- Strong passwords are essential