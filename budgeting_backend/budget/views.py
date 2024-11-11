from django.shortcuts import render
from rest_framework import generics
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal
from .serializers import IncomeSerializer, EssentialExpensesSerializer, NonEssentialExpensesSerializer, SavingsGoalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

# Pagination class to laod 10 records per page 
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# ListCreateAPIView: lists all incomes for the user and creates new income record
# GET request to /income/ = list income records
# POST request to /income/ = create new income record
class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all() # Get all income records from the database
    serializer_class = IncomeSerializer  # IncomeSerializer will transform Income objects to JSON and vice-versa
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    pagination_class = StandardResultsSetPagination

    # Override get_queryset to filter incomes by the logged-in user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) # Only return incomes that belong to the current user.
    
    # Automatically associate the logged-in user with the income record during creation
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)   # Save the income with the logged-in user
        except Exception as e:
            raise serializers.ValidationError(f"Error: {str(e)}")
        

# GET request to /income/<id>/ will retrieve a single income by its ID
# PUT/PATCH request to /income/<id>/ will update the specific income
# DELETE request to /income/<id>/ will delete the income
class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
# Essential Expenses follows the same logic

class EssentialExpensesListCreateView(generics.ListCreateAPIView):
    queryset = EssentialExpenses.objects.all()
    serializer_class = EssentialExpensesSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)   # Save the income with the logged-in user
        except Exception as e:
            raise serializers.ValidationError(f"Error: {str(e)}")
    
class EssentialExpensesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EssentialExpenses.objects.all()
    serializer_class = EssentialExpensesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

# Non Essential Expenses
class NonEssentialExpensesListCreateView(generics.ListCreateAPIView):
    queryset = NonEssentialExpenses.objects.all()
    serializer_class = NonEssentialExpensesSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)   # Save the income with the logged-in user
        except Exception as e:
            raise serializers.ValidationError(f"Error: {str(e)}")
    
class NonEssentialExpensesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NonEssentialExpenses.objects.all()
    serializer_class = NonEssentialExpensesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
# Savings Goals
class SavingsGoalListCreateView(generics.ListCreateAPIView):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)   # Save the income with the logged-in user
        except Exception as e:
            raise serializers.ValidationError(f"Error: {str(e)}")
    
class SavingsGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
