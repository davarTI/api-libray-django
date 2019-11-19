# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import EditorialSerializer
from .models import Editorial

from libros.models import Libro
from libros.serializers import LibroSerializer

# Create your views here.
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None): #Obtener todos los libros del autor
        editorial = self.get_object()
        libros = Libro.objects.filter(editorial__id=editorial.id)
        serialized = LibroSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este autor no tiene libros'})    
        return Response(status=status.HTTP_200_OK, data=serialized.data)