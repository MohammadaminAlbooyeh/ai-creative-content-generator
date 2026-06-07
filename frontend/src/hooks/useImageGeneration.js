import { useContentGeneration } from './useContentGeneration';

export function useImageGeneration() {
  const { generate, loading, error, result } = useContentGeneration();

  const generateImage = async (params) => {
    return generate('/api/v1/generate/image', params);
  };

  return { generateImage, loading, error, result };
}
