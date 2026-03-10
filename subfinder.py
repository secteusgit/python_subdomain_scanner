import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python3 subfinder.py domain.com")
    sys.exit()

domain = sys.argv[1]

print(f"\n[+] Scanning subdomains for {domain}\n")

with open("wordlist.txt") as file:
    for sub in file:
        sub = sub.strip()
        subdomain = f"{sub}.{domain}"

        try:
            socket.gethostbyname(subdomain)
            print(f"[FOUND] {subdomain}")
        except socket.gaierror:
            pass

print("\nScan finished.")
