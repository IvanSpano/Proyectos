#Agrega cajas para rellenar con información. en Views.py está la función para agregar esa info a la tabla utilizada

"""
from django import forms
class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")

#Agrega una caja para ponerle un tilde, un booleano

class FormularioCurso(forms.Form):
 nombre = forms.CharField(label="Nombre", max_length=128)
 inscriptos = forms.IntegerField(label="Inscriptos")
 solo_empresas = forms.BooleanField(label="¿Solo empresas?", required=False)

#Agrega una lista de opcoines

class FormularioCurso(forms.Form):
 nombre = forms.CharField(label="Nombre", max_length=128)
 inscriptos = forms.IntegerField(label="Inscriptos")
 TURNOS = (
 (1, "Mañana"),
 (2, "Tarde"),
 (3, "Noche")
 )
 turno = forms.ChoiceField(label="Turno", choices=TURNOS)
"""

from django.forms import ModelForm
from .models import Curso

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno")