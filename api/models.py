from django.db import models


class Documento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    expira = models.DateField()
    alerta1y = models.BooleanField(default=True)
    alerta6m = models.BooleanField(default=True)
    alerta3m = models.BooleanField(default=True)
    alerta1m = models.BooleanField(default=True)

    # Para que aparezca el contenido de la propiedad nombre
    def __str__(self):
        return self.nombre

    # kwargs es un tipo especial de parametros en el cual se puede pasar una lista de parametros
    # Función para guardar el campo modificado
    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Documento, self).save()

    # Para hacer referencia en la sección de admin del modelo en plural
    class Meta:
        verbose_name_plural = "Documentos"
