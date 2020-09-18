"""This file contains the model for a track on MixUp"""

from django.db import models
from django.db.models import F
from .artist import artist
from .genre import genre

class track(models.Model):

  creatorId = models.OneToOneField(artist, on_delete=models.CASCADE)
  dateCreated = models.DateField(auto_now_add=True)
  lastUpdated = models.DateField(auto_now=True)
  openForRemix = models.BooleanField()
  genre = models.OneToOneField(genre, on_delete=models.CASCADE)
  bpm = models.IntegerField()

  class Meta:
      verbose_name = ("track")
      verbose_name_plural = ("tracks")

  def __str__(self):
      return self.name


