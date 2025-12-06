import requests

url = "https://example.com"

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("Server is healthy ✔")
    else:
        print(f"Server error: {response.status_code}")
except Exception as e:
    print("Server is down ❌")
    print("Error:", e)
