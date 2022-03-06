from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name="index"),
    path('employees/', views.EmployeeList.as_view(), name="employees"),
    path('api/employee/add/', views.AddEmployee.as_view(), name="add_employee"),
    path('api/employee/delete/', views.DeleteEmployee.as_view(), name="delete_employee"),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
