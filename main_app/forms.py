from django.forms import ModelForm
from .models import Strumming

class StrummingForm(ModelForm):
  class Meta:
    model = Strumming
    fields = ['date', 'gig']