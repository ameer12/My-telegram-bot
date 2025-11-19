import requests

API_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"
HEADERS = {"Content-Type": "application/json"}

def generate_content(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
    except:
        return ""

def spawn_article(topic):
    prompt = f"Write a short SEO-optimized article about: {topic}"
    return generate_content(prompt)

if __name__ == "__main__":
    topic = "AI-powered traffic systems in smart cities"
    article = spawn_article(topic)
    print(article)
