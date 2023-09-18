from django.shortcuts import get_object_or_404, render
from .decorators import superuser_required
from django.http import HttpResponse
from .models import TrainCheckpoint, TrainJourney, TrainJourneyCheckpoint, TruckJourney,Location,Buyers,TruckDriver,JourneyCheckpoint,Checkpoint,ShipJourney,ShipJourneyCheckpoint

def restricted_view(request):
    return render(request, 'adminpanel/dashboard.html')

def trucks(request):
    return render(request,'adminpanel/trucks.html')

def truck_list(request):
    context = {'TruckJourney' : TruckJourney.objects.all()}
    return render(request, 'adminpanel/truck_list.html',context)

from django.shortcuts import render, get_object_or_404, redirect

def inditruck(request, pk):
    recognized_plate = "MH20EJ036"
    recognized_location = "Mumbai"

    # Assuming mlmodel returns a recognized license plate as recognized_plate

    drivers = TruckDriver.objects.all()
    matching_driver = None

    for driver in drivers:
        if driver.truck_no == recognized_plate:
            matching_driver = driver
            break

    if matching_driver:
        # Update the truck journey record, considering location matching
        truck_journey = TruckJourney.objects.get(driver=matching_driver)
        
        # Iterate through checkpoints of the journey
        for journey_checkpoint in JourneyCheckpoint.objects.filter(journey=truck_journey):
            if journey_checkpoint.checkpoint.location.name == recognized_location:
                journey_checkpoint.checkpoint_reached = True
                journey_checkpoint.save()
                print("Found Truck")

    truck = get_object_or_404(TruckJourney, pk=pk)
    checkpoints = JourneyCheckpoint.objects.filter(journey=truck)
    context = {'truck': truck, 'checkpoints': checkpoints}
    return render(request, 'adminpanel/inditruck.html', context)

def trains(request):
    context = {'TrainJourney' : TrainJourney.objects.all()}
    return render(request,'adminpanel/trains.html',context)

def inditrain(request, pk):
    train = get_object_or_404(TrainJourney, pk=pk)
    checkpoints = TrainJourneyCheckpoint.objects.filter(journey=train)
    context = {'train': train, 'checkpoints': checkpoints}
    return render(request, 'adminpanel/inditrain.html', context)


def ships(request):
    context = {'ShipJourney' : ShipJourney.objects.all()}
    return render(request,'adminpanel/ships.html',context)

def indiship(request, pk):
    ship = get_object_or_404(ShipJourney, pk=pk)
    checkpoints = ShipJourneyCheckpoint.objects.filter(journey=ship)
    context = {'ship': ship, 'checkpoints': checkpoints}
    return render(request, 'adminpanel/indiship.html', context)