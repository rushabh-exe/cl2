from django.urls import path
from . import views

urlpatterns = [
    path('', views.rakes, name='rakes'),
    path('sendMail/',views.sendMail,name='sendMail')
]