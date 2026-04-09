from utils import hash_password
'''Secret Wi-Fi password (simulated)'''
PASSWORD = "abc"


def main():
    print("======================================")
    print(" WPA/WPA2 HANDSHAKE SIMULATION")
    print("======================================\n")

    handshake = hash_password(PASSWORD)

    # Save handshake to file
    with open("handshake.txt", "w") as f:
        f.write(handshake)

    print("[+] Secret password set (hidden)")
    print("[+] Simulated handshake generated:")
    print(handshake)
    print("\n[+] Handshake saved to handshake.txt")


if __name__ == "__main__":
    main()
