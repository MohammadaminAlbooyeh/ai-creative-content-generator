import React, { useState, useEffect } from 'react';
import api from '../services/api';
import LoadingSpinner from '../components/LoadingSpinner';

function HistoryPage() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const data = await api.get('/api/v1/history');
        setHistory(data.history || []);
      } catch (err) {
        console.error('Failed to load history:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <div className="page">
      <h2>Generation History</h2>
      {history.length === 0 ? (
        <p>No generation history yet.</p>
      ) : (
        <div className="history-list">
          {history.map((entry) => (
            <div key={entry.id} className="history-item">
              <span className="badge">{entry.content_type}</span>
              <span className="provider">{entry.provider}</span>
              <span className="date">{entry.created_at}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default HistoryPage;
