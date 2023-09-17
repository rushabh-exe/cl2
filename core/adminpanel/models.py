from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TrainStation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ShipYard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TruckDriver(models.Model):
    name = models.CharField(max_length=200)
    truck_no = models.CharField(max_length=200, unique=True)
    joined_date = models.DateField(auto_now_add=True)
    aadhar_no = models.CharField(max_length=12, unique=True)
    license_no = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Buyers(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class TrainJourney(models.Model):
    train_no = models.CharField(max_length=200)
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    COAL_TYPE_CHOICES = [
        ("Lignite", "Lignite"),
        ("Sub-Bituminous", "Sub-Bituminous"),
        ("Bituminous", "Bituminous"),
        ("Anthracite", "Anthracite"),
    ]
    coal_type = models.CharField(max_length=15, choices=COAL_TYPE_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.train_no

    def add_checkpoint(self, checkpoint):
        TrainJourneyCheckpoint.objects.get_or_create(journey=self, checkpoint=checkpoint)

    def remove_checkpoint(self, checkpoint):
        TrainJourneyCheckpoint.objects.filter(journey=self, checkpoint=checkpoint).delete()

class TrainCheckpoint(models.Model):
    location = models.ForeignKey(TrainStation, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Location: {self.location}, Checkpoint Reached: {self.checkpoint_reached}"

class ShipCheckpoint(models.Model):
    location = models.ForeignKey(ShipYard, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Location: {self.location}, Checkpoint Reached: {self.checkpoint_reached}"

class Checkpoint(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Location: {self.location}, Checkpoint Reached: {self.checkpoint_reached}"

class TruckJourney(models.Model):
    driver = models.ForeignKey(TruckDriver, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    COAL_TYPE_CHOICES = [
        ("Lignite", "Lignite"),
        ("Sub-Bituminous", "Sub-Bituminous"),
        ("Bituminous", "Bituminous"),
        ("Anthracite", "Anthracite"),
    ]
    coal_type = models.CharField(max_length=15, choices=COAL_TYPE_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.driver.name

    def add_checkpoint(self, checkpoint):
        JourneyCheckpoint.objects.get_or_create(journey=self, checkpoint=checkpoint)

    def remove_checkpoint(self, checkpoint):
        JourneyCheckpoint.objects.filter(journey=self, checkpoint=checkpoint).delete()

class JourneyCheckpoint(models.Model):
    journey = models.ForeignKey(TruckJourney, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Journey: {self.journey.driver.name}, Checkpoint: {self.checkpoint.location.name}, Checkpoint Reached: {self.checkpoint_reached}"

class TrainJourneyCheckpoint(models.Model):
    journey = models.ForeignKey(TrainJourney, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(TrainCheckpoint, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Journey: {self.journey.train_no}, Checkpoint: {self.checkpoint.location.name}, Checkpoint Reached: {self.checkpoint_reached}"


class ShipJourney(models.Model):
    ship_no = models.CharField(max_length=200)
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    COAL_TYPE_CHOICES = [
        ("Lignite", "Lignite"),
        ("Sub-Bituminous", "Sub-Bituminous"),
        ("Bituminous", "Bituminous"),
        ("Anthracite", "Anthracite"),
    ]
    coal_type = models.CharField(max_length=15, choices=COAL_TYPE_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"ShipNo: {self.ship_no}, Buyer: {self.buyer.name}"

class ShipJourneyCheckpoint(models.Model):
    journey = models.ForeignKey(ShipJourney, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(ShipCheckpoint, on_delete=models.CASCADE)
    checkpoint_reached = models.BooleanField(default=False)

    def __str__(self):
        return f"Journey: {self.journey.ship_no}, Checkpoint: {self.checkpoint.location.name}, Checkpoint Reached: {self.checkpoint_reached}"