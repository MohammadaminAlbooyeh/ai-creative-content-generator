import React from 'react';

const tones = ['professional', 'casual', 'persuasive', 'humorous', 'authoritative', 'empathetic', 'inspirational'];

function ToneSelector({ value = 'professional', onChange }) {
  return (
    <div className="selector">
      <label>Tone</label>
      <select value={value} onChange={(e) => onChange?.(e.target.value)}>
        {tones.map((t) => (
          <option key={t} value={t}>{t}</option>
        ))}
      </select>
    </div>
  );
}

export default ToneSelector;
