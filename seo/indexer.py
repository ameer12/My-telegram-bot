import requests

async def ping_google(url: str) -> bool:
    endpoint = f"https://www.google.com/ping?sitemap={url}"
    return requests.get(endpoint).status_code == 200

async def ping_bing(url: str) -> bool:
    endpoint = f"https://www.bing.com/ping?sitemap={url}"
    return requests.get(endpoint).status_code == 200

async def ping_yandex(url: str) -> bool:
    endpoint = f"https://webmaster.yandex.com/ping?sitemap={url}"
    return requests.get(endpoint).status_code == 200

async def ping_pingomatic(url: str) -> bool:
    endpoint = "http://pingomatic.com/ping/"
    data = {
        "title": "SEO Ping",
        "blogurl": url,
        "rssurl": url,
        "chk_blogs": "on",
        "chk_feedburner": "on",
        "chk_tailrank": "on",
        "chk_superfeedr": "on"
    }
    return requests.post(endpoint, data=data).status_code == 200

async def process_link(url: str) -> dict:
    """
    Executes all indexing methods and returns a dictionary of results.
    """
    results = {
        "Google": await ping_google(url),
        "Bing": await ping_bing(url),
        "Yandex": await ping_yandex(url),
        "Pingomatic": await ping_pingomatic(url)
    }
    return results
