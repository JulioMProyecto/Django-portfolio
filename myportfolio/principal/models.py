from django.db import models

# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    resumen = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titulo
