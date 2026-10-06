import requests

url = "https://www.idenshikyo.jp/"

response = requests.get(url, timeout=30)

print(response.text)
`
