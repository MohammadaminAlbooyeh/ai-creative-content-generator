import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useContentGeneration } from '../hooks/useContentGeneration';

const bundleTypes = ['blog_with_images', 'social_media_suite', 'marketing_campaign', 'presentation', 'content_suite'];

function ContentBundlePage() {
  const [topic, setTopic] = useState('');
  const [bundleType, setBundleType] = useState('blog_with_images');
  const [tone, setTone] = useState('professional');
  const { generate, loading, error, result } = useContentGeneration();

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    await generate('/api/v1/generate/bundle', {
      bundle_type: bundleType, topic, tone, include_images: true, include_voice: false, language: 'en',
    });
  };

  return (
    <div className="generator-page">
      <h2>Content Bundle Generator</h2>
      <div className="generator-controls">
        <div className="selector">
          <label>Bundle Type</label>
          <select value={bundleType} onChange={(e) => setBundleType(e.target.value)}>
            {bundleTypes.map((b) => (
              <option key={b} value={b}>{b.replace(/_/g, ' ')}</option>
            ))}
          </select>
        </div>
        <ToneSelector value={tone} onChange={setTone} />
        <PromptInput placeholder="Enter your topic for the content bundle..." value={topic} onChange={setTopic} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={typeof result.content === 'string' ? result.content : JSON.stringify(result.content, null, 2)} />}
    </div>
  );
}

export default ContentBundlePage;
