from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_ssn", "full_name", "loan_amount", "equity_amount", "salary_amount")