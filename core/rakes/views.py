import math
from django.shortcuts import render
from django.http import HttpResponse
from adminpanel.models import *


# Create your views here.


def rakes(request):
    trucks = TruckJourney.objects.all()
    trains = TrainJourney.objects.all()
    ships = ShipJourney.objects.all()
    trainCounts = TrainJourney.objects.filter(complete=False)

    truck_sum = 0
    for coal in trucks:
        capacity = coal.capacity
        truck_sum += capacity
    print(truck_sum)

    train_sum = 0
    for coal in trains:
        capacity = coal.capacity
        train_sum += capacity
    print(train_sum)

    ship_sum = 0
    for coal in ships:
        capacity = coal.capacity
        ship_sum += capacity
    print(ship_sum)

    totalProduction = truck_sum + train_sum + ship_sum

    trainCount = 0
    for count in trainCounts:
        trainCount += 1
    print(trainCount)

    trainCoalCount = totalProduction - ship_sum - truck_sum
    rakesCapacity = 1000
    numberofRakes = math.ceil(trainCoalCount / rakesCapacity)
    print(numberofRakes)

    context = {
        'totalProduction':totalProduction,
        'trainCount':trainCount,
        'trainCoalCount':trainCoalCount,
        'numberofRakes':numberofRakes
    }
    return render(request,"rakes/page.html",context)


def sendMail(request):
    return render(request, "rakes/sendMail.html")