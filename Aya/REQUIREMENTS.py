import subprocess
import sys

packages = [
    "requests",
    "beautifulsoup4",
    "python-whois",
    "aiohttp",
    "phonenumbers",
    "dnspython"
    "from concurrent.futures import ThreadPoolExecutor, as_completed"
]

print("Installing Aya requirements...")
print("-------------------------------")

for package in packages:
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("-------------------------------")
print("All requirements installed!")
print()
print("Join our chill discord!!")
print("https://discord.gg/qJyvEmxkja")
input("Press Enter to exit...")