from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import json
import os


def apply_tone(text: str, tone: str) -> str:
    """Return the text rewritten with a very simple tone prefix."""
    tone = tone.lower()
    if tone == "liberal":
        return f"[Liberal tone] {text}"
    if tone == "conservative":
        return f"[Conservative tone] {text}"
    return text

app = FastAPI()

# Allow frontend (Vite) on localhost:5173 to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/combined-articles")
def get_combined_articles():
    path = Path(__file__).resolve().parent.parent / "data" / "combined_articles.json"
    if not os.path.exists(path):
        return JSONResponse({"error": "Data not found"}, status_code=404)

    with open(path) as f:
        data = json.load(f)          # ← this is already a list
    return JSONResponse(data)        # ← send list, not {"data": list}

@app.get("/api/combined-articles-us")
def get_combined_articles_us():
    path = Path(__file__).resolve().parent.parent / "data_us" / "combined_articles.json"
    if not os.path.exists(path):
        return JSONResponse({"error": "Data not found"}, status_code=404)

    with open(path) as f:
        data = json.load(f)          # ← this is already a list
    return JSONResponse(data)        # ← send list, not {"data": list}


@app.get("/api/article-tone")
def get_article_tone(section: str, id: int, tone: str = "center"):
    """Return the requested article rewritten in the given tone."""
    if section == "me":
        path = Path(__file__).resolve().parent.parent / "data" / "combined_articles.json"
        key = "summary"
    else:
        path = Path(__file__).resolve().parent.parent / "data_us" / "combined_articles.json"
        key = "article"

    if not os.path.exists(path):
        return JSONResponse({"error": "Data not found"}, status_code=404)

    with open(path) as f:
        data = json.load(f)

    if id < 0 or id >= len(data):
        return JSONResponse({"error": "Article not found"}, status_code=404)

    item = data[id]
    text = apply_tone(item.get(key, ""), tone)
    return JSONResponse({"combined_title": item.get("combined_title"), "text": text})

# to run the server, use: uvicorn main:app --reload --port 8000
