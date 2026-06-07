import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="header">
      <Link to="/" className="header-logo">
        <h1>AI Content Generator</h1>
      </Link>
      <nav className="header-nav">
        <Link to="/my-content">My Content</Link>
        <Link to="/history">History</Link>
      </nav>
    </header>
  );
}

export default Header;
