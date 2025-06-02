// src/components/CombinedArticles.jsx
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../index.css"; 

export default function CombinedArticles() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/combined-articles`)
      .then((r) => r.json())
      .then((data) =>
        Array.isArray(data)
          ? setArticles(data)
          : setError("Unexpected API response")
      )
      .catch(() => setError("Could not load articles"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="articles-container">
      {articles.map((item, idx) => (
        <Link key={idx} to={`/article/${idx}`} className="article-card">
          <h3 className="article-title">{item.combined_title || "Untitled"}</h3>
          <p className="article-summary">{item.summary}</p>
        </Link>
      ))}
    </div>
  );
}
