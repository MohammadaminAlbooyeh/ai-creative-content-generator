import React, { useEffect } from 'react';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorDisplay from '../components/ErrorDisplay';
import { useContentHistory } from '../hooks/useContentHistory';

function HistoryPage() {
  const { items, loading, error, fetchHistory, deleteItem } = useContentHistory();

  useEffect(() => {
    fetchHistory();
  }, [fetchHistory]);

  if (loading) return <LoadingSpinner message="Loading history..." />;

  return (
    <div className="generator-page">
      <h1>Generation History</h1>
      <p className="page-description">View your past content generations</p>

      {error && <ErrorDisplay message={error} variant="error" />}

      {items.length === 0 ? (
        <p style={{ color: '#6b7280', padding: '24px 0' }}>No generation history yet. Start creating content!</p>
      ) : (
        <div className="content-grid">
          {items.map((entry) => (
            <div key={entry.id} className="content-card">
              <div className="content-card-header">
                <span className="content-card-title">{entry.content_type}</span>
                <span style={{ fontSize: '0.75rem', color: '#6b7280' }}>{entry.provider}</span>
              </div>
              <div className="content-card-body">
                {entry.content?.substring(0, 150)}
                {(entry.content?.length || 0) > 150 ? '...' : ''}
              </div>
              <div className="content-card-footer">
                <span style={{ fontSize: '0.75rem', color: '#9ca3af' }}>
                  {entry.created_at ? new Date(entry.created_at).toLocaleDateString() : ''}
                </span>
                <button className="btn btn-danger btn-sm" onClick={() => deleteItem(entry.id)}>
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default HistoryPage;
