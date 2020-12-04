from rest_framework import routers

from libros.api import (
    AutorListViewSet,
    AutorViewSet,
    LibroViewSet
)

router = routers.SimpleRouter()
router.register(r'autor', AutorViewSet)
router.register(r'libro', LibroViewSet)
router.register(r'autorList', AutorListViewSet)
urlpatterns = router.urls
