import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        <span className="brand-icon" aria-hidden="true">
          <svg viewBox="0 0 64 64" width="28" height="28">
            <rect x="6" y="6" width="52" height="52" rx="14" fill="#6366f1" />
            <path d="M22 20h20v6H28v6h12v6H28v8H22V20Z" fill="#fff" />
          </svg>
        </span>
        QuizForge
      </Link>
      <p className="navbar-tagline">Master code, one quiz at a time</p>
    </nav>
  );
};

export default Navbar;
