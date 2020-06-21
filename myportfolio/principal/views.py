from django.shortcuts import render
from .models import Proyecto
# Create your views here.


def inicio(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "principal/index.html", context)


def trabajos(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "principal/trabajos.html", context)
