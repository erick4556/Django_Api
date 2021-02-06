from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets
from .models import (
    Documento,
    Categoria,
    SubCategoria,
    Producto,
    Proveedor,
    ComprasEnc,
    ComprasDet,
    Cliente,
    FacturaEnc,
    FacturaDet,
)
from .serializer import (
    DocumentoSerializer,
    CategoriaSerializer,
    SubCategoriaSerializer,
    ProductoSerializer,
    ProveedorSerializer,
    ComprasDetSerializer,
    ComprasSerializer,
    ClienteSerializer,
    FacturasDetSerializer,
    FacturasSerializer,
)


def prueba(reqest):
    return HttpResponse("Respuesta")


class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Documento.objects.all().order_by("id")
    serializer_class = DocumentoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all().order_by("descripcion")
    serializer_class = CategoriaSerializer


class SubCategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubCategoria.objects.all().order_by("descripcion")
    serializer_class = SubCategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all().order_by("descripcion")
    serializer_class = ProductoSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Proveedor.objects.all().order_by("nombre")
    serializer_class = ProveedorSerializer


class ComprasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasEnc.objects.all().order_by("id")
    serializer_class = ComprasSerializer


class ComprasDetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasDet.objects.all().order_by("id")
    serializer_class = ComprasDetSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by("nombre")
    serializer_class = ClienteSerializer

    @action(
        methods=["get"],
        detail=False,
        permission_classes=[],
        url_path="by-name/(?P<nombre>[\w\ ]+)",
    )  # P significa una palabra que es nombre, va ser cualquier palabra y cualquier espacio en blanco. El + para que se pueda repetir varias veces
    def by_name(self, request, pk=None, nombre=None):
        print(nombre)
        obj = Cliente.objects.filter(
            nombre__icontains=nombre, estado=True
        )  # __icontains insesitive case, que no distingue entre mayuscula y minuscula
        if not obj:
            return Response({"detail": "No existe cliente"})
        else:
            serializador = ClienteSerializer(
                obj, many=True
            )  # many=True por que puede devolver mas de un registro
            return Response(serializador.data)


class FacturasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FacturaEnc.objects.all().order_by("id")
    serializer_class = FacturasSerializer


class FacturasDetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FacturaDet.objects.all().order_by("id")
    serializer_class = FacturasDetSerializer