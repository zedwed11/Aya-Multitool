import os
import shutil
from iplookup import run as iplookup
from dnslookup import run as dnslookup
from whoislookup import run as whoislookup
from webscraper import run as webscraper
from webcrawler import run as webcrawler
from DoSAttack import run as dosattack
from phonelookup import run as phonelookup
from codescraper import run as codescraper
from ipgrabber import run as ipgrabber
from Ippinger import run as ippinger
from Portscanner1 import run as portscanner1
from gmailbombss import run as gmailbombss
from MiniSherlock1 import run as MiniSherlock1
from subdomainsnooper import run as subdomainsnooper
from dorkingsearch import run as dorkingsearch
from breachchecker import run as breacher
from DoxCreator import run as doxcreator
from AyaVuln import run as ayavuln





os.system("cls")

logo = r"""___/\\\\\\\\\_____/\\\________/\\\_____/\\\\\\\\\______________         
 ____/\\\\\\\\\\\\\__\///\\\____/\\\/____/\\\\\\\\\\\\\____________        
 __ __/\\\/////////\\\___\///\\\/\\\/_____/\\\/////////\\\___________       
   _\/\\\_______\/\\\_____\///\\\/______\/\\\_______\/\\\___________      
    _\/\\\\\\\\\\\\\\\_______\/\\\_______\/\\\\\\\\\\\\\\\___________     
     _\/\\\/////////\\\_______\/\\\_______\/\\\/////////\\\___________    
      _\/\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\___________   
      _\/\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\___________  
        _\///________\///________\///________\///________\///____________ 
"""

width = shutil.get_terminal_size().columns

for line in logo.splitlines():
    print(line.center(width))
print("------------------------------------------------------------------------------------------------------------------------")


logo = r"""   //Anywhere, Anytime.\\"""

print("===================================")
print("=============")
print("======")
print("by @zed")
print("Join Our Discord!")
print("Yes I completely made this tool by myself, no help. I am new to coding")
print()
print("So please go easy on me and if you have ideas for the tool just dm me in discord or join!!")
print("https://discord.gg/cCKctNPvE6")


width = shutil.get_terminal_size().columns

for line in logo.splitlines():
    print(line.center(width))

print("Malicous...")
print("==============")
print("[1] Email Bomber")
print("[2] DoS Attack")
print("[3] Ip Grabber")
print()
print()
print()
print("Osint...")
print("===========")
print("[4] Ip Lookup")
print("[5] Dns Lookup")
print("[6] Phone Lookup")
print("[7] WHOIS Lookup")
print()
print()
print()
print("Utility...")
print("=============")
print("[8] Port Scanner")
print("[9] Web Scraper")
print("[10] Web Crawler")
print("[11] Code Scraper")
print("[12] Ip Pinger")
print("[13] Dark Web Links....")
print()
print()
print()
print("More OSINT..")
print("=============")
print("[14] Username Search")
print("[15] Google Dorking Query Engine")
print("[16} Subdomain Snooper")
print("[17] Email Breach Searcher")
print()
print()
print("Malicous Utilities..")
print("========================")
print("[18] Dox Creator")
print("[19] Website Vulnerability Scanner")
print()
print()
choice = input("[1-19]> ")
print()
print("-------------------------------------------")

if choice == "1":
    gmailbombss()

elif choice == "2":
    dosattack()

elif choice == "3":
    ipgrabber()

elif choice == "4":
    iplookup()

elif choice == "5":
    dnslookup()

elif choice == "6":
    phonelookup()

elif choice == "7":
    whoislookup()

elif choice == "8":
    portscanner1()

elif choice == "9":
    webscraper()

elif choice == "10":
    webcrawler()

elif choice == "11":
    codescraper()

elif choice == "12":
    ippinger()

elif choice == "13":
    print("Dark Web Links")
    print("==============")
    print("==================================")
    print()
    print()
    print("1. Tor Project: https://www.torproject.org/")
    print("use Tor Browser to access the dark web and the links im giving u, also use a vpn, disable javascript, use tails os or whonix if u wanna be really secure")
    print("if ur broke honestly just use proton vpn, if u got money use nullvad, also use proxy chains if u can,")
    print()
    print()
    print("DRUGS/GUNS")
    print("=============")
    print("1. Drughub: http://drughuj7l72ig56pza77eriu7yh6qsao4xb4yasq2qfjusxzuq6rlwqd.onion")
    print("2. BlackMarket Guns: http://bmgunsyop5qa34nzrayd6shsovsukwbbscyo2hbu3ri7b2ghw6sjgrad.onion/")
    print()
    print("MARKETS")
    print("=============")
    print("1. Nexus Market: https://nexus7x625hcsc3aucxk4rkfdxd5nipguct5ppankin5ftw2jy4mxdid.top/")
    print("2. Omega Market: http://omega7yhz7n4vg4yhf2na2qaaaeatdlqvjbj2juc245mr5muxtnuvgyd.onion/")
    print()
    print("FORUMS")
    print("=============")
    print("1. Tenebris: http://tenebrispoyfrcup4k24lciwrh4gc5735hmld4dweq7his7zh423opqd.onion/")
    print("2. Dread: https://dreadytognbh7m5nlmqsogzzlxjy75iuxkulewbhxcorupbqahact2yd.onion/?")
    print()
    print()
    print("OTHER")
    print("=============")
    print("1. Hidden Wiki: https://thehidden-wiki.org/wiki/index.php/Main_Page")
    print("2. Opsec Bible (not really dark web but if ur conscious about opsec check this out): https://gist.github.com/vil/7dfdb362d3aef91183101c300da3c543")
    print("3. Darknethub: https://dark-web.guru/?shop=darknet-market&domain=black-market.org&page=%2F")
    print("4. Metadata Wiper: https://www.metawiper.net/")
    print()
    print()
    print("CRYPTO WALLETS")
    print("==================")
    print("If you too young or whatever and don't have a crypto wallet use these")
    print("1. Exodus Wallet: https://www.exodus.com/")
    print("2. Phantom: https://phantom.com/")
    print("These are all the links i got ngl if I find more i'll update this.")
    input("Enter to Exit...")

elif choice == "14":
    MiniSherlock1()

elif choice == "15":
    dorkingsearch()

elif choice == "16":
    subdomainsnooper()

elif choice == "17":
    breacher()

elif choice == "18":
    doxcreator()

elif choice == "19":
    ayavuln()




    input("Enter to exit...")