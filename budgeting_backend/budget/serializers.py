from rest_framework import serializers
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income  # Tie this serializer to the Income model
        fields = ['id', 'user', 'amount', 'name']
        read_only_fields = ['user']
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Income amount must be positive.")
        return value

class EssentialExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssentialExpenses   # Tie this serializer to the Essential Expenses Model
        fields = ['id', 'user', 'amount', 'name']
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Expenses amount must be positive.")
        return value

class NonEssentialExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonEssentialExpenses    # Tie this serializer to the Non Essential Expenses model
        fields = ['id', 'user', 'amount', 'name']
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Expenses amount must be positive.")
        return value

class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal # Tie this serializer to the SavingsGoal model
        fields = ['id', 'user', 'amount']
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Savings Goal amount must be positive.")
        return value