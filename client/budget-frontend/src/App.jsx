//import { useState } from 'react'
import './App.css'
import {BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar/';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import LoginRegister from './pages/LoginRegister';

function App() {

  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<LoginRegister />} />
      </Routes>
    </>
  );
}

export default App;