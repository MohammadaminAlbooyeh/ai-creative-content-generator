import React from 'react';

const tones = ['professional', 'casual', 'persuasive', 'humorous', 'authoritative', 'empathetic', 'inspirational'];

function ToneSelector() {
  return (
    <div className="selector">
      <label>Tone</label>
      <select>
        {tones.map((t) => (
          <option key={t} value={t}>{t}</option>
        ))}
      </select>
    </div>
  );
}

export default ToneSelector;
