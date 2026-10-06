import requests

html = requests.get(
    "https://www.idenshikyo.jp/",
    timeout=30
).text

for keyword in [
    "No.90",
    "No.89",
    "第18回遺伝子組換え実験安全研修会",
    "第42回総会"
]:
    print("\n")
    print("=" * 50)
    print(keyword)
    print("=" * 50)

    pos = html.find(keyword)

    if pos == -1:
        print("見つからない")
    else:
        print(html[max(0, pos-1000):pos+2000])
