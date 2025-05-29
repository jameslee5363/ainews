from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

# Step 1: Load topic page with Selenium
driver.get("https://www.timesofisrael.com/israel-and-the-region/")
time.sleep(3)  # Wait for the page to fully load

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Step 2: Extract first 3 article links (just 3 for now)
links = []

# main headline link
link_tag = soup.select_one("div.headline a")
if link_tag:
    links.append(link_tag["href"])

# other articles
articles = soup.select("div.item.template1.news div.headline a")

for a_tag in articles[:3]:
    if a_tag and 'href' in a_tag.attrs:
        links.append(a_tag['href'])

# Step 3: Visit each article and extract <p> from div.the-content
for link in links:
    print(f"\n--- Article: {link} ---")
    driver.get(link)
    time.sleep(2)  # Let the article page load

    article_soup = BeautifulSoup(driver.page_source, "html.parser")
    content_div = article_soup.find("div", class_="the-content")

    if content_div:
        for p in content_div.find_all("p"):
            print(p.get_text(strip=True))
    else:
        print("Article content not found.")

driver.quit()
