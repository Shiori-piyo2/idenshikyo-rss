import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.idenshikyo.jp/"


response = requests.get(BASE_URL, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="c-list_news")

print(f"見つかったテーブル数: {len(tables)}")

for i, table in enumerate(tables, start=1):
    print("\n" + "=" * 60)
    print(f"TABLE {i}")
    print("=" * 60)

    rows = table.find_all("tr")

    for row in rows:
        date_tag = row.find("th")
        link_tag = row.find("a", href=True)

        date_text = date_tag.get_text(" ", strip=True) if date_tag else ""
        title = link_tag.get_text(" ", strip=True) if link_tag else ""
        link = (
            urljoin(BASE_URL, link_tag["href"])
            if link_tag else ""
        )

        print("DATE :", date_text)
        print("TITLE:", title)
        print("LINK :", link)
        print("-" * 40)
