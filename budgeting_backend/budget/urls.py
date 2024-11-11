from django.urls import path
from .views import (
    IncomeListCreateView, IncomeDetailView,
    EssentialExpensesListCreateView, EssentialExpensesDetailView,
    NonEssentialExpensesListCreateView, NonEssentialExpensesDetailView,
    SavingsGoalListCreateView, SavingsGoalDetailView
)

app_name = 'budget'

URL_PATTERNS = [
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
    path('savings-goal/<int:pk>/', SavingsGoalDetailView.as_view(), name='savings-goal-detail')

]