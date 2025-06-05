import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

export default function MEArticlePage() {
  const { id } = useParams();
  const [article, setArticle] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/combined-articles`)
    //fetch("http://localhost:8000/api/combined-articles")
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
    <div style={{ maxWidth: '800px', margin: '2rem auto', padding: '1rem' }}>
      <h1>{article.combined_title}</h1>
      <p style={{ lineHeight: 1.6 }}>{article.summary}</p>

      <hr />
      <h4>Original Sources:</h4>
      <ul>
        <li><a href={article.is_article.url} target="_blank">Times of Israel</a></li>
        <li><a href={article.me_article.url} target="_blank">Middle East Eye</a></li>
      </ul>
    </div>
  );
}
