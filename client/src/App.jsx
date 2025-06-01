import { Routes, Route } from "react-router-dom";
import CombinedArticles from "./components/CombinedArticles";
import ArticlePage from "./ArticlePage"; 
import "./index.css"; 

function App() {
  return (
    <div>
      <header style={{ textAlign: "center", padding: "1rem 0", borderBottom: "1px solid #ddd" }}>
        <h1 style={{ margin: 0 }}>📰 AI News Digest</h1>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<CombinedArticles />} />
          <Route path="/article/:id" element={<ArticlePage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
