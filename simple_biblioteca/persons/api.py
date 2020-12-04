from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from persons.serializers import (
    MinimaPersonaSerializer,
    PersonaSerializer
)
from persons.models import Persona


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class MinimaPersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = MinimaPersonaSerializer


class NombresPersonasListApiView(APIView):

    def get(self, request):
        nombres = Persona.objects.values('nombre')
        return Response(nombres)
