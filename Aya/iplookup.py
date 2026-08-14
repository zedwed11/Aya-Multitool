import requests
import time


def typewriter(text, speed=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(speed)
    print()


def run():
    try:
        typewriter("IP Lookup Launched....")
        typewriter("============================")

        ip = input("Enter the IP address: ")

        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url, timeout=10)

        data = response.json()

        if data["status"] != "success":
            print("Lookup failed:", data.get("message", "Unknown error"))
            input("Press Enter to exit...")
            return

        print()
        typewriter("\\IP INFO//")
        typewriter("--------------")

        time.sleep(1)

        print("IP:", data["query"])
        print("-------------------------")
        print("Country:", data["country"])
        print("-------------------------")
        print("Region:", data["regionName"])
        print("-------------------------")
        print("City:", data["city"])
        print("-------------------------")
        print("ZIP:", data["zip"])
        print("-------------------------")
        print("ISP:", data["isp"])
        print("-------------------------")
        print("Organization:", data["org"])
        print("-------------------------")
        print("Latitude:", data["lat"])
        print("-------------------------")
        print("Longitude:", data["lon"])
        print("-------------------------")
        print("Timezone:", data["timezone"])

        input("\nPress Enter to return...")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.")
        input("Press Enter to return...")

    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the API.")
        input("Press Enter to return...")

    except requests.exceptions.RequestException as error:
        print("\nRequest error:", error)
        input("Press Enter to return...")

    except Exception as error:
        print("\nUnexpected error:", error)
        input("Press Enter to return...")