from django.db import models
from django.db.models.signals import pre_save
from myportfolio.utils import unique_slug_generator
# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    resumen = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True)
    imagen = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Proyecto)
