import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

export default function USArticlePage() {
  const { id } = useParams();
  const [article, setArticle] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/combined-articles-us`)
      .then((res) => res.json())
      .then((data) => {
        const item = data[Number(id)];
        if (item) setArticle(item);
        else setError("Article not found");
      })
      .catch(() => setError("Failed to load article"));
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!article) return <p>Loading...</p>;

  return (
    <div className="article-page">
      <h1>{article.combined_title}</h1>
      <p style={{ lineHeight: 1.6 }}>{article.article}</p>

      <hr />
      <h4>Original Sources:</h4>
      <ul>
        <li><a href={article.source_1.url} target="_blank" rel="noreferrer">Source 1</a></li>
        <li><a href={article.source_2.url} target="_blank" rel="noreferrer">Source 2</a></li>
      </ul>
    </div>
  );
}