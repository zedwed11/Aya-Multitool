import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

SITES = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Keybase": "https://keybase.io/{}",
    "Medium": "https://medium.com/@{}",
    "Dev.to": "https://dev.to/{}",
    "CodePen": "https://codepen.io/{}",
    "Replit": "https://replit.com/@{}",
    "PyPI": "https://pypi.org/user/{}/",
    "npm": "https://www.npmjs.com/~{}",
    "Docker Hub": "https://hub.docker.com/u/{}",
    "Hugging Face": "https://huggingface.co/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Mixcloud": "https://www.mixcloud.com/{}/",
    "Bandcamp": "https://bandcamp.com/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "Letterboxd": "https://letterboxd.com/{}/",
    "Keybase": "https://keybase.io/{}",
    "About.me": "https://about.me/{}",
    "Gravatar": "https://gravatar.com/{}",
    "Instructables": "https://www.instructables.com/member/{}/",
    "Thingiverse": "https://www.thingiverse.com/{}",
    "Codeberg": "https://codeberg.org/{}",
    "SourceForge": "https://sourceforge.net/u/{}/",
    "Bitbucket": "https://bitbucket.org/{}",
    "Buy Me a Coffee": "https://www.buymeacoffee.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Ko-fi": "https://ko-fi.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Rumble": "https://rumble.com/c/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "WordPress": "https://{}.wordpress.com/",
    "Blogger": "https://{}.blogspot.com/",
    "Telegram": "https://t.me/{}",
    "Keybase Chat": "https://keybase.io/{}",
    "Product Hunt": "https://www.producthunt.com/@{}",
    "Foursquare": "https://foursquare.com/{}",
    "500px": "https://500px.com/p/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "Imgur": "https://imgur.com/user/{}",
    "Giphy": "https://giphy.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "ArtStation": "https://www.artstation.com/{}",
    "Sketchfab": "https://sketchfab.com/{}",
    "Canva": "https://www.canva.com/p/{}",
    "Duolingo": "https://www.duolingo.com/profile/{}",
    "Chess.com": "https://www.chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "AniList": "https://anilist.co/user/{}/",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "Xbox": "https://xboxgamertag.com/search/{}",
    "NameMC": "https://namemc.com/profile/{}",
    "Minecraft Forums": "https://www.minecraftforum.net/members/{}",
    "SpigotMC": "https://www.spigotmc.org/members/{}",
    "Planet Minecraft": "https://www.planetminecraft.com/member/{}/",
    "Lego Ideas": "https://ideas.lego.com/profile/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "Archive.org": "https://archive.org/details/@{}",
    "Goodreads Profile": "https://www.goodreads.com/user/show/{}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "AllTrails": "https://www.alltrails.com/members/{}",
    "Disqus": "https://disqus.com/by/{}/",
    "Gravatar Profile": "https://gravatar.com/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "Stack Exchange": "https://stackexchange.com/users/{}",
    "Super User": "https://superuser.com/users/{}",
    "Ask Ubuntu": "https://askubuntu.com/users/{}",
    "Server Fault": "https://serverfault.com/users/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "LeetCode": "https://leetcode.com/u/{}/",
    "Codewars": "https://www.codewars.com/users/{}",
    "Exercism": "https://exercism.org/profiles/{}",
    "Khan Academy": "https://www.khanacademy.org/profile/{}",
    "Scratch": "https://scratch.mit.edu/users/{}/",
    "Glitch": "https://glitch.com/@{}",
    "Observable": "https://observablehq.com/@{}",
    "Gist": "https://gist.github.com/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Forumotion": "https://www.forumotion.com/",
    "Myspace": "https://myspace.com/{}",
    "VK": "https://vk.com/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "Bluesky": "https://bsky.app/profile/{}",
    "Threads": "https://www.threads.net/@{}",
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "X": "https://x.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Minds": "https://www.minds.com/{}",
    "Gab": "https://gab.com/{}",
    "MeWe": "https://mewe.com/i/{}",
    "Guns.lol": "https://guns.lol/{}",
}


def check_site(site, url, username):
    try:
        target = url.format(username)

        response = requests.get(
            target,
            timeout=8,
            allow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        # 200 usually means the profile/page exists.
        if response.status_code == 200:
            return site, target, True

        return site, target, False

    except requests.RequestException:
        return site, url.format(username), False


def run():
    print("Mini Sherlock Launched....")
    print("-------------------------")
    print()

    username = input("Enter username: ").strip()

    if not username:
        print("You didn't enter a username.")
        input("Enter to exit...")
        return

    print()
    print(f"Searching for: {username}")
    print(f"Checking {len(SITES)} websites...")
    print("=" * 60)

    found = []
    not_found = []

    with ThreadPoolExecutor(max_workers=15) as executor:

        jobs = [
            executor.submit(check_site, site, url, username)
            for site, url in SITES.items()
        ]

        for job in as_completed(jobs):
            site, url, exists = job.result()

            if exists:
                found.append((site, url))
                print(f"[+] FOUND     {site}: {url}")
            else:
                not_found.append(site)
                print(f"[-] Not found {site}")

    print()
    print("=" * 60)
    print(f"Search complete!")
    print(f"Found: {len(found)}")
    print(f"Not found: {len(not_found)}")
    print("=" * 60)

    if found:
        print()
        print("FOUND ACCOUNTS")
        print("--------------")

        for site, url in found:
            print(f"[+] {site}")
            print(f"    {url}")

    print()
    input("Enter to exit...")