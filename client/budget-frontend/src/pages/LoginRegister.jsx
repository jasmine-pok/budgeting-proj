import React, { useState } from "react";
import "../assets/styles/loginregisters.css"; // Add styling here
import { apiRequest} from "../utils/apiRequest";


const LoginRegister = () => {
  const [isLogin, setIsLogin] = useState(true); // Toggle between login and register
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Function to handle form submission
  const handleSubmit = async (e) => {
    const backendUrl = '';
    e.preventDefault();

    const endpoint = isLogin ? `${backendUrl}/auth/login/` : `${backendUrl}/auth/register/`; // Backend endpoints
    const userData = isLogin ?{ username, password } :  { username, email, password };

    try {
       const response = await fetch(endpoint, {
        method: "POST",
        credentials: "include",  // This allows cookies to be stored
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
        
      });
   const result = await response.json(); // ✅ Read response JSON only once
    console.log("Login API Response:", result);
    
        if (response.ok)  {
        // Handle login response (store tokens)
        
          alert("Login successful!");
            // Redirect to the home page if login is successful
              /*setTimeout(() => {
                window.location.href = "/";
              }, 2000);*/
        }else {
         //commented out for demo
          // alert("Error: " + (result.detail || "Unable to process request"));
        }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="login-register-container">
    <div className= "login-box">
      <h2>{isLogin ? "Login" : "Register"}</h2>
      
      {!isLogin && (
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
            required
          />
        </div>  
      )}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter username"
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter password"
            required
          />
        </div>
        
        
        <button type="submit" className="btn btn-primary">
          {isLogin ? "Login" : "Register"}
        </button>
      </form>
      <div className="toggle-container">
        <p>
          {isLogin
            ? "Don't have an account? "
            : "Already have an account? "}
          <button
            type="button"
            onClick={() => setIsLogin(!isLogin)}
            className="btn btn-link"
          >
            {isLogin ? "Register" : "Login"}
          </button>
        </p>
        </div>  
      </div>
    </div>
  );
};
export default LoginRegister;
