import socket
import time
from concurrent.futures import ThreadPoolExecutor


def run():
    print("Tool Launched....")
    print("------------------------")
    print("Port Scanner..")
    print("Scan for Open or Closed Ports on IP Addresses")
    print()

    target = input("Enter Target IP: ")

    start_time = time.time()

    print(f"\nScanning {target}...\n")

    ports = range(1, 101)

    def scan_port(target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")

            sock.close()

        except socket.error:
            print(f"[!] Error scanning port {port}")

    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)

    end_time = time.time()

    print(f"\nScan finished in {round(end_time - start_time, 2)} seconds")

    input("\nPress Enter to close...")