import { useContentGeneration } from './useContentGeneration';

export function useVoiceGeneration() {
  const { generate, loading, error, result } = useContentGeneration();

  const generateVoice = async (params) => {
    return generate('/api/v1/generate/voice', params);
  };

  return { generateVoice, loading, error, result };
}
