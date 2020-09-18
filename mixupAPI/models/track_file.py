"""This file contains the model for a file to be used on a track"""

from django.db import models
from django.db.models import F
from .track import track
from .artist import artist

class track_file(models.Model):

  name = models.CharField(max_length=30)
  description = models.CharField(max_length=75)
  track = models.OneToOneField(track, on_delete=models.CASCADE)
  artist = models.OneToOneField(artist, on_delete=models.CASCADE)
  url = models.CharField(max_length=150)
  dateUploaded = models.DateField(auto_now_add=True)


  class Meta:
      verbose_name = ("track file")
      verbose_name_plural = ("track files")

  def __str__(self):
      return self.name

