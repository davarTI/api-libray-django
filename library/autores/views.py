from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import AutorSerializer
from .models import Autor
from libros.models import Libro
from libros.serializers import LibroSerializer


# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None): #Obtener todos los libros del autor
        autor = self.get_object()
        libros = Libro.objects.filter(autores__id=autor.id)
        serialized = LibroSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este autor no tiene libros'})    
        return Response(status=status.HTTP_200_OK, data=serialized.data)