from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LoanApplication(models.Model):
    customer_ssn = models.CharField(max_length=11)
    full_name = models.CharField(max_length=255)
    loan_amount = models.IntegerField()
    equity_amount = models.IntegerField()
    salary_amount = models.IntegerField()

    user = models.ForeignKey(User, related_name="loan_applications", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        app_label = 'loan_application'