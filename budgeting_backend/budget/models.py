from django.db import models
from django.contrib.auth.models import User

# Income class
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Link to a user with foreign key relationship
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)     # different categories such as Full-time job, side hustle etc

    def __str__(self):
        return f"{self.name} - {self.amount}"

class EssentialExpenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
class NonEssentialExpenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property 
    def total_income(self):
        return sum(income.amount for income in self.user.income_set.all())
    
    @property
    def total_essential_expenses(self):
        return sum(expense.amount for expense in self.user.essentialexpenses_set.all())
    
    @property
    def total_non_essential_expense(self):
        return sum(expense.amount for expense in self.user.nonessentialexpenses_set.all())
    
    @property
    def remaining_expense(self):
        return self.total_income - self.total_essential_expenses
    
    @property
    def time_to_reach_goal(self):
        savings_goal = self.user.savingsgoal_set.first()
        if savings_goal:
            monthly_savings = self.remaining_expense - self.total_non_essential_expense
            if monthly_savings > 0:
                months = savings_goal.goal_amount / monthly_savings
                if months >= 12:
                    years = months/12
                    return years
                else:
                    return months
            return None 

    

    

