from rest_framework import serializers
from . import models

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanApplication
        fields = [
            "customer_ssn",
            "full_name",
            "loan_amount",
            "equity_amount",
            "salary_amount",
        ]