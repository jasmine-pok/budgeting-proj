import { useContext, useState, useEffect } from 'react';
import { AppContext } from '../context/AppContext';
import { apiRequest } from "../utils/apiRequest";  // Import apiRequest
import '../Dashboard.css';

const Dashboard = () => {
    const {
      monthlyEarnings,
      essentialExpenses,
      nonEssentialExpenses,
      savingsGoal,
    } = useContext(AppContext);

  const [totalEssentialExpenses, setTotalEssentialExpenses] = useState(0);
  const [totalNonEssentialExpenses, setTotalNonEssentialExpenses] = useState(0);
  const [timeToSavingsGoal, setTimeToSavingsGoal] = useState('');

  useEffect(() => {
    const fetchDashboardData = async () => {
      const backendUrl = 'https://5f18979a-8527-486e-b5f3-f3f6f3d7c611.mock.pstmn.io';
      try {
        fetch(`${backendUrl}/essential-expenses-total`, {
          headers: {
            "Accept": "application/json", // Ensure we expect JSON
          },
        })
      .then(res => res.text()) // Log as raw text before parsing
      .then(text => {
        console.log("Raw Response Text:", text);
        try {
          const jsonData = JSON.parse(text);
          console.log("Parsed JSON:", jsonData);
          if (jsonData && typeof jsonData === "object" && jsonData.total !== undefined) {
            console.log("Extracted Total:", jsonData.total);
          } else {
            console.error("JSON does not contain 'total':", jsonData);
          }
          
        } catch (error) {
          console.error("JSON Parsing Error:", error);
        }
      })
      .catch(err => console.error("Fetch Error:", err));
          
        // Essential Expenses
        // Essential Expenses
const essentialResponse = await fetch(`${backendUrl}/essential-expenses-total`);
console.log("Full Essential Response:", essentialResponse); // Logs the full response

if (essentialResponse.ok) {
  try {
    // Ensure we correctly read the response as JSON
    const essentialData = await essentialResponse.json();
    console.log("Parsed Essential Data:", essentialData);

    // Ensure that we correctly extract the 'total' field
    if (essentialData && typeof essentialData.total === "number") {
      setTotalEssentialExpenses(essentialData.total); // Correctly set the value
    } else {
      console.error("Parsed essential data does not contain a valid 'total' field:", essentialData);
    }
  } catch (error) {
    console.error("Failed to parse essential expenses response as JSON:", error);
  }
} else {
  console.error(`Failed to fetch essential expenses: ${essentialResponse.status}`);
}

        // Non-Essential Expenses
        const nonEssentialResponse = await fetch(`${backendUrl}/non-essential-expenses-total`);
        const nonEssentialText = await nonEssentialResponse.text();
        console.log('Non-Essential Response Raw:', nonEssentialText);
        const nonEssentialData = JSON.parse(nonEssentialText);
        setTotalNonEssentialExpenses(nonEssentialData.total);
    
        // Time to Savings Goal
        const savingsResponse = await fetch(`${backendUrl}/time-to-savings-goal`);
        const savingsText = await savingsResponse.text();
        console.log('Savings Response Raw:', savingsText);
        setTimeToSavingsGoal(savingsText); // Directly set plain text response
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      }
    };  
    const isValidJSON = (text) => {
      try {
        JSON.parse(text);
        return true;
      } catch (e) {
        return false;
      }
    };
    fetchDashboardData();
  }, []);
  
  
    return (
      <div className="dashboard-container">
        <h2>Welcome to the Dashboard</h2>
        
        {/* Quadrant 1: Monthly Earnings */}
        <div className= "flex-container">
        <div className="flex-item">
        <h4>Monthly Earnings</h4>
        <p>${monthlyEarnings}</p>
      </div>

        {/* Quadrant 2: Savings Goal */}
        <div className="flex-item">
          <h4>Savings Goal</h4>
          <p>${savingsGoal}</p>
        </div>

        {/* Quadrant 3: Display Essential Expenses */}
        <div className="flex-item">
        <h4>Essential Expenses:</h4>
        <ul>
          {essentialExpenses.map((expense, index) => (
            <li key={index}>
              {expense.name}: ${expense.amount}
            </li>
          ))}
        </ul>
        </div>
  
        {/*Quadrant 4:  Display Non-Essential Expenses */}
        <div className="flex-item">
        <h4>Non-Essential Expenses:</h4>
        <ul>
          {nonEssentialExpenses.map((expense, index) => (
            <li key={index}>
              {expense.name}: ${expense.amount}
            </li>
          ))}
            </ul>
        </div>
         {/* Quadrant 5:  Time to reach goal*/}
         <div className="flex-item full-width">
          <h4>Time to reach Savings Goal:</h4>
          <p>{timeToSavingsGoal}</p>
        </div>
        {/* Quadrant 6: Display Total Essential Expenses */}
        <div className="flex-item full-width">
          <h4>Total Essential Expenses:</h4>
          <p>${totalEssentialExpenses}</p>
        </div>

        {/* Quadrant 7: Display Total Non-Essential Expenses */}
        <div className="flex-item full-width">
          <h4>Total Non-Essential Expenses:</h4>
          <p>${totalNonEssentialExpenses}</p>
        </div>

      </div>
      </div>
    );
  };
  
  export default Dashboard;
  
