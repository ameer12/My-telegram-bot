import requests
import random
import time

PROXIES = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080"
]

SEARCH_QUERY = "site:your-landing-page.com"
TARGET_URL = "https://your-landing-page.com"

def simulate_click(proxy):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        search_url = f"https://www.google.com/search?q={SEARCH_QUERY}"
        response = session.get(search_url, headers=headers, timeout=10)
        if TARGET_URL in response.text:
            session.get(TARGET_URL, headers=headers, timeout=10)
            print(f"[✓] Click simulated via {proxy}")
        else:
            print(f"[✗] Target not found in search via {proxy}")
    except Exception as e:
        print(f"[!] Error with {proxy}: {e}")

def run_ctr_simulation():
    for proxy in PROXIES:
        simulate_click(proxy)
        time.sleep(random.uniform(5, 10))

if __name__ == "__main__":
    run_ctr_simulation()
