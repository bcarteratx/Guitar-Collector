from django.shortcuts import render
from django.http import HttpResponse
from .models import Guitar

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello Guitarists</h1>')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
  guitars = Guitar.objects.all()
  return render(request, 'guitars/index.html', { 'guitars': guitars })
