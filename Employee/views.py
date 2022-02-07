from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
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

class AddEmployees(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        fields = Employee._meta.get_fields()
        validData = True
        for field in fields:
            if field.name != "id" and field.name != "image":
                if request.data[field.name] == '':
                    validData = False
                    break
        if validData:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student added', 'data': serializer.data})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        return Response({'status': 400, 'message': 'Student not created'})

