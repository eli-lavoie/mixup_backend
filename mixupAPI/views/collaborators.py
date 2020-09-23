from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from mixupAPI.models import Artist, Track, Collaborator

class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Collaborator
    url = serializers.HyperlinkedIdentityField(
      view_name="collaborator",
      lookup_field='id'
    )
    fields=('id', 'url', 'track', 'artist')

class Collaborators(ViewSet):

  def list(self, request):
    collaborators = Collaborator.objects.all()
    serializer = CollaboratorSerializer(collaborators, many=True, context={'request': request} )

    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    try:
      collaborator = Collaborator.objects.get(pk=pk)

      serializer = CollaboratorSerializer(collaborator, context={'request': request})
      return Response(serializer.data)

    except Exception as ex:
      return HttpResponseServerError(ex)

  def create(self, request):
    artist = Artist.objects.get(artist_name=request.data['artist_name'])
    track = Track.objects.get(pk=request.data['track_id'])

    new_collaborator = Collaborator()

    new_collaborator.track = track
    new_collaborator.artist = artist

    new_collaborator.save()

    serializer = CollaboratorSerializer(new_collaborator, context={'request': request})
    return Response(serializer.data)

  def destroy(self, request, pk=None):
    try:
      collaborator = Collaborator.objects.get(pk=pk)

      collaborator.delete()
      return Response({}, status=status.HTTP_204_NO_CONTENT)

    except Collaborator.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status.HTTP_404_NOT_FOUND)
    
    except Exception as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
