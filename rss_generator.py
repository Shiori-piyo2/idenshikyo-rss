import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin
from datetime import datetime, timezone

BASE_URL = "https://www.idenshikyo.jp/"


def get_items():
    html = requests.get(BASE_URL, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")

    tables = soup.find_all("table", class_="c-list_news")

    for i, table in enumerate(tables, start=1):

        print("=" * 50)
        print("TABLE", i)
        print("=" * 50)

        rows = table.find_all("tr")

        for row in rows[:3]:
            print(row.get_text(" ", strip=True))

    return []

items = get_items()

fg = FeedGenerator()

fg.id(BASE_URL)
fg.title("遺伝子研究安全管理協議会 RSS")
fg.link(href=BASE_URL)
fg.description("おしらせ・組換え生物等委員会通信")

for item in items:
    fe = fg.add_entry()

    fe.id(item["link"])
    fe.title(item["title"])
    fe.link(href=item["link"])
    fe.description(item["date"])

    fe.pubDate(datetime.now(timezone.utc))

fg.rss_file("feed.xml")

print(f"RSS作成完了: {len(items)}件")
