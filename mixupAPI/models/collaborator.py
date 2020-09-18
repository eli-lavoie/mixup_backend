"""This file contains the model for a track collaborator"""

from django.db import models
from django.db.models import F
from .track import track
from .artist import artist

class collaborator(models.Model):

  track = models.OneToOneField(track, on_delete=models.CASCADE)
  artist = models.OneToOneField(artist, on_delete=models.CASCADE)

  class Meta:
      verbose_name = ("collaborator")
      verbose_name_plural = ("collaborators")

  def __str__(self):
      return self.name

