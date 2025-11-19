import requests
import random
import time

INDEXING_ENDPOINTS = [
    "https://www.google.com/ping?sitemap=https://your-landing-page.com/sitemap.xml",
    "https://www.bing.com/ping?sitemap=https://your-landing-page.com/sitemap.xml",
    "https://rpc.pingomatic.com/",
    "https://www.indexnow.org/indexnow",
]

def submit_to_indexing(endpoint):
    try:
        response = requests.get(endpoint, timeout=10)
        if response.status_code == 200:
            print(f"[✓] Submitted to {endpoint}")
        else:
            print(f"[✗] Failed at {endpoint} — Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error with {endpoint}: {e}")

def run_indexing_boost():
    for endpoint in INDEXING_ENDPOINTS:
        submit_to_indexing(endpoint)
        time.sleep(random.uniform(2, 4))

if __name__ == "__main__":
    run_indexing_boost()
