import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useSocialGeneration } from '../hooks/useSocialGeneration';

const platforms = ['twitter', 'facebook', 'instagram', 'linkedin', 'tiktok'];

function SocialMediaPage() {
  const [topic, setTopic] = useState('');
  const [platform, setPlatform] = useState('twitter');
  const [tone, setTone] = useState('casual');
  const { generateSocial, loading, error, result } = useSocialGeneration();

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    await generateSocial({ platform, topic, tone, include_hashtags: true, language: 'en' });
  };

  return (
    <div className="generator-page">
      <h2>Social Media Content Generator</h2>
      <div className="generator-controls">
        <div className="selector">
          <label>Platform</label>
          <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
            {platforms.map((p) => (
              <option key={p} value={p}>{p}</option>
            ))}
          </select>
        </div>
        <ToneSelector value={tone} onChange={setTone} />
        <PromptInput placeholder="Enter your topic for social media..." value={topic} onChange={setTopic} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={result.content} />}
    </div>
  );
}

export default SocialMediaPage;
