from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from mixupAPI.models import Track, Track_File, Artist
import datetime

class TrackFileSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Track_File
    url = serializers.HyperlinkedIdentityField(
      view_name="track_file",
      lookup_field="id"
    )
    fields=('id', 'url', 'name', 'description', 'track','artist', 'url', 'dateUploaded')

class Track_Files(ViewSet):

  def retrieve(self, request, pk=None):
    try:
      file = Track_File.objects.get(pk=pk)

      serializer = TrackFileSerializer(file, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    files = Track_File.objects.all()

    serializer = TrackFileSerializer(files, many=True, context={'request': request})
    
    return Response(serializer.data)

  def create(self, request):

    artist = Artist.objects.get(user=request.auth.user)
    track = Track.objects.get(pk=request.data['track_id'])
    today = datetime.date.today()
    date = today.strftime('%Y/%m/%d')

    new_file = Track_File()
    new_file.name = request.data['file_name']
    new_file.description = request.data['file_description']
    new_file.track = track
    new_file.artist = artist
    new_file.url = request.data['file_url']
    date_uploaded =  date

    new_file.save()

    serializer = TrackFileSerializer(new_file, context={'request': request})
    return Response(serializer.data)