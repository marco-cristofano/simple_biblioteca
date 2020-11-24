from rest_framework import routers

from libros.api import (
    AutorViewSet,
    LibroViewSet
)
router = routers.SimpleRouter()
router.register(r'autor', AutorViewSet)
router.register(r'libro', LibroViewSet)
urlpatterns = router.urls
