from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from mixupAPI.models import Artist
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = User
    url = serializers.HyperlinkedIdentityField(
      view_name="user",
      lookup_field="id"
    )
    fields = (
      "id",
      'first_name',
      'last_name',
      'date_joined',
      'email'
    )

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

  user = UserSerializer()
  
  class Meta:
    model = Artist
    url = serializers.HyperlinkedIdentityField(
      view_name="artist",
      lookup_field='id'
    )
    fields = (
      'id',
      'url',
      'user',
      'artist_name'
    )

class Artists(ViewSet):
  def retrieve(self, request, pk=None):

    try:
      artist = Artist.objects.get(pk=pk)

      serializer = ArtistSerializer(artist, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    artists = Artist.objects.all()

    serializer = ArtistSerializer(artists, many=True, context={'request': request})

    return Response(serializer.data)