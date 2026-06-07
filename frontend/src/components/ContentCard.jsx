import React from 'react';
import { Link } from 'react-router-dom';

function ContentCard({ title, description, path, icon }) {
  return (
    <Link to={path} className="content-card">
      <span className="card-icon">{icon}</span>
      <h3>{title}</h3>
      <p>{description}</p>
    </Link>
  );
}

export default ContentCard;
