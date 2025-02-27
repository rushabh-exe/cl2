from django.shortcuts import get_object_or_404, render
from .decorators import superuser_required
from django.http import HttpResponse
from .models import TrainCheckpoint, TrainJourney, TrainJourneyCheckpoint, TruckJourney,Location,Buyers,TruckDriver,JourneyCheckpoint,Checkpoint,ShipJourney,ShipJourneyCheckpoint

def restricted_view(request):
    return render(request, 'adminpanel/home.html')

def trucks(request):
    return render(request,'adminpanel/trucks.html')

def truck_list(request):
    context = {'TruckJourney' : TruckJourney.objects.all()}
    return render(request, 'adminpanel/truck_list.html',context)

from django.shortcuts import render, get_object_or_404, redirect

def inditruck(request, pk):
    truck = get_object_or_404(TruckJourney, pk=pk)
    checkpoints = JourneyCheckpoint.objects.filter(journey=truck)
    context = {'truck': truck, 'checkpoints': checkpoints}
    return render(request, 'adminpanel/inditruck.html', context)

def trains(request):
    context = {'TrainJourney' : TrainJourney.objects.all()}
    return render(request,'adminpanel/trains.html',context)

def inditrain(request, pk):
    train = get_object_or_404(TrainJourney, pk=pk)
    checkpoint= TrainJourneyCheckpoint.objects.filter(journey=train)
    context = {'train': train, 'checkpoints': checkpoint}
    return render(request, 'adminpanel/inditrain.html', context)


def ships(request):
    context = {'ShipJourney' : ShipJourney.objects.all()}
    return render(request,'adminpanel/ships.html',context)

def indiship(request, pk):
    ship = get_object_or_404(ShipJourney, pk=pk)
    checkpointer = ShipJourneyCheckpoint.objects.filter(journey=ship)
    context = {'ship': ship, 'checkpoints': checkpointer}
    return render(request, 'adminpanel/indiship.html', context)


def drivers(request):
    drivers = TruckDriver.objects.all()
    context = {'drivers':drivers}
    return render(request, 'adminpanel/drivers.html',context)