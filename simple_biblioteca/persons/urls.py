from django.urls import path

from rest_framework import routers

from persons.api import (
    NombresPersonasListApiView,
    PersonaViewSet,
    MinimaPersonaViewSet,

)

router = routers.SimpleRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'persona_minima', MinimaPersonaViewSet)
urlpatterns = router.urls
urlpatterns += [path('listado_nombres/', NombresPersonasListApiView.as_view())]
