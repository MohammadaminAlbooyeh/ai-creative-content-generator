import React from 'react';

function ErrorDisplay({ message = 'An error occurred' }) {
  return (
    <div className="error-display">
      <p>Error: {message}</p>
    </div>
  );
}

export default ErrorDisplay;
