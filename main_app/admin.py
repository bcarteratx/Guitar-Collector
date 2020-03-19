from django.contrib import admin
# import your models here
from .models import Guitar, Strumming, Photo

# Register your models here
admin.site.register(Guitar)
admin.site.register(Strumming)
admin.site.register(Photo)