import React from 'react';

function PreviewPanel({ content }) {
  return (
    <div className="preview-panel">
      <h3>Preview</h3>
      <div className="preview-content">{content}</div>
    </div>
  );
}

export default PreviewPanel;
