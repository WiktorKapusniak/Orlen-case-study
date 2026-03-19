import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import json
import re

def get_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text(strip=True) for p in paragraphs[:10])

    return text

client = OpenAI()

def analyze_article(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": """You are a strict data extraction system.
Return ONLY valid JSON. No explanations."""
                },
                {
                    "role": "user",
                    "content": f"""
Extract:
- keywords (max 5)
- sentiment (positive/neutral/negative)
- main_trend (one short sentence)

Return JSON.

Text:
{text}
"""
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content
        result = re.sub(r"```json|```", "", result).strip()

        return json.loads(result)

    except Exception as e:
        print("Błąd:", e)
        return None


def analyze_global_trend(articles):
    trends = [
        a["analysis"]["main_trend"]
        for a in articles
        if a["analysis"]
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Summarize multiple article trends into one main trend."
            },
            {
                "role": "user",
                "content": f"""
Here are trends from multiple articles:

{trends}

Find ONE main overarching trend.

Return one sentence only.
"""
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

url = "https://biznesalert.pl/category/energetyka/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = []

for article in soup.select("article")[:5]:
    title = article.find("h2").text.strip()
    print(f"Analizuję: {title}")
    link = article.find("a")["href"]
    content = get_article_content(link)
    anylysis = analyze_article(content)

    articles.append({
        "title": title,
        "link": link,
        "analysis": anylysis,
    })


global_trend = analyze_global_trend(articles)


with open("results.json", "w", encoding="utf-8") as f:
    json.dump({
        "articles": articles,
        "global_trend": global_trend
    }, f, indent=2, ensure_ascii=False)
