import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin
from datetime import datetime, timezone

BASE_URL = "https://www.idenshikyo.jp/"


def get_items():
    html = requests.get(BASE_URL, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")

    items = []

    tables = soup.find_all("table", class_="c-list_news")

    # TABLE1=おしらせ、TABLE2=委員会通信
    target_tables = tables[:2]

    for table in target_tables:

        rows = table.find_all("tr")

        for row in rows:
            date_tag = row.find("th")
            link_tag = row.find("a", href=True)

            if not link_tag:
                continue

            date_text = date_tag.get_text(" ", strip=True) if date_tag else ""

            title = link_tag.get_text(" ", strip=True)

            link = urljoin(BASE_URL, link_tag["href"])

            category = "おしらせ"

            if "gmo_news" in link:
                category = "委員会通信"

            items.append({
                "date": date_text,
                "title": f"【{category}】{title}",
                "link": link
            })

    return items


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
``
