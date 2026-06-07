import React from 'react';

function SaveButton({ onSave }) {
  return (
    <button className="btn btn-save" onClick={onSave}>
      Save
    </button>
  );
}

export default SaveButton;
