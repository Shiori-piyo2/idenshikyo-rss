import requests

html = requests.get(
    "https://www.idenshikyo.jp/",
    timeout=30
).text

keyword = "第18回遺伝子組換え実験安全研修会"

pos = html.find(keyword)

print(html[max(0, pos-2000):pos+3000])
