import React from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import LengthSelector from '../components/LengthSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

const blogTemplates = ['listicle', 'how_to', 'tutorial', 'review', 'opinion', 'news'];

function BlogGeneratorPage() {
  return (
    <div className="generator-page">
      <h2>Blog Post Generator</h2>
      <div className="generator-controls">
        <TemplateSelector templates={blogTemplates} />
        <ToneSelector />
        <LengthSelector />
        <PromptInput placeholder="Enter your blog topic..." />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default BlogGeneratorPage;
