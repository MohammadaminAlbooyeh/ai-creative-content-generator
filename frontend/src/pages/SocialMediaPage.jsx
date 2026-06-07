import React from 'react';
import PromptInput from '../components/PromptInput';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

function SocialMediaPage() {
  return (
    <div className="generator-page">
      <h2>Social Media Content Generator</h2>
      <div className="generator-controls">
        <PromptInput placeholder="Enter your topic for social media..." />
        <ToneSelector />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default SocialMediaPage;
