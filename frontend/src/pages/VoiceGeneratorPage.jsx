import React from 'react';
import PromptInput from '../components/PromptInput';
import VoiceSelector from '../components/VoiceSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

function VoiceGeneratorPage() {
  return (
    <div className="generator-page">
      <h2>Voice Generator</h2>
      <div className="generator-controls">
        <PromptInput placeholder="Enter text to convert to speech..." />
        <VoiceSelector />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default VoiceGeneratorPage;
