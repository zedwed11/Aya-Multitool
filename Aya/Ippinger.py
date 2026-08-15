import subprocess
import platform

def run():
    print("Tool Launched....")
    print("------------------------")
    print("IP pinger")
    print()
    print()

    ip = input("Enter IP or hostname: ")

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", ip]

    else:
        command = ["ping", "-c", "4", ip]

    try:
        subprocess.run(command)

    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to close...")
