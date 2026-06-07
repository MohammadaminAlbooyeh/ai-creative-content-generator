import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import VoiceSelector from '../components/VoiceSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useVoiceGeneration } from '../hooks/useVoiceGeneration';

function VoiceGeneratorPage() {
  const [text, setText] = useState('');
  const [voice, setVoice] = useState('Rachel');
  const { generateVoice, loading, error, result } = useVoiceGeneration();

  const handleGenerate = async () => {
    if (!text.trim()) return;
    await generateVoice({ text, voice, speed: 1.0, language: 'en', provider: 'elevenlabs' });
  };

  return (
    <div className="generator-page">
      <h2>Voice Generator</h2>
      <div className="generator-controls">
        <VoiceSelector value={voice} onChange={setVoice} />
        <PromptInput placeholder="Enter text to convert to speech..." value={text} onChange={setText} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={`Audio generated: ${result.audio || 'success'}`} />}
    </div>
  );
}

export default VoiceGeneratorPage;
