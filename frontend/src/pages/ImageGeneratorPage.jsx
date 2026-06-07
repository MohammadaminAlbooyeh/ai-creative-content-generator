import React from 'react';
import PromptInput from '../components/PromptInput';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

function ImageGeneratorPage() {
  return (
    <div className="generator-page">
      <h2>Image Generator</h2>
      <div className="generator-controls">
        <PromptInput placeholder="Describe the image you want to generate..." />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default ImageGeneratorPage;
