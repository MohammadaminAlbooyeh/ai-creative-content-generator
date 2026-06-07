import { useState } from 'react';
import api from '../services/api';

export function useBundleGeneration() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const generate = async (params) => {
    setLoading(true);
    setError(null);
    try {
      const data = await api.post('/api/v1/generate/bundle', params);
      setResult(data);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { generate, loading, error, result };
}
