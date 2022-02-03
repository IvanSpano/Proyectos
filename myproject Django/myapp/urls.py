from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("curso", views.curso, name="curso"),
    path("nuevo-curso", views.nuevo_curso, name="nuevo_curso")

]
