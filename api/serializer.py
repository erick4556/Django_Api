from rest_framework import serializers

from .models import (
    Documento,
    Categoria,
    SubCategoria,
    Producto,
    Proveedor,
    ComprasDet,
    ComprasEnc,
    Cliente,
)


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


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class ComprasDetSerializer(serializers.ModelSerializer):
    producto_descripcion = serializers.ReadOnlyField(source="producto.descripcion")

    class Meta:
        model = ComprasDet
        fields = [
            "cabecera",
            "id",
            "producto",
            "cantidad",
            "precio",
            "subtotal",
            "descuento",
            "total",
            "producto_descripcion",
        ]


class ComprasSerializer(serializers.ModelSerializer):
    # Son muchos los detalles que va devolver
    detalle = ComprasDetSerializer(many=True, read_only=True)

    class Meta:
        model = ComprasEnc
        fields = ["id", "proveedor", "fecha", "detalle"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
