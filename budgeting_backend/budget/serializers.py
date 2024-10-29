from rest_framework import serializers
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'user', 'amount', 'name']

class EssentialExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssentialExpenses
        fields = ['id', 'user', 'amount', 'name']

class NonEssentialExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonEssentialExpenses
        fields = ['id', 'user', 'amount', 'name']

class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = ['id', 'user', 'amount']