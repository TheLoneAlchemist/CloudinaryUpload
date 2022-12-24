from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=300,unique=True)
    # image = models.ImageField(upload_to = 'image')
    # song = models.FileField(upload_to='audio')
    image = CloudinaryField('image')
    song  = CloudinaryField('audio',default="",resource_type ='auto')
    def __str__(self) -> str:
        return self.song_name