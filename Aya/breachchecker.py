import requests

def run():
    print("Email Breach Checker Launched...")
    print("--------------------------------")
    print()

    email = input("Enter email: ").strip()

    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("\n[+] Email found in breach database!")

        for breach in data["breaches"][0]:
            print(f"[+] {breach}")

    elif response.status_code == 404:
        print("\n[+] No breaches found!")

    else:
        print(f"\n[-] Request failed: {response.status_code}")