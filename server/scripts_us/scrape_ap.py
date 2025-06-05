import requests
from bs4 import BeautifulSoup
import json
import os
import time

BASE_URL = "https://apnews.com"
LIST_URL = f"{BASE_URL}/us-news"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_article_links():
    res = requests.get(LIST_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = []

    for item in soup.select(".PageList-items-item")[:3]:
        title_tag = item.select_one(".PagePromo-title a")
        if title_tag:
            title = title_tag.get_text(strip=True)
            url = title_tag["href"]
            if not url.startswith("http"):
                url = BASE_URL + url
            articles.append({"title": title, "url": url})
    return articles

def scrape_article_content(url):
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")
        content_div = soup.find("div", class_="RichTextStoryBody RichTextBody")
        if not content_div:
            return ""
        paragraphs = content_div.find_all("p")
        return "\n".join(p.get_text(strip=True) for p in paragraphs)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data_us")
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, "ap.json")
    output = []

    print("Fetching article list...")
    articles = get_article_links()

    for article in articles:
        print(f"Scraping: {article['title']}")
        content = scrape_article_content(article["url"])
        output.append({
            "source": "AP News",
            "title": article["title"],
            "url": article["url"],
            "content": content
        })
        time.sleep(1)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
