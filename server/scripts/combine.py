from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from tqdm import tqdm

# Load API key from .env
load_dotenv()
client = OpenAI()

# Load paired articles
with open("./data/article_pairs.json", "r") as f:
    article_pairs = json.load(f)

# Function to combine article pair with GPT
def combine_articles(is_article, me_article):
    prompt = f"""
You are a neutral journalist. Create a new story from the following news stories into one balanced article.
Make sure to fairly represent all perspectives.

--- Times of Israel article ---
Title: {is_article['title']}
Content: {is_article['content']}

--- Middle East Eye article ---
Title: {me_article['title']}
Content: {me_article['content']}

First, generate a compelling and neutral title for this combined article.
Then, write a summary of the synthesized article.

Format your response like this:

Title: <your new title>
Summary: <your synthesized summary>
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that synthesizes news articles objectively."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=600
    )

    output = response.choices[0].message.content.strip()
    lines = output.split("\n", 1)
    title = lines[0].replace("Title: ", "").strip()
    summary = lines[1].replace("Summary: ", "").strip() if len(lines) > 1 else ""
    return title, summary

# Loop through pairs and combine
combined_results = []

print("Combining articles with GPT...")
for pair in tqdm(article_pairs):
    try:
        combined_title, summary = combine_articles(pair["is_article"], pair["me_article"])
        combined_results.append({
            "similarity": pair["similarity"],
            "combined_title": combined_title,
            "summary": summary,
            "is_article": pair["is_article"],
            "me_article": pair["me_article"]
        })
    except Exception as e:
        print("Error with a pair:", e)

# Save to file
output_path = "./data/combined_articles.json"
with open(output_path, "w") as f:
    json.dump(combined_results, f, indent=2)

print(f"Saved {len(combined_results)} combined articles to {output_path}")
