import React, { useState, useEffect } from 'react';
import { contentAPI } from '../services/content_api';
import ContentCard from '../components/ContentCard';
import LoadingSpinner from '../components/LoadingSpinner';

function MyContentPage() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchContent = async () => {
      try {
        const data = await contentAPI.getAll();
        setItems(data.items || []);
      } catch (err) {
        console.error('Failed to load content:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchContent();
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <div className="page">
      <h2>My Content</h2>
      {items.length === 0 ? (
        <p>No content saved yet. Generate some content to see it here.</p>
      ) : (
        <div className="content-list">
          {items.map((item) => (
            <div key={item.id} className="content-item">
              <h3>{item.title || item.content_type}</h3>
              <p className="content-type">{item.content_type}</p>
              <p className="content-date">{item.created_at}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default MyContentPage;
