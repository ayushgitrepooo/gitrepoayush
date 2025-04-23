from django.contrib import admin
from .models import Calculator

# Register your models here.

@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('a','operation', 'b', 'result', 'created_at')
    list_filter = ('operation', 'created_at')
    search_fields = ('a', 'b', 'result')
    ordering = ('-created_at',)
    