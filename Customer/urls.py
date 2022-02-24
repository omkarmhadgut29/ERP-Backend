from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name="customer"),
    path('api/add-customer/', views.AddCustomer.as_view(), name="add-customer"),
]
