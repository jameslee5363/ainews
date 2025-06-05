import { Routes, Route, Link, Navigate } from "react-router-dom";
import CombinedArticlesMiddleEast from "./components/CombinedArticlesMiddleEast";
import CombinedArticlesUS from "./components/CombinedArticlesUS";
import MEArticlePage from "./MEArticlePage";
import USArticlePage from "./USArticlePage";
import "./index.css";

function App() {
  return (
    <div className="app-container">
      <header className="site-header">
        <h1>📰 AI News Digest</h1>

        {/* Navigation Menu */}
        <nav className="top-nav">
          <Link to="/us" className="nav-link">US News</Link>
          <Link to="/middle-east" className="nav-link">Middle East News</Link>
        </nav>
      </header>

      <p style={{ textAlign: "center" }}>Last updated on 6/05/25</p>

      <main>
        <Routes>
          <Route path="/" element={<Navigate to="/us" />} />
          <Route path="/us" element={<CombinedArticlesUS />} />
          <Route path="/middle-east" element={<CombinedArticlesMiddleEast />} />
          <Route path="/me-article/:id" element={<MEArticlePage />} />
          <Route path="/us-article/:id" element={<USArticlePage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
