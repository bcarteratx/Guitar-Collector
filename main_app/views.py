from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse
from .models import Guitar, Photo
### for s3
import uuid
import boto3 #sdk to interact with aws bucket
S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'guitarcollectorone'

# Create your views here.
class GuitarCreate(CreateView):
  model = Guitar
  fields = '__all__'

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = ['model', 'brand', 'description', 'year']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

def home(request):
  return HttpResponse('<h1>Hello Guitarists</h1>')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
  guitars = Guitar.objects.all()
  return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
  guitar = Guitar.objects.get(id=guitar_id)
  return render(request, 'guitars/detail.html', { 'guitar': guitar })



def add_photo(request, guitar_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to guitar_id or guitar (if you have a guitar object)
            photo = Photo(url=url, guitar_id=guitar_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', guitar_id=guitar_id)