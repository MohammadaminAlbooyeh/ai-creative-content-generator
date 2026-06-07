import { useContentGeneration } from './useContentGeneration';

export function useSocialGeneration() {
  const { generate, loading, error, result } = useContentGeneration();

  const generateSocial = async (params) => {
    return generate('/api/v1/generate/social', params);
  };

  return { generateSocial, loading, error, result };
}
