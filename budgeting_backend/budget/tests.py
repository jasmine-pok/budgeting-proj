from django.test import TestCase
from django.contrib.auth.models import User
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal

# models.py Unit Test

class BudgetingAppTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_income_creation(self):
        # Create income instance 
        income = Income.objects.create(user=self.user, name='Full-time job', amount=5000)
        self.assertEqual(income.name, 'Full-time job')
        self.assertEqual(income.amount, 5000)
        self.assertEqual(income.user, self.user)

    def test_essential_expense_creation(self):
        # Create essential expense instance
        expense = EssentialExpenses.objects.create(user=self.user, name='Rent', amount=1500)
        self.assertEqual(expense.name, 'Rent')
        self.assertEqual(expense.amount, 1500)

    def test_non_essential_expense_creation(self):
        # Create non essential expense instance
        expense = NonEssentialExpenses.objects.create(user=self.user, name='Dining Out', amount=200)
        self.assertEqual(expense.name, 'Dining Out')
        self.assertEqual(expense.amount, 200)

    def test_savings_goal_creation(self):
        # Create essential expense instance
        goal = SavingsGoal.objects.create(user=self.user, amount=10000)
        self.assertEqual(goal.amount, 10000)

    def test_calculating_total_income(self):
        # Create multiple Income instances
        Income.objects.create(user=self.user, name='Full-time job', amount=5000)
        Income.objects.create(user=self.user, name='Side hustle', amount=1500)
        total_income = sum(income.amount for income in self.user.income_set.all())
        self.assertEqual(total_income, 6500)
        
    def test_calculating_total_expenses(self):
        # Create essential and non-essential expenses
        EssentialExpenses.objects.create(user=self.user, name='Rent', amount=1500)
        NonEssentialExpenses.objects.create(user=self.user, name='Dining Out', amount=200)
        total_expenses = sum(expense.amount for expense in self.user.essentialexpenses_set.all()) + \
                         sum(expense.amount for expense in self.user.nonessentialexpenses_set.all())
        self.assertEqual(total_expenses, 1700)