"""This file contains the model for a genre"""

from django.db import models
from django.db.models import F

class genre(models.Model):

  genre_name = models.CharField(max_length=50)

  class Meta:
      verbose_name = ("genre")
      verbose_name_plural = ("genres")

  def __str__(self):
      return self.name

