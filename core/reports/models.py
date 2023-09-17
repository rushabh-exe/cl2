from django.db import models

# Create your models here.

class prodcutions(models.Model):
    Subs = models.CharField(max_length=255)  
    target = models.FloatField(default=0)  
    fyno = models.FloatField(default=0)    
    Achmt = models.FloatField(default=0)    
    pastfyno = models.FloatField(default=0)
    growth = models.FloatField(default=0)  

    def __str__(self):
        return self.Subs

    def save(self, *args, **kwargs):
        if self.target != 0:
            self.Achmt = (self.fyno / self.target) * 100
        else:
            self.Achmt = 0

        if self.pastfyno != 0:
            self.growth = ((self.fyno - self.pastfyno) / self.pastfyno) * 100
        else:
            self.growth = 0

        super(prodcutions, self).save(*args, **kwargs)