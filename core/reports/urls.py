from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewReport, name='reports'),
    path('seereport/', views.reports, name='seereport'),
]
