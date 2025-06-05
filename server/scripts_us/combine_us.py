# combining American news articles

# combine_matched_articles.py

# combine_matched_articles.py

import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

# Load OpenAI API key from .env
load_dotenv()
client = OpenAI()

# Load matched article pairs
input_path = os.path.join(os.path.dirname(__file__), '..', 'data_us', 'matched_articles.json')
with open(input_path, "r", encoding="utf-8") as f:
    matched_pairs = json.load(f)

# Function to combine two articles using GPT
def combine_articles(content1, content2):
    prompt = f"""
You are a neutral journalist. Create a new story from the following two articles into one balanced article.
Make sure to fairly represent all perspectives.

--- Article 1 ---
{content1}

--- Article 2 ---
{content2}

First, generate a compelling and neutral title for this combined article.
Then, write a new, full, synthesized article.

Format your response like this:

Title: <your new title>
Article: <your synthesized article>
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that synthesizes news articles objectively."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000  # increased for longer article
    )

    output = response.choices[0].message.content.strip()
    lines = output.split("\n", 1)
    title = lines[0].replace("Title: ", "").strip()
    article = lines[1].replace("Article: ", "").strip() if len(lines) > 1 else ""
    return title, article

# Combine all matched pairs
combined_articles = []

print("Combining articles with GPT...")
for pair in tqdm(matched_pairs):
    try:
        content1 = pair["content1"]
        content2 = pair["content2"]
        url1 = pair["url1"]
        url2 = pair["url2"]

        combined_title, combined_article = combine_articles(content1, content2)

        combined_articles.append({
            "combined_title": combined_title,
            "article": combined_article,
            "source_1": {"url": url1, "content": content1},
            "source_2": {"url": url2, "content": content2}
        })
    except Exception as e:
        print("Error processing a pair:", e)

# Save the combined articles
output_path = os.path.join(os.path.dirname(__file__), '..', 'data_us', 'combined_articles.json')
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(combined_articles, f, indent=2, ensure_ascii=False)

print(f"Saved {len(combined_articles)} combined articles to {output_path}")
