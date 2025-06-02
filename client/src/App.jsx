import { Routes, Route } from "react-router-dom";
import CombinedArticles from "./components/CombinedArticles";
import ArticlePage from "./ArticlePage"; 
import "./index.css"; 

function App() {
  return (
    <div className="app-container">
      <header className="site-header">
        <h1>📰 AI News Digest</h1>
      </header>

      <p style={{ textAlign: "center"}}>Last updated on 6/01/25</p>

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
