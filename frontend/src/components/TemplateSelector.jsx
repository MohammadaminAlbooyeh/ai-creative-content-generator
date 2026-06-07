import React from 'react';

function TemplateSelector({ templates = [], value = '', onChange }) {
  return (
    <div className="selector">
      <label>Template</label>
      <select value={value} onChange={(e) => onChange?.(e.target.value)}>
        <option value="">Select template...</option>
        {templates.map((t) => (
          <option key={t} value={t}>{t.replace('_', ' ')}</option>
        ))}
      </select>
    </div>
  );
}

export default TemplateSelector;
