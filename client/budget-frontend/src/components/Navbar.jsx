import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from '../assets/logo.png'; // Adjust the path based on your folder structure

function Navbar() {
  return (
      /* Nav Bar Color & width */
    <nav className="navbar navbar-expand-lg" style={{ 
      backgroundColor: '#95beaa' ,
      width: '100%',
      padding: '0.8rem 1rem',
      }}>

      <div className="container-fluid">
        {/* Logo and Brand Name */}
        <Link 
        className="navbar-brand d-flex align-items-center" 
        href="#"
        to="/"
        style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#b86872' }}
        >
          <img 
            src={logo} 
            alt="Budgeting 101 Logo" 
            style={{ height: '50px', marginRight: '10px' }} 
          />
          <span className="text">Budgeting 101</span>
        </Link>

        {/* Navbar Toggle (for mobile view) */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Navbar Links */}
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link 
              to="/"
              className="nav-link text-white" 
              style={{ color: '#fff', fontWeight: 'bold', fontSize: '1.2rem' }}
              >Home</Link>
            </li>
            <li className="nav-item">
              <Link 
              to="Dashboard"
              className="nav-link text-white" 
              style={{ color: '#fff', fontWeight: 'bold',fontSize: '1.2rem' }}
              >Dashboard</Link>
            </li>
          </ul>

          {/* Login Section (aligned to the right) */}
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <Link 
              to="Login"
              className="nav-link" 
              style={{ color: '#b86872', fontWeight: 'bold', fontSize: '1.2rem' }}
              >Login</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
