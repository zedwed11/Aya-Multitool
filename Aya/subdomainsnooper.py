import requests


def run():
    print("Subdomain Snooper Launched....")
    print("----------------------------")
    print()

    domain = input("Enter Domain: ").strip()

    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("\n[+] Certificate data snooped")
    else:
        print("\n[-] Failed to retrieve certificate data.")
        return

    data = response.json()

    subdomains = set()

    for certificate in data:
        names = certificate.get("name_value", "")

        for name in names.split("\n"):
            name = name.strip().lower()

            if name.endswith("." + domain) or name == domain:
                subdomains.add(name)

    print("\nSubdomains Snooped:")
    print("----------------------------")

    if subdomains:
        for subdomain in sorted(subdomains):
            print(f"[+] {subdomain}")

            input("Enter to exit...")

        print("----------------------------")
        print(f"[+] Total: {len(subdomains)}")
    else:
        print("[-] No subdomains found.")

        input("Enter to exit..")


if __name__ == "__main__":
    run()
    





