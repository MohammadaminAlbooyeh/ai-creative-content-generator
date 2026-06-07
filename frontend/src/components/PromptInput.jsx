import React from 'react';

function PromptInput({ placeholder = 'Enter your prompt...' }) {
  return (
    <div className="prompt-input">
      <textarea
        placeholder={placeholder}
        rows={4}
        className="prompt-textarea"
      />
    </div>
  );
}

export default PromptInput;
