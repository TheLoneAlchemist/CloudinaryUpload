from django.forms import ModelForm      
from .models import Song

class PhotoForm(ModelForm):
  class Meta:
      model = Song
      fields = '__all__'
      