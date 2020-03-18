from django.shortcuts import render
from django.http import HttpResponse
from .models import Guitar

# Create your views here.

class Guitar:
  def __init__(self, model, brand, description, year):
    self.model = model
    self.brand = brand
    self.description = description
    self.year = year

guitars = [
  Guitar('Telecaster', 'Fender', 'Sunburst Deluxe with wide range humbuckers', 1973),
  Guitar('Jazzmaster', 'Fender', 'Olympic White with tortoise shell pickguard', 2010),
  Guitar('Casino', 'Epiphone', 'USA made reissue', 2020)
]   

def home(request):
  return HttpResponse('<h1>Hello Guitarists</h1>')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
#  guitars = Guitar.objects.all()
  return render(request, 'guitars/index.html', { 'guitars': guitars })
