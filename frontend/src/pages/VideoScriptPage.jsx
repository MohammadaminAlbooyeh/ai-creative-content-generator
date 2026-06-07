import React from 'react';
import PromptInput from '../components/PromptInput';
import ToneSelector from '../components/ToneSelector';
import LengthSelector from '../components/LengthSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

function VideoScriptPage() {
  return (
    <div className="generator-page">
      <h2>Video Script Generator</h2>
      <div className="generator-controls">
        <PromptInput placeholder="Enter your video topic..." />
        <ToneSelector />
        <LengthSelector />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default VideoScriptPage;
