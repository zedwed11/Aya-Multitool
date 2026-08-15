import socket
import dns.resolver


def run():
    print("Tool Launched....")
    print("----------------------")

    domain = input("Enter Domain... ")

    try:
        ip = socket.gethostbyname(domain)

        print(f"\nIP Address: {ip}")
        print(f"Domain: {domain}")

        hostname, aliases, addresses = socket.gethostbyname_ex(domain)

        print(f"Hostname: {hostname}")

        print("\nA Records:")
        for x in dns.resolver.resolve(domain, "A"):
            print(f"  └── {x}")

        print("\nAAAA Records:")
        for x in dns.resolver.resolve(domain, "AAAA"):
            print(f"  └── {x}")

        print("\nMX Records:")
        for x in dns.resolver.resolve(domain, "MX"):
            print(f"  └── {x}")

        print("\nNS Records:")
        for x in dns.resolver.resolve(domain, "NS"):
            print(f"  └── {x}")

        print("\nTXT Records:")
        for x in dns.resolver.resolve(domain, "TXT"):
            print(f"  └── {x}")


        



    except socket.gaierror:
        print("\nCould not find that domain.")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    run()