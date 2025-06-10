import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import ToneSlider from "./components/ToneSlider";

export default function USArticlePage() {
  const { id } = useParams();
  const [article, setArticle] = useState(null);
  const [error, setError] = useState(null);
  const [toneIdx, setToneIdx] = useState(1);
  const [toneText, setToneText] = useState("");

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

  useEffect(() => {
    if (!article) return;
    const tone = ["liberal", "center", "conservative"][toneIdx];
    fetch(
      `${import.meta.env.VITE_API_BASE_URL}/api/article-tone?section=us&id=${id}&tone=${tone}`
    )
      .then((res) => res.json())
      .then((data) => setToneText(data.text))
      .catch(() => setToneText(article.article));
  }, [toneIdx, article, id]);

  if (error) return <p>{error}</p>;
  if (!article) return <p>Loading...</p>;

  return (
    <div className="article-page">
      <ToneSlider value={toneIdx} onChange={setToneIdx} />
      <h1>{article.combined_title}</h1>
      <p style={{ lineHeight: 1.6 }}>{toneText}</p>

      <hr />
      <h4>Original Sources:</h4>
      <ul>
        <li><a href={article.source_1.url} target="_blank" rel="noreferrer">Source 1</a></li>
        <li><a href={article.source_2.url} target="_blank" rel="noreferrer">Source 2</a></li>
      </ul>
    </div>
  );
}
