from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeadList.as_view(), name="lead"),
    path('api/add-lead/', views.AddLead.as_view(), name="add-lead"),
]
