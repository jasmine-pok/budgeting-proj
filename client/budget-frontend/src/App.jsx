import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar/';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>

<div className="alert alert-warning" role="alert">
  This is a Bootstrap alert!
</div>
 <div className="App">
      <Navbar />
      <h1>Budgeting 101</h1>
      {/* Other components and content can go here */}
    </div>
    <h2>Budgeting 101</h2>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
