import React from 'react';

const voices = ['Rachel', 'Domi', 'Bella', 'Antoni', 'Elli', 'Josh', 'Arnold', 'Adam', 'Sam'];

function VoiceSelector() {
  return (
    <div className="selector">
      <label>Voice</label>
      <select>
        {voices.map((v) => (
          <option key={v} value={v}>{v}</option>
        ))}
      </select>
    </div>
  );
}

export default VoiceSelector;
