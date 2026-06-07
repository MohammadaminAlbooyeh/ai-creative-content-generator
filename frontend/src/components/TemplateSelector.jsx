import React from 'react';

function TemplateSelector({ templates = [] }) {
  return (
    <div className="selector">
      <label>Template</label>
      <select>
        {templates.map((t) => (
          <option key={t} value={t}>{t.replace('_', ' ')}</option>
        ))}
      </select>
    </div>
  );
}

export default TemplateSelector;
