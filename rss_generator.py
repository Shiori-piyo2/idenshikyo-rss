import requests

html = requests.get(
    "https://www.idenshikyo.jp/",
    timeout=30
).text

for keyword in [
    "おしらせ",
    "組換え生物等委員会通信"
]:
    pos = html.find(keyword)

    print("\n" + "=" * 50)
    print(keyword)
    print("=" * 50)

    if pos != -1:
        print(html[max(0, pos-1000):pos+2000])
    else:
        print("見つからない")
