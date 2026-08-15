import json
import os


PROFILE_FILE = "profiles.json"


def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}

    with open(PROFILE_FILE, "r") as file:
        return json.load(file)


def save_profiles(profiles):
    with open(PROFILE_FILE, "w") as file:
        json.dump(profiles, file, indent=4)


def create_profile(profiles):
    print("\n--- Create Dox ---")

    name = input("Name: ").strip()

    if not name:
        print("[-] Name cannot be empty.")
        return

    profile = {
        "email": input("Email: ").strip(),
        "username": input("Username/Alias: ").strip(),
        "phone": input("Phone: ").strip(),
        "ip": input("IP: ").strip(),
        "location": input("Location: ").strip(),
        "instagram": input("Instagram: ").strip(),
        "github": input("GitHub: ").strip(),
        "twitter": input("X/Twitter: ").strip(),
        "tiktok": input("TikTok: ").strip(),
        "website": input("Website: ").strip(),
        "notes": input("Notes: ").strip()
    }

    profiles[name] = profile
    save_profiles(profiles)

    print(f"\n[+] Profile '{name}' saved!")


def view_profiles(profiles):
    if not profiles:
        print("\n[-] No Doxes saved.")
        return

    print("\n--- Saved Doxes ---")

    for name in profiles:
        print(f"[+] {name}")


def view_profile(profiles):
    name = input("\nEnter profile name: ").strip()

    if name not in profiles:
        print("[-] Profile not found.")
        return

    profile = profiles[name]

    print("\n================================")
    print(f"        {name}")
    print("================================")

    for field, value in profile.items():
        print(f"{field.title()}: {value}")

    print("================================")


def delete_profile(profiles):
    name = input("\nEnter profile name to delete: ").strip()

    if name not in profiles:
        print("[-] Profile not found.")
        return

    del profiles[name]
    save_profiles(profiles)

    print(f"[+] Profile '{name}' deleted.")


def run():
    profiles = load_profiles()

    while True:
        print("\n")
        print("================================")
        print("       AYA DOX MANAGER")
        print("================================")
        print("[1] Create Profile")
        print("[2] View Profiles")
        print("[3] View Profile")
        print("[4] Delete Profile")
        print("[5] Exit")
        print("================================")

        choice = input("Select option: ").strip()

        if choice == "1":
            create_profile(profiles)

        elif choice == "2":
            view_profiles(profiles)

        elif choice == "3":
            view_profile(profiles)

        elif choice == "4":
            delete_profile(profiles)

        elif choice == "5":
            print("[+] Exiting Dox Manager...")
            break

        else:
            print("[-] Invalid option.")


if __name__ == "__main__":
    run()