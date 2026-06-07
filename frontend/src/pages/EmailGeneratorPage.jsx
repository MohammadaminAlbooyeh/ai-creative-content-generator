import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import TemplateSelector from '../components/TemplateSelector';
import ToneSelector from '../components/ToneSelector';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useEmailGeneration } from '../hooks/useEmailGeneration';
import { validatePrompt } from '../utils/validators';

const emailTypes = ['welcome', 'promotional', 'newsletter', 'transactional', 'followup'];

function EmailGeneratorPage() {
  const [subject, setSubject] = useState('');
  const [emailType, setEmailType] = useState('welcome');
  const [tone, setTone] = useState('professional');
  const [localError, setLocalError] = useState(null);
  const { generate, loading, error, result } = useEmailGeneration();

  const handleGenerate = async () => {
    setLocalError(null);
    const validationError = validatePrompt(subject);
    if (validationError) {
      setLocalError(validationError);
      return;
    }
    try {
      await generate({ email_type: emailType, subject, tone, key_points: [], language: 'en' });
    } catch {
      // handled by hook
    }
  };

  const displayError = localError || error;

  return (
    <div className="generator-page">
      <h1>Email Generator</h1>
      <p className="page-description">Create professional emails for any occasion</p>
      <div className="generator-form">
        <div className="form-row">
          <TemplateSelector templates={emailTypes} value={emailType} onChange={setEmailType} />
          <ToneSelector value={tone} onChange={setTone} />
        </div>
        <PromptInput placeholder="Enter your email subject and key points..." value={subject} onChange={setSubject} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {displayError && <ErrorDisplay message={displayError} variant="error" />}
      {loading && <LoadingSpinner message="Generating email..." />}
      {result && (
        <div className="generator-result">
          <h2>Generated Email</h2>
          <div className="generator-result-content">{result.content}</div>
        </div>
      )}
    </div>
  );
}

export default EmailGeneratorPage;
