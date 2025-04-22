import requests

url = "http://192.168.8.145:11434/v1/completions"
payload = {
    "model": "deepseek-r1:32b",
    "prompt": "给我讲一个笑话",
    "max_tokens": 4090
}
response = requests.post(url, json=payload)
print(response.json())