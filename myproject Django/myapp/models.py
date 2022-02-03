from django.db import models

# Create your models here.

from django.db import models
"""
class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    turno = models.PositiveSmallintegerfield(choices=TURNOS, null=True)
"""
class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turno = models.PositiveSmallIntegerField(choices=TURNOS, null=True)
    profesor = models.ForeignKey("Profesor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()

    class Meta:
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre
