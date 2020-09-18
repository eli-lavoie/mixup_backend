from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from mixupAPI.models import Genre

class GenreSerializer(serializers.HyperlinkedModelSerializer):
  """JSON Serializer for MixUp genres"""

  class Meta:
    model = Genre
    url = serializers.HyperlinkedIdentityField(
      view_name="genre",
      lookup_field="id"
    )
    fields = ('id', 'url', 'genre_name')


class Genres(ViewSet):

  def retrieve(self, request, pk=None):
    try:
      genre = Genre.objects.get(pk=pk)
      serializer = GenreSerializer(genre, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    genres = Genre.objects.all()

    serializer = GenreSerializer(
      genres, many=True, context={'request': request}
    )
    return Response(serializer.data)

  def destroy(self, request, pk=None):
    try:
      genre = Genre.objects.get(pk=pk)
      genre.delete()
      return Response({}, status=status.HTTP_204_NO_CONTENT)

    except Genre.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status.HTTP_404_NOT_FOUND)

    except Exception as ex:
      return HttpResponseServerError(ex)
  
  def create(self, request):
    new_genre = Genre()
    new_genre.genre_name = request.data['genre_name']

    new_genre.save()

    serializer = GenreSerializer(new_genre, context={'request': request})

    return Response(serializer.data)