from django.contrib import admin
from .models import Income, EssentialExpenses, NonEssentialExpenses, SavingsGoal, Profile

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount')  # Columns displayed in the admin list view
    search_fields = ('user__username', 'name')  # Add search functionality
    list_filter = ('user',)  # Add filtering options

@admin.register(EssentialExpenses)
class EssentialExpensesAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount')
    search_fields = ('user__username', 'name')
    list_filter = ('user',)

@admin.register(NonEssentialExpenses)
class NonEssentialExpensesAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount')
    search_fields = ('user__username', 'name')
    list_filter = ('user',)

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount')
    search_fields = ('user__username', 'name')
    list_filter = ('user',)


