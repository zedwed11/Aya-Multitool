import requests

def run():
    print("Tool Launched....")
    print("----------------------")

    from bs4 import BeautifulSoup

    print("===============================================================")
    print("Code Scraper by @zed")
    print("Input the website you want to scrape and it will return the code of the website")
    print("================================================================================")

    website = input("Website You want to scrape: ")

    # replaces https:// so it can be added back in later
    # this is to avoid double https://
    website = website.replace("https://", "")
    website = website.replace("http://", "")

    print(f"Scraping {website}...")
    website = "https://" + website

    try:
        # sends a response to the website to get its HTML/code
        response = requests.get(website, timeout=10)

        if response.status_code == 200:
            print(f"Successfully scraped {website}")
            print("---------------------------------------------------------------")
            print(response.text)

        else:
            print(f"Failed to scrape {website}. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred while scraping {website}: {e}")

    # keeps the tool open
    input("Press Enter to exit...")