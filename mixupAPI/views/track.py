from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from mixupAPI.models import Track, Artist, Genre
import datetime

class TrackSerializer(serializers.HyperlinkedModelSerializer):
  """JSON Serializer for a track"""

  class Meta:
    model = Track
    url = serializers.HyperlinkedIdentityField(
      view_name="track",
      lookup_field='id'
    )
    fields=('id', 'url', 'creatorId', 'track_name', 'dateCreated', 'lastUpdated', 'openForRemix', 'genre', 'bpm')


class Tracks(ViewSet):
  '''Track for MixUp'''

  def retrieve(self, request, pk=None):
    """Handles single track get requests"""

    try:
      track = Track.objects.get(pk=pk)
      serializer = TrackSerializer(track, context={'request':request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

    def list(self, request):
      tracks = Track.objects.all()
      serializer = TrackSerializer(
        tracks,
        many=True,
        context={'request': request}
      )
      return Response(serializer.data)

    def create(self, request):
      """Handles a POST operation for creating a track"""

      artist = Artist.objects.get(user=request.auth.user)
      genre = Genre.objects.get(pk=request.data['genre_id'])


      new_track = Track()
      new_track.creatorId = artist
      new_track.track_name = request.data["track_name"]
      new_track.dateCreated = datetime.now
      new_track.lastUpdated = datetime.now
      new_track.openForRemix = request.data['open_for_remix']
      new_track.genre = genre
      new_track.bpm = request.data['bpm']

      new_track.save()

      serializer = TrackSerializer(new_track, context={'request': request})
      return Response(serializer.data)