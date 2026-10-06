import requests

url = "https://www.idenshikyo.jp/"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)
print(response.text[:500])
