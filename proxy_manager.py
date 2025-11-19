import requests
import random

PROXY_LIST_URL = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"

def fetch_proxies():
    try:
        response = requests.get(PROXY_LIST_URL, timeout=10)
        if response.status_code == 200:
            proxies = response.text.strip().split("\n")
            return [p for p in proxies if p]
    except:
        return []

def get_random_proxy(proxies):
    return random.choice(proxies) if proxies else None

if __name__ == "__main__":
    proxies = fetch_proxies()
    proxy = get_random_proxy(proxies)
    print(proxy)
