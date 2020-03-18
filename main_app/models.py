from django.db import models

# Create your models here.
class Guitar(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return self.model 