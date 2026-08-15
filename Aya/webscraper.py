import requests
from bs4 import BeautifulSoup
import time

def run():
    print("Tool Launched....")
    print("---------------------")
    print()

    url = input("Enter Url Here: ")

        
    #Agent spoofer for server/bot detection
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    print("Adding in delays so website thinks we're human..")
    print()
    print("Spoofing Bot as User...")
    print()
    print("And doesn't detect the Scraper Bot..")

    time.sleep(2)

    if response.status_code == 200:
        print("Website Retrieved..")

        time.sleep(0.1)
    elif response.status_code == 403:
        print("Forbidden Website..")
        input("Enter to exit..")
        return


    elif response.status_code == 404:
        print("Website Not Found...")
        input("Enter to exit..")
        return

    
    elif response.status_code == 500:
        print("Server Error..")
        input("Enter to exit..")
        return

    else:
        print("Website Request Failed...")
        print("Status Code:", response.status_code)
        input("Enter to exit..")
        return


    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)

    print()
    print("---------------------")
    print("Scraped Information")
    print("---------------------")

    time.sleep(00.10)
    h1 = soup.find("h1")
    if h1:
        print("[FOUND] H1:", h1.text.strip())
    else:
        print("[NOT FOUND] H1")

    h6 = soup.find("h6")
    if h6:
        print("[FOUND] H6:", h6.text.strip())
    else:
        print("[NOT FOUND] H6")

    p = soup.find("p")
    if p:
        print("[FOUND] P:", p.text.strip())
    else:
        print("[NOT FOUND] P")

    span = soup.find("span")
    if span:
        print("[FOUND] SPAN:", span.text.strip())
    else:
        print("[NOT FOUND] SPAN")

    label = soup.find("label")
    if label:
        print("[FOUND] LABEL:", label.text.strip())
    else:
        print("[NOT FOUND] LABEL")

    a = soup.find("a")
    if a:
        print("[FOUND] LINK:", a.get("href"))
    else:
        print("[NOT FOUND] LINK")

    img = soup.find("img")
    if img:
        print("[FOUND] IMAGE")
        print("    ALT:", img.get("alt"))
        print("    SRC:", img.get("src"))
    else:
        print("[NOT FOUND] IMAGE")

    div = soup.find("div")
    if div:
        print("[FOUND] DIV")
    else:
        print("[NOT FOUND] DIV")

    section = soup.find("section")
    if section:
        print("[FOUND] SECTION")
    else:
        print("[NOT FOUND] SECTION")

    article = soup.find("article")
    if article:
        print("[FOUND] ARTICLE")
    else:
        print("[NOT FOUND] ARTICLE")

    ul = soup.find("ul")
    if ul:
        print("[FOUND] UL")
    else:
        print("[NOT FOUND] UL")

    ol = soup.find("ol")
    if ol:
        print("[FOUND] OL")
    else:
        print("[NOT FOUND] OL")

    li = soup.find("li")
    if li:
        print("[FOUND] LI:", li.text.strip())
    else:
        print("[NOT FOUND] LI")

    table = soup.find("table")
    if table:
        print("[FOUND] TABLE")
    else:
        print("[NOT FOUND] TABLE")

    tr = soup.find("tr")
    if tr:
        print("[FOUND] TR")
    else:
        print("[NOT FOUND] TR")

    td = soup.find("td")
    if td:
        print("[FOUND] TD:", td.text.strip())
    else:
        print("[NOT FOUND] TD")

    th = soup.find("th")
    if th:
        print("[FOUND] TH:", th.text.strip())
    else:
        print("[NOT FOUND] TH")

    input_tag = soup.find("input")
    if input_tag:
        print("[FOUND] INPUT")
    else:
        print("[NOT FOUND] INPUT")

    button = soup.find("button")
    if button:
        print("[FOUND] BUTTON:", button.text.strip())
    else:
        print("[NOT FOUND] BUTTON")

    meta = soup.find("meta")
    if meta:
        print("[FOUND] META")
    else:
        print("[NOT FOUND] META")

    head = soup.find("head")
    if head:
        print("[FOUND] HEAD")
    else:
        print("[NOT FOUND] HEAD")

    title = soup.title
    if title:
        print("[FOUND] TITLE:", title.text.strip())
    else:
        print("[NOT FOUND] TITLE")

    print("---------------------")
    input("Enter to exit...")