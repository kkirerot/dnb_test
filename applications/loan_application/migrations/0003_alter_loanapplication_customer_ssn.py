# Generated by Django 4.2.4 on 2023-08-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_application', '0002_loanapplication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='customer_ssn',
            field=models.CharField(max_length=11),
        ),
    ]