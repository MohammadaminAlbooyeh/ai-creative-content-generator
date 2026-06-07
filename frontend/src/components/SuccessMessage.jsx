import React from 'react';

function SuccessMessage({ message = 'Content generated successfully!' }) {
  return (
    <div className="success-message">
      <p>{message}</p>
    </div>
  );
}

export default SuccessMessage;
