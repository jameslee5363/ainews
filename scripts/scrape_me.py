import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

ME_BASE_URL = "https://www.middleeasteye.net"
ME_TOPIC_URL = f"{ME_BASE_URL}/topics/israel-war-gaza"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def me_get_article_links():
    res = requests.get(ME_TOPIC_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    links = []
    main_links = soup.find_all('h2', class_='main-article-title')
    tile_links = soup.find_all('a', class_='mee-tile-title')

    for h2 in main_links:
        a = h2.find('a')
        if a and 'href' in a.attrs:
            links.append(ME_BASE_URL + a['href'])

    for a in tile_links:
        if 'href' in a.attrs:
            links.append(ME_BASE_URL + a['href'])

    return list(set(links))  # De-duplicate


def me_extract_article_text(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    # Get title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Untitled"

    # Get content
    paragraphs = soup.find_all("p")
    content = "\n\n".join(p.get_text(strip=True) for p in paragraphs)

    # Get date (optional enhancement)
    date_tag = soup.find("time")
    published = date_tag.get("datetime") if date_tag else None

    return {
        "source": "Middle East Eye",
        "title": title,
        "url": url,
        "published": published,
        "content": content
    }


# Main runner
if __name__ == "__main__":
    print("=== MIDDLE EAST EYE ARTICLES ===")
    me_article_links = me_get_article_links()

    articles = []
    for i, url in enumerate(me_article_links[:5]):  # Limit for now
        print(f"Fetching Article {i+1}: {url}")
        article_data = me_extract_article_text(url)
        articles.append(article_data)

    # Write to JSON (overwrite mode)
    with open("data/me_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(articles)} articles to me_articles.json")
