import { createContext, useState } from 'react';
import PropTypes from 'prop-types'; // Import PropTypes

// Create a Context
const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [monthlyEarnings, setMonthlyEarnings] = useState('');
  const [essentialExpenses, setEssentialExpenses] = useState([{ name: '', amount: '' }]);
  const [nonEssentialExpenses, setNonEssentialExpenses] = useState([{ name: '', amount: '' }]);
  const [savingsGoal, setSavingsGoal] = useState('');

  return (
    <AppContext.Provider
      value={{
        monthlyEarnings,
        setMonthlyEarnings,
        essentialExpenses,
        setEssentialExpenses,
        nonEssentialExpenses,
        setNonEssentialExpenses,
        savingsGoal,
        setSavingsGoal,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
// PropTypes validation for AppProvider
AppProvider.propTypes = {
  children: PropTypes.node.isRequired, // Validate that children is a React node
};

export {AppContext};
