import React from 'react';
import { Link } from 'react-router-dom';

const links = [
  { path: '/blog', label: 'Blog Posts', icon: '📝' },
  { path: '/social', label: 'Social Media', icon: '📱' },
  { path: '/email', label: 'Emails', icon: '✉️' },
  { path: '/image', label: 'Images', icon: '🎨' },
  { path: '/voice', label: 'Voice', icon: '🎤' },
  { path: '/video', label: 'Video Scripts', icon: '🎬' },
  { path: '/bundle', label: 'Content Bundles', icon: '📦' },
];

function Sidebar() {
  return (
    <aside className="sidebar">
      <nav>
        {links.map((l) => (
          <Link key={l.path} to={l.path} className="sidebar-link">
            <span className="sidebar-icon">{l.icon}</span>
            {l.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;
