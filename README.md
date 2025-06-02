# NeutralPress   
AI-powered news synthesis from diverse sources to reduce political bias.

## Overview

NeutralPress is a full-stack web application that uses GPT-4 and embeddings to combine news articles covering the same event from politically diverse sources. By analyzing and merging these perspectives, the app aims to generate synthesized stories that reduce ideological bias and provide a more balanced narrative.

## Live Demo

[ainews-rho.vercel.app](https://ainews-rho.vercel.app/)

## Features

- Web scraping pipelines for real-time article collection
- GPT-4 powered content synthesis
- Cosine similarity matching using `text-embedding-3-small` to pair related articles
- Focused on high-conflict topics (e.g., Israel-Palestine) with plans to expand
- Fully deployed MVP using Vercel (frontend) and Render (backend)

## Tech Stack

- **Frontend:** React (Vite), Tailwind CSS  
- **Backend:** FastAPI, Python, OpenAI API  
- **AI/ML:** GPT-4 for synthesis, `text-embedding-3-small` for similarity scoring  
- **Deployment:** Vercel (frontend), Render (backend)

## Local Setup

Clone the repo and run the frontend and backend separately.

### Backend (FastAPI)

```bash
cd server
cd app
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000

### Frontend (React)
cd client
npm install
npm run dev
