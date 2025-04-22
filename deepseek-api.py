import requests

url = "http://192.168.8.153:11434/api/generate"
headers = {"Content-Type": "application/json","Accept": "application/json"}
data = {
    "model": "deepseek-r1:32b",
    "prompt": "天为什么是蓝色的?",
    "max_tokens": 4090,  # 可选，最大生成的 token 数
    "stream":False
}
response = requests.post(url, json=data, headers=headers)
print(response)