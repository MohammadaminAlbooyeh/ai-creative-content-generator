import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useContentGeneration } from '../hooks/useContentGeneration';

const emailTypes = ['welcome', 'promotional', 'newsletter', 'transactional', 'followup'];

function EmailGeneratorPage() {
  const [subject, setSubject] = useState('');
  const [emailType, setEmailType] = useState('welcome');
  const [tone, setTone] = useState('professional');
  const { generate, loading, error, result } = useContentGeneration();

  const handleGenerate = async () => {
    if (!subject.trim()) return;
    await generate('/api/v1/generate/email', {
      email_type: emailType, subject, tone, key_points: [], language: 'en',
    });
  };

  return (
    <div className="generator-page">
      <h2>Email Generator</h2>
      <div className="generator-controls">
        <TemplateSelector templates={emailTypes} value={emailType} onChange={setEmailType} />
        <ToneSelector value={tone} onChange={setTone} />
        <PromptInput placeholder="Enter your email subject and key points..." value={subject} onChange={setSubject} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={result.content} />}
    </div>
  );
}

export default EmailGeneratorPage;
