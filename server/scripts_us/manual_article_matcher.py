import os
import requests
from bs4 import BeautifulSoup
import json

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_article_text(url):
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, 'html.parser')

        paragraphs = soup.find_all('p')
        content = '\n'.join(p.get_text(strip=True) for p in paragraphs)
        return content[:2000]  # truncate if needed
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

pairs = []

print("Enter article URL pairs. Type 'q' to quit.")

while True:
    url1 = input("\nEnter first URL (or 'q' to quit): ").strip()
    if url1.lower() == 'q':
        break
    url2 = input("Enter second URL: ").strip()
    
    print("Fetching articles...")

    article1 = get_article_text(url1)
    article2 = get_article_text(url2)

    pairs.append({
        "url1": url1,
        "content1": article1,
        "url2": url2,
        "content2": article2
    })

    print("Pair saved.")

# Ensure target directory exists
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data_us')
os.makedirs(output_dir, exist_ok=True)

# Save JSON to data_us/matched_articles.json
output_path = os.path.join(output_dir, 'matched_articles.json')
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(pairs, f, indent=2, ensure_ascii=False)

print(f"\nAll done. Saved to '{output_path}'.")
