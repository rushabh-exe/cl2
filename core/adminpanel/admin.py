from django.contrib import admin
from .models import Buyers, ShipCheckpoint, TruckDriver, TruckJourney, Location, JourneyCheckpoint, Checkpoint, TrainJourneyCheckpoint, TrainJourney, TrainCheckpoint, TrainStation, ShipJourney, ShipJourneyCheckpoint, ShipYard

class CheckpointAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # Create a JourneyCheckpoint for each TruckJourney
        truck_journeys = TruckJourney.objects.all()
        for journey in truck_journeys:
            JourneyCheckpoint.objects.get_or_create(journey=journey, checkpoint=obj)

class JourneyCheckpointInline(admin.TabularInline):
    model = JourneyCheckpoint

class TruckJourneyAdmin(admin.ModelAdmin):
    inlines = [JourneyCheckpointInline]

class TrainJourneyCheckpointInLine(admin.TabularInline):
    model = TrainJourneyCheckpoint

class TrainJourneyAdmin(admin.ModelAdmin):
    inlines = [TrainJourneyCheckpointInLine]

class ShipJourneyCheckpointInLine(admin.TabularInline):
    model = ShipJourneyCheckpoint

class ShipJourneyAdmin(admin.ModelAdmin):
    inlines = [ShipJourneyCheckpointInLine]

# Register your models here.
admin.site.register(TruckDriver)
admin.site.register(Buyers)
admin.site.register(Location)
admin.site.register(JourneyCheckpoint)
admin.site.register(TruckJourney, TruckJourneyAdmin)
admin.site.register(Checkpoint, CheckpointAdmin)
admin.site.register(TrainCheckpoint)
admin.site.register(TrainJourney, TrainJourneyAdmin)
admin.site.register(TrainStation)
admin.site.register(TrainJourneyCheckpoint)
admin.site.register(ShipYard)
admin.site.register(ShipCheckpoint)
admin.site.register(ShipJourney, ShipJourneyAdmin)
admin.site.register(ShipJourneyCheckpoint)
