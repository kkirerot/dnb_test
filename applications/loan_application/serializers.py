from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class LoanApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanApplication
        fields = [
            "customer_ssn",
            "full_name",
            "loan_amount",
            "equity_amount",
            "salary_amount",
        ]
        
class LoanApplicationAdminListSerializer(serializers.ModelSerializer): 
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields =  [
                "email",
            ]
    
    user = UserSerializer()
    class Meta:
        model = models.LoanApplication
        fields = [
            "customer_ssn",
            "full_name",
            "loan_amount",
            "equity_amount",
            "salary_amount",
            "user",
        ]
