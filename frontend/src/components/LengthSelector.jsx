import React from 'react';

function LengthSelector({ value = 'medium', onChange }) {
  return (
    <div className="selector">
      <label>Length</label>
      <select value={value} onChange={(e) => onChange?.(e.target.value)}>
        <option value="short">Short</option>
        <option value="medium">Medium</option>
        <option value="long">Long</option>
      </select>
    </div>
  );
}

export default LengthSelector;
