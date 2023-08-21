from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from applications.loan_application.models import LoanApplication

class LoanApplicationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')        
        self.staff_user = User.objects.create_user(username='staff', password='password', is_staff=True)
        self.client = APIClient()
    
    def test_create_loan_application(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('loan_application_create')  
        data = {
            'customer_ssn': '13109611111',
            'full_name': 'tor-erik kristensen',
            'loan_amount': 100000,
            'equity_amount': 200000,
            'salary_amount': 400000,
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LoanApplication.objects.count(), 1)
        self.assertEqual(LoanApplication.objects.get().customer_ssn, '13109611111')
        
        
    def test_retrieve_loan_applications_by_staff(self):
        self.client.force_authenticate(user=self.staff_user)  
        
        url = reverse('loan_application_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_retrieve_loan_applications_by_non_staff(self):
        self.client.force_authenticate(user=self.user)  
        url = reverse('loan_application_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_create_loan_application_without_authentication(self):
        url = reverse('loan_application_create')
        data = {
            'customer_ssn': '13109611111',
            'full_name': 'tor-erik kristensen',
            'loan_amount': 100000,
            'equity_amount': 200000,
            'salary_amount': 400000,
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_loan_applications_without_authentication(self):
        url = reverse('loan_application_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)