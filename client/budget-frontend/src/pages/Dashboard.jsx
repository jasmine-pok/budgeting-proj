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
  
 // Editing state
  const [editingEssentialIndex, setEditingEssentialIndex] = useState(null);
  const [editingNonEssentialIndex, setEditingNonEssentialIndex] = useState(null);
 
  // Editable copies (UI state)
  const [editedEssentialExpenses, setEditedEssentialExpenses] = useState([]);
  const [editedNonEssentialExpenses, setEditedNonEssentialExpenses] = useState([]);
 
  // Calculated values
  const [totalEssentialExpenses, setTotalEssentialExpenses] = useState(0);
  const [totalNonEssentialExpenses, setTotalNonEssentialExpenses] = useState(0);
  const [timeToSavingsGoal, setTimeToSavingsGoal] = useState('');

  // =====================================
  // Initialize editable state from context
  // =====================================
  useEffect(() => {
     setEditedEssentialExpenses(
      essentialExpenses.map(e => ({
        ...e,
        amount: Number(e.amount) || 0,
      }))
    );

    setEditedNonEssentialExpenses(
      nonEssentialExpenses.map(e => ({
        ...e,
        amount: Number(e.amount) || 0,
      }))
    );
  }, [essentialExpenses, nonEssentialExpenses]);

// =====================================
  // Recalculate totals + time to goal
  // =====================================
  useEffect(() => {
    const essentialTotal = editedEssentialExpenses.reduce(
      (sum, e) => sum + e.amount,
      0
    );

    const nonEssentialTotal = editedNonEssentialExpenses.reduce(
      (sum, e) => sum + e.amount,
      0
    );

    setTotalEssentialExpenses(essentialTotal);
    setTotalNonEssentialExpenses(nonEssentialTotal);

    const monthlySavings =
      monthlyEarnings - essentialTotal - nonEssentialTotal;

    if (monthlySavings <= 0) {
      setTimeToSavingsGoal('Not achievable with current expenses');
    } else {
      const months = Math.ceil(savingsGoal / monthlySavings);
      setTimeToSavingsGoal(`${months} month${months > 1 ? 's' : ''}`);
    }
  }, [
    editedEssentialExpenses,
    editedNonEssentialExpenses,
    monthlyEarnings,
    savingsGoal,
  ]);

  // =====================================
  // Handlers
  // =====================================
  const handleEssentialExpenseChange = (index, newAmount) => {
    setEditedEssentialExpenses(prev =>
      prev.map((expense, i) =>
        i === index
          ? { ...expense, amount: Number(newAmount) || 0 }
          : expense
      )
    );
  };

  const handleNonEssentialExpenseChange = (index, newAmount) => {
    setEditedNonEssentialExpenses(prev =>
      prev.map((expense, i) =>
        i === index
          ? { ...expense, amount: Number(newAmount) || 0 }
          : expense
      )
    );
  };
  /*
// ===============================
// BACKEND INTEGRATION (WIP)
// Intended behavior:
// - Fetch calculated totals from Django backend
// - Receive time-to-savings-goal estimate
// API integration was not finalized, so frontend
// calculations are used for demo purposes.
// ===============================

useEffect(() => {
    const fetchDashboardData = async () => {
      const backendUrl = '';
     
      try {
        // Fetch total essential expenses
        const essentialResponse = await apiRequest(`${backendUrl}/essential-expenses-total`, {
          method: 'GET',
          credentials: 'include',
        });

        if (essentialResponse?.total !== undefined) {
          setTotalEssentialExpenses(essentialResponse.total);
          setEditedEssentialExpenses([...essentialExpenses]); // Initialize editable list
        } else {
          console.error("Error: Essential expenses data is invalid:", essentialResponse);
        }

        // Fetch total non-essential expenses
        const nonEssentialResponse = await apiRequest(`${backendUrl}/non-essential-expenses-total`, {
          method: 'GET',
          credentials: 'include',
        });

        if (nonEssentialResponse?.total !== undefined) {
          setTotalNonEssentialExpenses(nonEssentialResponse.total);
          setEditedNonEssentialExpenses([...nonEssentialExpenses]); // Initialize editable list
        } else {
          console.error("Error: Non-essential expenses data is invalid:", nonEssentialResponse);
        }

        // Fetch time to reach savings goal
        const savingsResponse = await apiRequest(`${backendUrl}/budget/time-to-reach-goal/`, {
          method: 'GET',
          credentials: 'include',
        });
        console.log('Savings Response Raw:', savingsResponse);
        const savingsText = await savingsResponse.text();
        console.log('Savings Response Text:', savingsText);

        if (savingsResponse?.time !== undefined) {
          setTimeToSavingsGoal(savingsResponse.time);
        } else {
          console.error("Error: Time-to-savings-goal data is invalid:", savingsResponse);
        }
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      }
    };

    fetchDashboardData();
  }, []);

*/
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
        {(editedEssentialExpenses).map((expense, index) => (
            <li key={index} className="expense-item">
                {editingEssentialIndex === index ? (
                    <>
                        <input
                            type="number"
                            value={expense.amount}
                            onChange={(e) => handleEssentialExpenseChange(index, e.target.value)}
                        />
                        <button onClick={() => setEditingEssentialIndex(null)}>Save</button>
                    </>
                ) : (
                    <>
                        <span>{expense.name}: ${expense.amount}</span>
                        <button onClick={() => setEditingEssentialIndex(index)}>Edit</button>
                    </>
                )}
            </li>
        ))}
        </ul>
        </div>
  
        {/*Quadrant 4:  Display Non-Essential Expenses */}
        <div className="flex-item">
        <h4>Non-Essential Expenses:</h4>
        <ul>
        {(editedNonEssentialExpenses).map((expense, index) => (
            <li key={index} className="expense-item">
                {editingNonEssentialIndex === index ? (
                    <>
                        <input
                            type="number"
                            value={expense.amount}
                            onChange={(e) => handleNonEssentialExpenseChange(index, e.target.value)}
                        />
                        <button onClick={() => setEditingNonEssentialIndex(null)}>Save</button>
                    </>
                ) : (
                    <>
                        <span>{expense.name}: ${expense.amount}</span>
                        <button onClick={() => setEditingNonEssentialIndex(index)}>Edit</button>
                    </>
                )}
            </li>
        ))}
            </ul>
        </div>

        {/* Quadrant 5: Display Total Essential Expenses */}
        <div className="flex-item">
          <h4>Total Essential Expenses:</h4>
          <p>${totalEssentialExpenses}</p>
        </div>

        {/* Quadrant 6: Display Total Non-Essential Expenses */}
        <div className="flex-item">
          <h4>Total Non-Essential Expenses:</h4>
          <p>${totalNonEssentialExpenses}</p>
        </div>

        {/* Quadrant 7:  Time to reach goal*/}
        <div className="flex-item full-width">
          <h4>Time to reach Savings Goal:</h4>
          <p>{timeToSavingsGoal}</p>
        </div>

      </div>
      </div>
    );
  };
  
  export default Dashboard;
  
