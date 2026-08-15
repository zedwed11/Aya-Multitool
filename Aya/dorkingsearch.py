import webbrowser


def run():
    print("Tool Launched...")
    print("--------------------------------")
    print()

    domain = input("Enter domain: ").strip()

    print()
    print("[1] Find PDF files")
    print("[2] Find login pages")
    print("[3] Find exposed directories")
    print("[4] Find documents")
    print("[5] Find admin pages")
    print("[6] Search for a keyword")
    print("[7] Custom dork")
    print()

    choice = input("Select option: ").strip()

    if choice == "1":
        dork = f"site:{domain} filetype:pdf"

    elif choice == "2":
        dork = f"site:{domain} inurl:login"

    elif choice == "3":
        dork = f"site:{domain} intitle:\"index of\""

    elif choice == "4":
        dork = f"site:{domain} filetype:doc OR filetype:docx"

    elif choice == "5":
        dork = f"site:{domain} inurl:admin"

    elif choice == "6":
        keyword = input("Enter keyword: ").strip()
        dork = f"site:{domain} \"{keyword}\""

    elif choice == "7":
        dork = input("Enter custom Google dork: ").strip()

    else:
        print("[-] Invalid option.")
        return

    print()
    print(f"[+] Generated Dork: {dork}")
    print()

    search_url = "https://www.google.com/search?q=" + dork.replace(" ", "+")
    webbrowser.open(search_url)

    print("[+] Opening Google search...")


if __name__ == "__main__":
    run()