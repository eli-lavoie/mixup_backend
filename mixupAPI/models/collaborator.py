"""This file contains the model for a track collaborator"""

from django.db import models
from django.db.models import F
from .track import Track
from .artist import Artist

class Collaborator(models.Model):

  track = models.ForeignKey(Track, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  class Meta:
      verbose_name = ("collaborator")
      verbose_name_plural = ("collaborators")

  def __str__(self):
      return self.name

