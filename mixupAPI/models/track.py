"""This file contains the model for a track on MixUp"""

from django.db import models
from django.db.models import F
from .artist import Artist
from .genre import Genre

class Track(models.Model):

  creatorId = models.ForeignKey(Artist, on_delete=models.CASCADE)
  track_name = models.CharField(max_length=30, null=True)
  dateCreated = models.DateField(auto_now_add=True)
  lastUpdated = models.DateField(auto_now=True)
  openForRemix = models.BooleanField()
  genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
  bpm = models.IntegerField()

  class Meta:
      verbose_name = ("track")
      verbose_name_plural = ("tracks")

  def __str__(self):
      return self.name


