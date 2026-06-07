import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import ToneSelector from '../components/ToneSelector';
import LengthSelector from '../components/LengthSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useVideoScriptGeneration } from '../hooks/useVideoScriptGeneration';

const videoTypes = ['youtube', 'tiktok', 'instagram_reels', 'podcast', 'educational'];

function VideoScriptPage() {
  const [topic, setTopic] = useState('');
  const [videoType, setVideoType] = useState('youtube');
  const [tone, setTone] = useState('engaging');
  const [duration, setDuration] = useState('medium');
  const { generateVideoScript, loading, error, result } = useVideoScriptGeneration();

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    await generateVideoScript({ topic, video_type: videoType, duration, tone, language: 'en' });
  };

  return (
    <div className="generator-page">
      <h2>Video Script Generator</h2>
      <div className="generator-controls">
        <div className="selector">
          <label>Video Type</label>
          <select value={videoType} onChange={(e) => setVideoType(e.target.value)}>
            {videoTypes.map((v) => (
              <option key={v} value={v}>{v.replace('_', ' ')}</option>
            ))}
          </select>
        </div>
        <ToneSelector value={tone} onChange={setTone} />
        <LengthSelector value={duration} onChange={setDuration} />
        <PromptInput placeholder="Enter your video topic..." value={topic} onChange={setTopic} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={result.content} />}
    </div>
  );
}

export default VideoScriptPage;
