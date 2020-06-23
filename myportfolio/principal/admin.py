from django.contrib import admin
from .models import Proyecto

from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class ProyectoAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Proyecto, ProyectoAdmin)
