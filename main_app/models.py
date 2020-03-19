from django.db import models

# Create your models here.

GIGS = (
    ('P', 'Practice'),
    ('C', 'Concert'),
    ('S', 'Studio')
)

class Guitar(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return self.model

class Strumming(models.Model):
  date = models.DateField('strumming date')
  gig = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=GIGS,
    # set the default value for gig to be 'P'
    default=GIGS[0][0]
  )
  guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_gig_display()} on {self.date}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for guitar_id: {self.guitar_id} @{self.url}"