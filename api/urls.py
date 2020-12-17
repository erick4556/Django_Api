from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import DocumentoViewSet, CategoriaViewSet

from .views import prueba

# Para generar un endpoint para cada uno de los métodos
router = routers.DefaultRouter()
router.register("docs", DocumentoViewSet)
router.register("categoria", CategoriaViewSet)

urlpatterns = [
    # path("", prueba, name="prueba")
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
