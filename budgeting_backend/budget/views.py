from django.shortcuts import render
from rest_framework import generics
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal
from .serializers import IncomeSerializer, EssentialExpensesSerializer, NonEssentialExpensesSerializer, SavingsGoalSerializer
from rest_framework.permissions import IsAuthenticated

# ListCreateAPIView: lists all incomes for the user and creates new income record
# GET request to /income/ = list income records
# POST request to /income/ = create new income record
class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all() # Get all income records from the database
    serializer_class = IncomeSerializer  # IncomeSerializer will transform Income objects to JSON and vice-versa
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    # Override get_queryset to filter incomes by the logged-in user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) # Only return incomes that belong to the current user.
    
    # Automatically associate the logged-in user with the income record during creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)   # Save the income with the logged-in user