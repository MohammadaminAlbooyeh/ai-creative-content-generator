import React from 'react';

function LoadingSpinner() {
  return (
    <div className="loading-spinner">
      <div className="spinner"></div>
      <p>Generating...</p>
    </div>
  );
}

export default LoadingSpinner;
