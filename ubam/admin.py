from django.contrib import admin
from .models import Docente, Alumno, Grupo, Asignatura, Calificacion

admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(Asignatura)
admin.site.register(Calificacion)