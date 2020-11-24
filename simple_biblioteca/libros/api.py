from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from libros.serializers import (
    AutorSerializer,
    LibroConAutorSerializer,
    LibroSerializer

)
from libros.models import (
    Autor,
    Libro
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=True, methods=['get'], url_path='libro_con_autor')
    def libro_con_autor(self, request, pk=None):
        libro = self.get_object()
        serializer = LibroConAutorSerializer(libro)
        return Response(serializer.data)
