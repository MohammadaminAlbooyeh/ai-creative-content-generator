import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import LengthSelector from '../components/LengthSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useBlogGeneration } from '../hooks/useBlogGeneration';

const blogTemplates = ['listicle', 'how_to', 'tutorial', 'review', 'opinion', 'news'];

function BlogGeneratorPage() {
  const [topic, setTopic] = useState('');
  const [template, setTemplate] = useState('listicle');
  const [tone, setTone] = useState('professional');
  const [length, setLength] = useState('medium');
  const { generateBlog, loading, error, result } = useBlogGeneration();

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    await generateBlog({ topic, template, tone, length, language: 'en' });
  };

  return (
    <div className="generator-page">
      <h2>Blog Post Generator</h2>
      <div className="generator-controls">
        <TemplateSelector templates={blogTemplates} value={template} onChange={setTemplate} />
        <ToneSelector value={tone} onChange={setTone} />
        <LengthSelector value={length} onChange={setLength} />
        <PromptInput placeholder="Enter your blog topic..." value={topic} onChange={setTopic} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={result.content} />}
    </div>
  );
}

export default BlogGeneratorPage;
