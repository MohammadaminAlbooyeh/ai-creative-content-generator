import React from 'react';

function DownloadButton({ content, filename = 'content.txt' }) {
  const handleDownload = () => {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <button className="btn btn-download" onClick={handleDownload}>
      Download
    </button>
  );
}

export default DownloadButton;
