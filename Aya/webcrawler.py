import asyncio
import logging
import random
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger("AdvancedCrawler")


class AdvancedCrawler:

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",

        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]

    def __init__(
        self,
        seed_url: str,
        max_workers: int = 5,
        max_pages: int = 50,
        timeout: int = 10
    ):
        self.seed_url = seed_url
        self.max_pages = max_pages
        self.timeout = timeout

        self.semaphore = asyncio.Semaphore(max_workers)
        self.queue = asyncio.Queue()

        self.visited_urls = set()
        self.domain = urlparse(seed_url).netloc

        self.queue.put_nowait(seed_url)

    def _get_random_headers(self) -> dict:
        return {
            "User-Agent": random.choice(self.USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                      "image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }

    async def fetch_page(
        self,
        session: aiohttp.ClientSession,
        url: str
    ) -> str:

        async with self.semaphore:

            await asyncio.sleep(random.uniform(0.5, 1.5))

            try:
                headers = self._get_random_headers()

                async with session.get(
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    allow_redirects=True
                ) as response:

                    if response.status != 200:
                        logger.warning(
                            f"HTTP {response.status} encountered at: {url}"
                        )
                        return ""

                    content_type = response.headers.get(
                        "Content-Type",
                        ""
                    )

                    if "text/html" not in content_type:
                        logger.debug(
                            f"Skipping non-HTML content at: {url}"
                        )
                        return ""

                    return await response.text()

            except Exception as e:
                logger.error(
                    f"Network exception at {url}: {str(e)}"
                )
                return ""

    def extract_links(
        self,
        html: str,
        current_url: str
    ) -> list:

        found_links = []

        soup = BeautifulSoup(html, "html.parser")

        for anchor in soup.find_all("a", href=True):

            href = anchor["href"]

            absolute_url = urljoin(
                current_url,
                href
            )

            parsed = urlparse(
                absolute_url
            )._replace(fragment="")

            normalized_url = parsed.geturl()

            if parsed.netloc == self.domain:
                found_links.append(normalized_url)

        return found_links

    async def worker(
        self,
        session: aiohttp.ClientSession
    ):

        while True:

            current_url = await self.queue.get()

            try:

                if current_url in self.visited_urls:
                    continue

                if len(self.visited_urls) >= self.max_pages:
                    continue

                self.visited_urls.add(current_url)

                logger.info(
                    f"Indexing [{len(self.visited_urls)}/{self.max_pages}]: "
                    f"{current_url}"
                )

                html = await self.fetch_page(
                    session,
                    current_url
                )

                if html:

                    links = self.extract_links(
                        html,
                        current_url
                    )

                    for link in links:

                        if (
                            link not in self.visited_urls
                            and len(self.visited_urls) < self.max_pages
                        ):
                            await self.queue.put(link)

            finally:
                self.queue.task_done()

    async def run(self):

        connector = aiohttp.TCPConnector(
            limit_per_host=10,
            ttl_dns_cache=300
        )

        async with aiohttp.ClientSession(
            connector=connector
        ) as session:

            worker_count = self.semaphore._value

            workers = [
                asyncio.create_task(
                    self.worker(session)
                )
                for _ in range(worker_count)
            ]

            await self.queue.join()

            for worker in workers:
                worker.cancel()

            await asyncio.gather(
                *workers,
                return_exceptions=True
            )

        logger.info(
            "Crawler finished. Total pages crawled: "
            f"{len(self.visited_urls)}"
        )


def run():

    print("Tool Launched....")
    print("----------------------")

    target_url = input(
        "Enter the URL you want to crawl: "
    ).strip()

    if not target_url:
        print("No URL entered.")
        return

    if not target_url.startswith(("http://", "https://")):
        target_url = "https://" + target_url

    try:

        parsed = urlparse(target_url)

        if not parsed.netloc:
            print("Invalid URL.")
            return

        print()
        print("Starting crawler...")
        print(f"Target: {target_url}")
        print("Maximum pages: 30")
        print()

        crawler = AdvancedCrawler(
            seed_url=target_url,
            max_workers=8,
            max_pages=30
        )

        asyncio.run(crawler.run())

    except KeyboardInterrupt:

        print("\nCrawler stopped.")

    except Exception as e:

        print(f"Error: {e}")

    input("\nEnter to exit...")