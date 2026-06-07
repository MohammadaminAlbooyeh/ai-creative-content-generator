import React, { useState } from 'react';
import PromptInput from '../components/PromptInput';
import GenerationButton from '../components/GenerationButton';
import ContentDisplay from '../components/ContentDisplay';
import ErrorDisplay from '../components/ErrorDisplay';
import LoadingSpinner from '../components/LoadingSpinner';
import { useImageGeneration } from '../hooks/useImageGeneration';

function ImageGeneratorPage() {
  const [prompt, setPrompt] = useState('');
  const [size, setSize] = useState('1024x1024');
  const { generateImage, loading, error, result } = useImageGeneration();

  const handleGenerate = async () => {
    if (!prompt.trim()) return;
    await generateImage({ prompt, size, num_images: 1, provider: 'dall-e' });
  };

  return (
    <div className="generator-page">
      <h2>Image Generator</h2>
      <div className="generator-controls">
        <div className="selector">
          <label>Size</label>
          <select value={size} onChange={(e) => setSize(e.target.value)}>
            <option value="256x256">256x256</option>
            <option value="512x512">512x512</option>
            <option value="1024x1024">1024x1024</option>
            <option value="1792x1024">1792x1024</option>
          </select>
        </div>
        <PromptInput placeholder="Describe the image you want to generate..." value={prompt} onChange={setPrompt} />
        <GenerationButton onClick={handleGenerate} loading={loading} />
      </div>
      {loading && <LoadingSpinner />}
      {error && <ErrorDisplay message={error} />}
      {result && <ContentDisplay content={result.images?.join(', ') || result.content} />}
    </div>
  );
}

export default ImageGeneratorPage;
