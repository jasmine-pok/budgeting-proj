import { useState } from "react";
import { useContext } from 'react';
import { useNavigate } from "react-router-dom";  // Import useNavigate hook for redirection
import { AppContext } from '../context/AppContext';
import { apiRequest } from "../utils/apiRequest";  // Import apiRequest

function Home() {
  //use to redirect user after submitting info
    const navigate = useNavigate();  

   // Access context values and setters
   const {
    monthlyEarnings,
    setMonthlyEarnings,
    essentialExpenses,
    setEssentialExpenses,
    nonEssentialExpenses,
    setNonEssentialExpenses,
    savingsGoal,
    setSavingsGoal,
  } = useContext(AppContext);

  // Function to handle adding a new expense row
  const addEssentialExpenseRow = () => {
    setEssentialExpenses([...essentialExpenses, { name: '', amount: '' }]);
  };

  const addNonEssentialExpenseRow = () => {
    setNonEssentialExpenses([...nonEssentialExpenses, { name: '', amount: '' }]);
  };


  // Function to handle the form submission
  const submitForm = async (e) => {
    e.preventDefault();  // Prevent the default form submission behavior

    const backendUrl = 'http://3.144.107.209';

   // const accessToken = localStorage.getItem("access_token");
    // Prepare data to send to the backend
    const formData = {
      monthlyEarnings: monthlyEarnings,
      essentialExpenses: essentialExpenses,
      nonEssentialExpenses: nonEssentialExpenses,
      savingsGoal: savingsGoal
    };
    
    try {

        // Send each data category to its respective endpoint
        await apiRequest(`${backendUrl}/budget/income/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ monthlyEarnings }),
        });
    
        await apiRequest(`${backendUrl}/budget/essential-expenses/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ essentialExpenses }),
        });
    
        await apiRequest(`${backendUrl}/budget/non-essential-expense/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ nonEssentialExpenses }),
        });
    
        await apiRequest(`${backendUrl}/budget/savings-goal/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ savingsGoal }),
        });
    
        // Redirect to the dashboard if all submissions succeed
        navigate('/dashboard');
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
};
    return (
    <div className="align-items-center min-vh-100">
    <div className="welcome Header text-center mb-4">
    <h2>Welcome to Budgeting 101!</h2>
    </div>

      {/*Monthly Earnings*/}
        <div className="Monthly Earnings text-center mb-4">
        <h3>Please Enter your Monthly Earnings:</h3>
        <div className="input-group mb-3 w-50 mx-auto">
        <span className="input-group-text">$</span>
          <input
            type="number"
            placeholder="Amount"
            aria-label="Monthly Earnings"
            className="form-control"
            value={monthlyEarnings}
            onChange={(e) => setMonthlyEarnings(e.target.value)}
            />
        </div>
        </div>

      {/* Essential Spending Section */}
        <div className="Essential Spending text-center mb-4">
        <h3>Essential Expenses:</h3>
        
        {essentialExpenses.map((expense, index) => (
        <div key={index} className="input-group mb-3 w-50 mx-auto">
          <input
            type="text"
            placeholder="Expense Name"
            aria-label="Expense Name"
            className="form-control"
            value={expense.name}
            onChange={(e)=> {
                const updatedExpenses = [...essentialExpenses];
                updatedExpenses[index].name = e.target.value;
                setEssentialExpenses(updatedExpenses);
            }}
          />

          <span className="input-group-text">$</span>
          <input
            type="number"
            placeholder="Amount"
            aria-label="Amount"
            className="form-control"
            value={expense.amount}
            onChange={(e) => {
              const updatedExpenses = [...essentialExpenses];
              updatedExpenses[index].amount = e.target.value;
              setEssentialExpenses(updatedExpenses);
            }}
          />
          </div>
        ))}
        
        <button
          className="btn btn-primary mt-3"
          onClick={addEssentialExpenseRow}
        >
            Add Essential Expense
        </button>

        </div>
      
      {/* Non-Essential Spending Section */}
        <div className="Non-Essential Spending text-center mb-4">
        <h3>Non-Essential Expenses:</h3>
        {nonEssentialExpenses.map((expense, index) => (
          <div key={index} className="input-group mb-3 w-50 mx-auto">
            <input
              type="text"
              placeholder="Expense Name"
              aria-label="Expense Name"
              className="form-control"
              value={expense.name}
              onChange={(e) => {
                const updatedExpenses = [...nonEssentialExpenses];
                updatedExpenses[index].name = e.target.value;
                setNonEssentialExpenses(updatedExpenses);
              }}
            />
            <span className="input-group-text">$</span>
            <input
              type="number"
              placeholder="Amount"
              aria-label="Amount"
              className="form-control"
              value={expense.amount}
              onChange={(e) => {
                const updatedExpenses = [...nonEssentialExpenses];
                updatedExpenses[index].amount = e.target.value;
                setNonEssentialExpenses(updatedExpenses);
              }}
            />
          </div>
        ))}
        <button
          className="btn btn-secondary mt-3"
          onClick={addNonEssentialExpenseRow}
        >
          Add Non-Essential Expense
        </button>
        </div>


    {/*Savings Goal Section*/}
    <div className="Savings Goal text-center mb-4">
            <h3>Please Enter your Savings Goal:</h3>
            <div className="input-group mb-3 w-50 mx-auto">
            <span className="input-group-text">$</span>
          <input
            type="number"
            placeholder="Amount"
            aria-label="Savings Goal"
            className="form-control"
            value={savingsGoal}
            onChange={(e) => setSavingsGoal(e.target.value)}
            />
        </div>
        </div>

      {/* Submit Button */}
      <div className="text-center mt-4">
        <button className="btn btn-success" onClick={submitForm}>
          Submit
        </button>
      </div>
    
    </div>

);
}
export default Home;
