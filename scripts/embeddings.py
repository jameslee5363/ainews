from openai import OpenAI
import json
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm

load_dotenv()
# --- Set API key ---
client = OpenAI()

# --- Load Articles ---
with open("./data/is.json") as f:
    is_articles = json.load(f)

with open("./data/me_articles.json") as f:
    me_articles = json.load(f)

# --- Get Embedding ---
def get_embedding(text, model="text-embedding-3-small"):
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding

# --- Compute Embeddings ---
print("Embedding Times of Israel titles...")
is_embeddings = [get_embedding(article["title"]) for article in tqdm(is_articles)]

print("Embedding Middle East Eye titles...")
me_embeddings = [get_embedding(article["title"]) for article in tqdm(me_articles)]

# --- Compute Cosine Similarity Matrix ---
similarity_matrix = cosine_similarity(is_embeddings, me_embeddings)

# --- Flatten similarity matrix into (i, j, similarity) tuples ---
similarity_pairs = []

for i in range(len(is_articles)):
    for j in range(len(me_articles)):
        similarity_pairs.append((i, j, similarity_matrix[i][j]))

# --- Sort all possible pairs by descending similarity ---
similarity_pairs.sort(key=lambda x: x[2], reverse=True)

# --- Greedy pairing for top 10 ---
used_is_indices = set()
used_me_indices = set()
pairs = []

for i, j, score in similarity_pairs:
    if i not in used_is_indices and j not in used_me_indices:
        pairs.append({
            "similarity": round(score, 4),
            "is_article": {
                "title": is_articles[i]["title"],
                "content": is_articles[i]["content"],
                "url": is_articles[i]["url"]
            },
            "me_article": {
                "title": me_articles[j]["title"],
                "content": me_articles[j]["content"],
                "url": me_articles[j]["url"]
            }
        })
        used_is_indices.add(i)
        used_me_indices.add(j)

        if len(pairs) == 10:
            break
        
# --- Save to JSON ---
os.makedirs("data", exist_ok=True)
with open("data/article_pairs.json", "w") as f:
    json.dump(pairs, f, indent=2)

print(f"Saved {len(pairs)} article pairs to data/article_pairs.json")
