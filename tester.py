import requests
url = "http://127.0.0.1:8000/predict"
payload = {"text": "Trump muslim hillary"}
res = requests.post(url, json=payload)

print(res.status_code)
print(res.json())