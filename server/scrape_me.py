import requests
from bs4 import BeautifulSoup

# Scraper for Middle East Eye articles

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

    return links[:3]  # Limit for brevity

def me_extract_article_text(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    paragraphs = soup.find_all("p")
    content = "\n\n".join(p.get_text(strip=True) for p in paragraphs)
    return content


# Main runner
if __name__ == "__main__":

    print("=== MIDDLE EAST EYE ARTICLES ===")
    me_article_links = me_get_article_links()
    for i, url in enumerate(me_article_links):
        print(f"\n--- ME Article {i+1}: {url} ---\n")
        article_text = me_extract_article_text(url)
        print(article_text[:3000])
        print("\n" + "="*80 + "\n")

    
