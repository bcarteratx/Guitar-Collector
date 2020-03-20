from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.

GIGS = (
    ('P', 'Practice'),
    ('C', 'Concert'),
    ('S', 'Studio')
)

class Amp(models.Model):
  name = models.CharField(max_length=50)
  speakers = models.CharField(max_length=20)
  watts = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('amps_detail', kwargs={'pk': self.id})


class Guitar(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    
    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

class Strumming(models.Model):
  date = models.DateField('strumming date')
  gig = models.CharField(
    max_length=1,
    choices=GIGS,
    default=GIGS[0][0]
  )
  guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_gig_display()} on {self.date}"

    # change the default sort
  class Meta:
    ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for guitar_id: {self.guitar_id} @{self.url}"