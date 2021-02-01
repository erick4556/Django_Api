from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    DocumentoViewSet,
    CategoriaViewSet,
    SubCategoriaViewSet,
    ProductoViewSet,
    ProveedorViewSet,
    ComprasViewSet,
    ComprasDetViewSet,
    ClienteViewSet,
    FacturasViewSet,
    FacturasDetViewSet,
)

from .views import prueba

# Para generar un endpoint para cada uno de los métodos
router = routers.DefaultRouter()
router.register("docs", DocumentoViewSet)
router.register("categoria", CategoriaViewSet)
router.register("subcategoria", SubCategoriaViewSet)
router.register("producto", ProductoViewSet)
router.register("proveedor", ProveedorViewSet)
router.register("compras", ComprasViewSet)
router.register("compras-detalle", ComprasDetViewSet)
router.register("cliente", ClienteViewSet)
router.register("facturas", FacturasViewSet)
router.register("facturas-detalle", FacturasDetViewSet)

urlpatterns = [
    # path("", prueba, name="prueba")
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
