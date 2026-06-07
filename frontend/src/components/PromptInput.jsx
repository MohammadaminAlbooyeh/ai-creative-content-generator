import React from 'react';

function PromptInput({ placeholder = 'Enter your prompt...', value = '', onChange }) {
  return (
    <div className="prompt-input">
      <textarea
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange?.(e.target.value)}
        rows={4}
        className="prompt-textarea"
      />
    </div>
  );
}

export default PromptInput;
