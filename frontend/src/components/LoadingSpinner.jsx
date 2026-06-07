import React from 'react';

const LoadingSpinner = ({ message = 'Loading...', size = 'md' }) => {
  return (
    <div className={`loading-spinner loading-spinner--${size}`}>
      <div className="spinner"></div>
      {message && <p className="loading-spinner-message">{message}</p>}
    </div>
  );
};

export default LoadingSpinner;
