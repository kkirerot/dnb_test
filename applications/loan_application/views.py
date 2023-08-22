from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import permissions
from . import models
from . import serializers

class LoanApplicationCreateView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = models.LoanApplication.objects.all()
    serializer_class = serializers.LoanApplicationCreateSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["user"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoanApplicationListView(APIView):
    permission_classes = [permissions.IsStaffUser]
    queryset = models.LoanApplication.objects.all()
    serializer_class = serializers.LoanApplicationAdminListSerializer
    
    def get(self, request):
        loan_applications = models.LoanApplication.objects.all()
        serializer = self.serializer_class(loan_applications, many=True)
        return Response(serializer.data)