from django.shortcuts import render, HttpResponse
from .models import Proyecto
# Create your views here.


def inicio(request):
    # proyectos = Proyecto.objects.all()
    # context = {"proyectos": proyectos}
    # return render(request, "principal/index_es.html", context)

    from django.utils import translation
    language = request.session.get(translation.LANGUAGE_SESSION_KEY)

    if language == "en":
        proyectos = Proyecto.objects.all()
        context = {"proyectos": proyectos}
        return render(request, 'principal/indexEN.html', context)
    else:
        proyectos = Proyecto.objects.all()
        context = {"proyectos": proyectos}
        return render(request, 'principal/indexES.html', context)


def trabajos(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "principal/trabajos.html", context)


def detalles(request, slug_text):
    proyecto = Proyecto.objects.filter(slug=slug_text)
    if proyecto.exists():
        proyecto = proyecto.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")

    context = {'proyecto': proyecto}

    return render(request, "principal/detalles.html", context)
