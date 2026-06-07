import React from 'react';

function GenerationButton({ onClick, loading = false }) {
  return (
    <button className="generate-btn" onClick={onClick} disabled={loading}>
      {loading ? 'Generating...' : 'Generate'}
    </button>
  );
}

export default GenerationButton;
