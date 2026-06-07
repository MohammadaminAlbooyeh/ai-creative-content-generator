import React, { useState } from 'react';

function EditPanel({ initialContent = '', onSave }) {
  const [content, setContent] = useState(initialContent);

  return (
    <div className="edit-panel">
      <h3>Edit Content</h3>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} rows={10} />
      <button onClick={() => onSave(content)}>Save Changes</button>
    </div>
  );
}

export default EditPanel;
