from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import LibroSerializer, LibroCreateSerializer
from .models import Libro
from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from autores.models import Autor
from editoriales.models import Editorial

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return LibroCreateSerializer
        return LibroSerializer

    @action(detail=True, methods=['GET'])
    def autores(self, request, pk=None): #Obtener todos los autores del libro
        libro = self.get_object()
        autores = Autor.objects.filter(libro__id=libro.id)
        serialized = AutorSerializer(autores, many=True)
        if not autores:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene autores'})    
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def editoriales(self, request, pk=None): #Obtener todos los autores del libro
        libro = self.get_object()
        editoriales = Editorial.objects.filter(libro__id=libro.id)
        serialized = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene editoriales'})    
        return Response(status=status.HTTP_200_OK, data=serialized.data)