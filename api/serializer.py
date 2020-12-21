from rest_framework import serializers

from .models import Documento, Categoria, SubCategoria, Producto


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"  # Se incluye todos los campos del modelo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"  # Se incluye todos los campos del modelo


class SubCategoriaSerializer(serializers.ModelSerializer):
    cat_descripcion = serializers.ReadOnlyField(source="categoria.descripcion")

    class Meta:
        model = SubCategoria
        fields = ("id", "categoria", "descripcion", "cat_descripcion")


class ProductoSerializer(serializers.ModelSerializer):
    scat_descripcion = serializers.ReadOnlyField(source="subcategoria.descripcion")

    class Meta:
        model = Producto
        fields = (
            "id",
            "codigo",
            "descripcion",
            "existencia",
            "precio",
            "subcategoria",
            "scat_descripcion",
        )
