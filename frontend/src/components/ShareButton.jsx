import React from 'react';

function ShareButton({ content }) {
  const handleShare = async () => {
    if (navigator.share) {
      await navigator.share({ text: content });
    }
  };

  return (
    <button className="btn btn-share" onClick={handleShare}>
      Share
    </button>
  );
}

export default ShareButton;
