import React from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

const bundleTypes = ['blog_with_images', 'social_media_suite', 'marketing_campaign', 'presentation'];

function ContentBundlePage() {
  return (
    <div className="generator-page">
      <h2>Content Bundle Generator</h2>
      <div className="generator-controls">
        <TemplateSelector templates={bundleTypes} />
        <ToneSelector />
        <PromptInput placeholder="Enter your topic for the content bundle..." />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default ContentBundlePage;
