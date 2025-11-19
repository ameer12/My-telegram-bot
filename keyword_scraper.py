import requests
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_google_suggestions(query):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            suggestions = response.json()[1]
            return suggestions
    except:
        return []

def generate_keywords(base_terms):
    all_keywords = []
    for term in base_terms:
        suggestions = fetch_google_suggestions(term)
        all_keywords.extend(suggestions)
    return list(set(all_keywords))

if __name__ == "__main__":
    base_terms = ["ai city", "smart traffic", "urban automation"]
    keywords = generate_keywords(base_terms)
    for kw in keywords:
        print(kw)
