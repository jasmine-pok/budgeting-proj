from django.urls import path
from .views import (
    IncomeListCreateView, IncomeDetailView,
    EssentialExpensesListCreateView, EssentialExpensesDetailView,
    NonEssentialExpensesListCreateView, NonEssentialExpensesDetailView,
    SavingsGoalListCreateView, SavingsGoalDetailView,
    TimeToReachGoalView
)

app_name = 'budget'

urlpatterns = [
    # Income URLS
    path('income/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),

    # Essential Expenses URLS
    path('essential-expenses/', EssentialExpensesListCreateView.as_view(), name='essential-expenses-list-create'),
    path('essential-expenses/<int:pk>/', EssentialExpensesDetailView.as_view(), name='essential-expenses-detail'),

    # Non Essential Expenses URLS
    path('non-essential-expenses/', NonEssentialExpensesListCreateView.as_view(), name='non-essential-expenses-list-create'),
    path('non-essential-expenses/<int:pk>/', NonEssentialExpensesDetailView.as_view(), name='non-essential-expenses-detail'),

    # Savings Goal
    path('savings-goal/', SavingsGoalListCreateView.as_view(), name='savings-goal-list-create'),
    path('savings-goal/<int:pk>/', SavingsGoalDetailView.as_view(), name='savings-goal-detail'),

    # Time to reach goal
    path('time-to-reach-goal/', TimeToReachGoalView.as_view(), name='time-to-reach-goal')
]