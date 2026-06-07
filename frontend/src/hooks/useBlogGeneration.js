import { useContentGeneration } from './useContentGeneration';

export function useBlogGeneration() {
  const { generate, loading, error, result } = useContentGeneration();

  const generateBlog = async (params) => {
    return generate('/api/v1/generate/blog', params);
  };

  return { generateBlog, loading, error, result };
}
