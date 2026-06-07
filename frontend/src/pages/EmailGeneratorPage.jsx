import React from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';

const emailTemplates = ['welcome', 'promotional', 'newsletter', 'transactional', 'followup'];

function EmailGeneratorPage() {
  return (
    <div className="generator-page">
      <h2>Email Generator</h2>
      <div className="generator-controls">
        <TemplateSelector templates={emailTemplates} />
        <ToneSelector />
        <PromptInput placeholder="Enter your email subject and key points..." />
        <GenerationButton />
      </div>
      <ContentDisplay />
    </div>
  );
}

export default EmailGeneratorPage;
