from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Documento, Categoria
from .serializer import DocumentoSerializer, CategoriaSerializer


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
