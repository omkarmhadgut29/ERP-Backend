from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

def index(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(request, 'Employee/index.html', context)

class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
