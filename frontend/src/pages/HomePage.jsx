import React from 'react';
import ContentCard from '../components/ContentCard';

const generators = [
  { title: 'Blog Posts', description: 'Generate blog posts, listicles, how-tos', path: '/blog', icon: '📝' },
  { title: 'Social Media', description: 'Create posts for Instagram, Twitter, LinkedIn', path: '/social', icon: '📱' },
  { title: 'Emails', description: 'Write welcome, promotional, newsletter emails', path: '/email', icon: '✉️' },
  { title: 'Images', description: 'Generate images with DALL-E', path: '/image', icon: '🎨' },
  { title: 'Voice', description: 'Convert text to speech', path: '/voice', icon: '🎤' },
  { title: 'Video Scripts', description: 'Generate video and podcast scripts', path: '/video', icon: '🎬' },
  { title: 'Content Bundles', description: 'Create multi-modal content suites', path: '/bundle', icon: '📦' },
];

function HomePage() {
  return (
    <div className="home-page">
      <h1>AI Creative Content Generator</h1>
      <p>Select a content type to get started</p>
      <div className="generator-grid">
        {generators.map((g) => (
          <ContentCard key={g.path} {...g} />
        ))}
      </div>
    </div>
  );
}

export default HomePage;
