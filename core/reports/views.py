from django.shortcuts import get_object_or_404, render
from adminpanel.models import *
from .models import *
# Create your views here.

def viewReport(request):

    truck = TruckJourney.objects.all()
    truck_coal_sum = 0
    for coal in truck:
        capacity = coal.capacity
        truck_coal_sum += capacity

    train = TrainJourney.objects.all()
    train_coal_sum = 0
    for coal in train:
        capacity = coal.capacity
        train_coal_sum += capacity


    target = 5000
    amt = truck_coal_sum + train_coal_sum
    if target>amt:
        # percentage = ((target - (truck_coal_sum+train_coal_sum))/target) * 100
        # print("- " + percentage)
        percentage = ((target-amt)/target)*100
        print("-" + str(percentage) + "%")
    else:
        print("all good")












    return render(request, 'reports/report.html')
    
    