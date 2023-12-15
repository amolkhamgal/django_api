from django.shortcuts import render
from .models import Department, Employee
from .serializers import DeptSerializer, EmpSerializer
from rest_framework import viewsets
# Create your views here.

class DeptViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DeptSerializer

class EmpViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer    
