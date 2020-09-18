"""This file contains the model for a file to be used on a track"""

from django.db import models
from django.db.models import F
from .track import Track
from .artist import Artist

class Track_File(models.Model):

  name = models.CharField(max_length=30)
  description = models.CharField(max_length=75)
  track = models.OneToOneField(Track, on_delete=models.CASCADE)
  artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
  url = models.CharField(max_length=150)
  dateUploaded = models.DateField(auto_now_add=True)


  class Meta:
      verbose_name = ("track file")
      verbose_name_plural = ("track files")

  def __str__(self):
      return self.name

