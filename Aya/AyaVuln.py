import requests


def run():
    print("Tool launched...")
    print("---------------------")
    print()
    print("Aya Vulnerability Scanner")
    print()

    url = input("Enter website URL: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

    except requests.RequestException as error:
        print(f"[-] Connection failed: {error}")
        input("Enter to close...")

    print()
    print(f"[+] Website: {response.url}")
    print(f"[+] Status Code: {response.status_code}")
    print(f"[+] Response Time: {response.elapsed.total_seconds():.2f}s")
    print()

    print("----- Security Headers -----")

    security_headers = {
        "Strict-Transport-Security": "HSTS",
        "Content-Security-Policy": "Content Security Policy",
        "X-Content-Type-Options": "Content Type Protection",
        "X-Frame-Options": "Clickjacking Protection",
        "Referrer-Policy": "Referrer Policy",
        "Permissions-Policy": "Permissions Policy"
    }

    for header, description in security_headers.items():

        if header in response.headers:
            print(f"[+] {description}: Present")
        else:
            print(f"[-] {description}: Missing")

    print()
    print("----- Cookie Security -----")

    if not response.cookies:
        print("[+] No cookies detected.")

    else:
        for cookie in response.cookies:

            print()
            print(f"Cookie: {cookie.name}")

            if cookie.secure:
                print("[+] Secure: Enabled")
            else:
                print("[-] Secure: Missing")

            if cookie.has_nonstandard_attr("HttpOnly"):
                print("[+] HttpOnly: Enabled")
            else:
                print("[-] HttpOnly: Missing")

            if cookie.get("SameSite"):
                print(f"[+] SameSite: {cookie.get('SameSite')}")
            else:
                print("[-] SameSite: Missing")

    print()
    print("----- Server Information -----")

    server = response.headers.get("Server")

    if server:
        print(f"[!] Server header exposed: {server}")
    else:
        print("[+] Server header not exposed.")

    print()
    print("----- Additional Information -----")

    content_type = response.headers.get("Content-Type")

    if content_type:
        print(f"[+] Content-Type: {content_type}")

    powered_by = response.headers.get("X-Powered-By")

    if powered_by:
        print(f"[!] X-Powered-By exposed: {powered_by}")
    else:
        print("[+] X-Powered-By not exposed.")

    print()
    print("---------------------")
    print("Scan complete.")
    input("Enter to close...")


if __name__ == "__main__":
    run()