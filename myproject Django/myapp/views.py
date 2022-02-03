from django.shortcuts import render
import sqlite3
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curso


# Create your views here.
from django.http import HttpResponse

def index(request):
    ctx = {
    "alumnos": ["Juan", "Sofía", "Matias"]
    }
    return render(request, "myapp/index.html", ctx)


def curso(request):
    curso = Curso.objects.all()
    ctx = {"cursos": curso}
    return render(request, "myapp/curso.html", ctx)


"""
def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("test.db")
            cursor = conn.cursor()
            cursor.execute(
            "INSERT INTO cursos(nombre, inscriptos) VALUES(?,?)",
            (form.cleaned_data["nombre"], form.cleaned_data["inscriptos"])
            )
            conn.commit()
            conn.close()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)
"""
def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("curso"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)