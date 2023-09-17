from django.db import models

# Create your models here.

class addProduction(models.Model):
    month = models.DateTimeField(auto_now_add=True)
    target = models.IntegerField(help_text="Target value in MT",default=0)
