import React from 'react';

const icons = {
  error: '!',
  warning: '!',
  info: 'i',
};

const ErrorDisplay = ({ message, variant = 'error', onDismiss }) => {
  if (!message) return null;

  return (
    <div className={`error-display error-display--${variant}`}>
      <span className="error-display-icon">{icons[variant] || '!'}</span>
      <span className="error-display-message">{message}</span>
      {onDismiss && (
        <button className="error-display-dismiss" onClick={onDismiss}>
          x
        </button>
      )}
    </div>
  );
};

export default ErrorDisplay;
