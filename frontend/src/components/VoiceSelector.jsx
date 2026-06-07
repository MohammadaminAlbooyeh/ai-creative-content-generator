import React from 'react';

const voices = ['Rachel', 'Domi', 'Bella', 'Antoni', 'Elli', 'Josh', 'Arnold', 'Adam', 'Sam'];

function VoiceSelector({ value = 'Rachel', onChange }) {
  return (
    <div className="selector">
      <label>Voice</label>
      <select value={value} onChange={(e) => onChange?.(e.target.value)}>
        {voices.map((v) => (
          <option key={v} value={v}>{v}</option>
        ))}
      </select>
    </div>
  );
}

export default VoiceSelector;
