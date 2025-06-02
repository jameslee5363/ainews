from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import json
import os

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

# to run the server, use: uvicorn main:app --reload --port 8000
