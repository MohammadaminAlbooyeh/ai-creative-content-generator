import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import ErrorBoundary from './components/ErrorBoundary';
import LoadingSpinner from './components/LoadingSpinner';
import ProtectedRoute from './components/ProtectedRoute';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
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
      <ErrorBoundary>
        <div className="app">
          <Header />
          <div className="app-layout">
            <Sidebar />
            <main className="app-main">
              <Suspense fallback={<LoadingSpinner message="Loading page..." />}>
                <Routes>
                  <Route path="/login" element={<LoginPage />} />
                  <Route path="/signup" element={<SignupPage />} />
                  <Route path="/" element={<HomePage />} />
                  <Route path="/blog" element={<ProtectedRoute><BlogGeneratorPage /></ProtectedRoute>} />
                  <Route path="/social" element={<ProtectedRoute><SocialMediaPage /></ProtectedRoute>} />
                  <Route path="/email" element={<ProtectedRoute><EmailGeneratorPage /></ProtectedRoute>} />
                  <Route path="/image" element={<ProtectedRoute><ImageGeneratorPage /></ProtectedRoute>} />
                  <Route path="/voice" element={<ProtectedRoute><VoiceGeneratorPage /></ProtectedRoute>} />
                  <Route path="/video" element={<ProtectedRoute><VideoScriptPage /></ProtectedRoute>} />
                  <Route path="/bundle" element={<ProtectedRoute><ContentBundlePage /></ProtectedRoute>} />
                  <Route path="/my-content" element={<ProtectedRoute><MyContentPage /></ProtectedRoute>} />
                  <Route path="/history" element={<ProtectedRoute><HistoryPage /></ProtectedRoute>} />
                </Routes>
              </Suspense>
            </main>
          </div>
        </div>
      </ErrorBoundary>
    </Router>
  );
}

export default App;
