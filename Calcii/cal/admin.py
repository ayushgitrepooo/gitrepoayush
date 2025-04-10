from django.contrib import admin
from .models import Calculator

# Register your models here.

@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('num1', 'operations', 'num2', 'result', 'created_at')
    list_filter = ('operations', 'created_at')
    search_fields = ('num1', 'num2', 'result')
    ordering = ('-created_at',)
    
