import React from 'react';

function LengthSelector() {
  return (
    <div className="selector">
      <label>Length</label>
      <select>
        <option value="short">Short</option>
        <option value="medium">Medium</option>
        <option value="long">Long</option>
      </select>
    </div>
  );
}

export default LengthSelector;
