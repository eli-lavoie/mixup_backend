''' This file contains the model for an artist on MixUp'''

from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Artist(models.Model):
  """This class is the model for an artist"""

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  artist_name = models.CharField(max_length=30)

  class Meta:
      verbose_name = ("artist")
      verbose_name_plural = ("artists")

  def __str__(self):
    return self.name


