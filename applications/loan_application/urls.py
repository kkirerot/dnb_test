from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.LoanApplicationCreateView.as_view(), name='loan_application_create'),
    path('list/', views.LoanApplicationListView.as_view(), name='loan_application_list'),
]