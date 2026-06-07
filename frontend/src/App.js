import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import HomePage from './pages/HomePage';
import BlogGeneratorPage from './pages/BlogGeneratorPage';
import SocialMediaPage from './pages/SocialMediaPage';
import EmailGeneratorPage from './pages/EmailGeneratorPage';
import ImageGeneratorPage from './pages/ImageGeneratorPage';
import VoiceGeneratorPage from './pages/VoiceGeneratorPage';
import VideoScriptPage from './pages/VideoScriptPage';
import ContentBundlePage from './pages/ContentBundlePage';
import MyContentPage from './pages/MyContentPage';
import HistoryPage from './pages/HistoryPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="app-layout">
          <Sidebar />
          <main className="app-main">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/blog" element={<BlogGeneratorPage />} />
              <Route path="/social" element={<SocialMediaPage />} />
              <Route path="/email" element={<EmailGeneratorPage />} />
              <Route path="/image" element={<ImageGeneratorPage />} />
              <Route path="/voice" element={<VoiceGeneratorPage />} />
              <Route path="/video" element={<VideoScriptPage />} />
              <Route path="/bundle" element={<ContentBundlePage />} />
              <Route path="/my-content" element={<MyContentPage />} />
              <Route path="/history" element={<HistoryPage />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
