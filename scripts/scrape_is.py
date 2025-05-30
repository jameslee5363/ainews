from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

IS_BASE_URL = "https://www.timesofisrael.com"
TOPIC_URL = f"{IS_BASE_URL}/israel-and-the-region/"

def scrape_toi_articles():
    driver = webdriver.Chrome()
    driver.get(TOPIC_URL)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    links = []

    # Main headline
    main_link = soup.select_one("div.headline a")
    if main_link and 'href' in main_link.attrs:
        links.append(main_link["href"])

    # Other articles
    articles = soup.select("div.item.template1.news div.headline a")
    for a_tag in articles[:3]:  # limit to 3
        if a_tag and 'href' in a_tag.attrs:
            links.append(a_tag['href'])

    story_data = []

    for link in links:
        full_url = link if link.startswith("http") else IS_BASE_URL + link
        print(f"Fetching: {full_url}")
        driver.get(full_url)
        time.sleep(2)

        article_soup = BeautifulSoup(driver.page_source, "html.parser")

        title_tag = article_soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        content_div = article_soup.find("div", class_="the-content")
        if content_div:
            paragraphs = content_div.find_all("p")
            content = "\n\n".join(p.get_text(strip=True) for p in paragraphs)
        else:
            content = "Content not found."

        story_data.append({
            "source": "Times of Israel",
            "title": title,
            "url": full_url,
            "content": content
        })

    driver.quit()

    with open("data/is.json", "w", encoding="utf-8") as f:
        json.dump(story_data, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(story_data)} articles to is.json")


if __name__ == "__main__":
    scrape_toi_articles()
