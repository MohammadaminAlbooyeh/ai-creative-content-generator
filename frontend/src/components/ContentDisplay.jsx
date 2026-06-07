import React from 'react';

function ContentDisplay({ content = null }) {
  if (!content) {
    return <div className="content-display placeholder">Generated content will appear here</div>;
  }
  return (
    <div className="content-display">
      {content}
    </div>
  );
}

export default ContentDisplay;
