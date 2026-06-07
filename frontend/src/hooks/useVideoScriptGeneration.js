import { useContentGeneration } from './useContentGeneration';

export function useVideoScriptGeneration() {
  const { generate, loading, error, result } = useContentGeneration();

  const generateVideoScript = async (params) => {
    return generate('/api/v1/generate/video', params);
  };

  return { generateVideoScript, loading, error, result };
}
