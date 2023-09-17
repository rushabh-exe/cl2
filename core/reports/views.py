from django.shortcuts import get_object_or_404, render
from adminpanel.models import ShipJourney,TrainJourney,TruckJourney
from .models import *

def viewReport(request):

    # truck = TruckJourney.objects.all()
    # truck_coal_sum = 0
    # for coal in truck:
    #     capacity = coal.capacity
    #     truck_coal_sum += capacity

    # train = TrainJourney.objects.all()
    # train_coal_sum = 0
    # for coal in train:
    #     capacity = coal.capacity
    #     train_coal_sum += capacity


    # target = 5000
    # amt = truck_coal_sum + train_coal_sum
    # if target>amt:
    #     # percentage = ((target - (truck_coal_sum+train_coal_sum))/target) * 100
    #     # print("- " + percentage)
    #     percentage = ((target-amt)/target)*100
    #     print("-" + str(percentage) + "%")
    # else:
    #     print("all good")

    return render(request, 'reports/report.html')
    
    

def reports(request):
    ship = ShipJourney.objects.all()
    trains = TrainJourney.objects.all()
    trucks = TruckJourney.objects.all()

    truck_sum = 0
    for coal in trucks:
        capacity = coal.capacity
        truck_sum += capacity

    train_sum = 0
    for coal in trains:
        capacity = coal.capacity
        train_sum += capacity

    ship_sum = 0
    for coal in ship:
        capacity = coal.capacity
        ship_sum += capacity

    total = (train_sum + truck_sum + ship_sum)/100 

    context = {
        'ship': ship,
        'truck': trucks,
        'train': trains,
        'truck_sum': truck_sum,
        'train_sum': train_sum,
        'ship_sum': ship_sum,
        'sum': total,
        'productions': prodcutions.objects.all(),
    }
    
    return render(request, 'reports/seereport.html', context)
