import { useState, useEffect } from 'react';
import api from '../services/api';

export function useContentHistory() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchHistory = async () => {
      setLoading(true);
      try {
        const data = await api.get('/api/v1/history');
        setHistory(data.history || []);
      } finally {
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  return { history, loading };
}
