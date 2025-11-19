import requests
import random
import time

BACKLINK_SOURCES = [
    "https://pingler.com",
    "https://www.bulkping.com",
    "https://www.indexkings.com",
    "https://freewebsubmission.com",
    "https://addurl.nu",
]

TARGET_URL = "https://your-landing-page.com"

def send_backlink(url, source):
    try:
        response = requests.post(source, data={"url": url}, timeout=10)
        if response.status_code == 200:
            print(f"[✓] Sent to {source}")
        else:
            print(f"[✗] Failed at {source} — Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error with {source}: {e}")

def run_backlink_campaign(target_url):
    print(f"🚀 Starting backlink campaign for: {target_url}")
    for source in BACKLINK_SOURCES:
        send_backlink(target_url, source)
        time.sleep(random.uniform(1.5, 3.5))

if __name__ == "__main__":
    run_backlink_campaign(TARGET_URL)
