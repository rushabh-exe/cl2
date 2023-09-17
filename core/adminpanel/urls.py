# appname/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.restricted_view, name='restricted_view'),
    path('trucks/',views.trucks, name='trucks'),
    path('trucks/list',views.truck_list,name="truck_list"),
    path('trucks/<str:pk>/',views.inditruck,name='inditruck'),
    path('trains/',views.trains,name="trains"),
    path('trains/<str:pk>/',views.inditrain,name='inditrains'),
    path('ships/',views.ships,name="ships"),
    path('ships/<str:pk>/',views.indiship,name='indiship'),
]
