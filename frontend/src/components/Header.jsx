import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import authService from '../services/auth';

function Header() {
  const [isAuthenticated, setIsAuthenticated] = useState(authService.isAuthenticated());
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const check = () => setIsAuthenticated(authService.isAuthenticated());
    window.addEventListener('storage', check);
    return () => window.removeEventListener('storage', check);
  }, []);

  const handleLogout = () => {
    authService.logout();
    setIsAuthenticated(false);
    setMenuOpen(false);
    navigate('/login');
  };

  return (
    <header className="header">
      <Link to="/" className="header-logo">
        <h1>AI Content Generator</h1>
      </Link>
      <nav className="header-nav">
        {isAuthenticated ? (
          <>
            <Link to="/my-content">My Content</Link>
            <Link to="/history">History</Link>
            <button className="btn btn-outline btn-sm" onClick={handleLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login" className="btn btn-outline btn-sm">Sign In</Link>
            <Link to="/signup" className="btn btn-primary btn-sm">Sign Up</Link>
          </>
        )}
      </nav>
      <button className="header-menu-toggle" onClick={() => setMenuOpen(!menuOpen)}>
        menu
      </button>
      {menuOpen && (
        <div className="header-mobile-menu">
          <Link to="/" onClick={() => setMenuOpen(false)}>Home</Link>
          <Link to="/my-content" onClick={() => setMenuOpen(false)}>My Content</Link>
          <Link to="/history" onClick={() => setMenuOpen(false)}>History</Link>
          {isAuthenticated ? (
            <button onClick={handleLogout}>Logout</button>
          ) : (
            <>
              <Link to="/login" onClick={() => setMenuOpen(false)}>Sign In</Link>
              <Link to="/signup" onClick={() => setMenuOpen(false)}>Sign Up</Link>
            </>
          )}
        </div>
      )}
    </header>
  );
}

export default Header;
