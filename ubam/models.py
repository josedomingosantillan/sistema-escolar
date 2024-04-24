from django.db import models


class CustomPermission(models.Model):
    class Meta:
        permissions = [
            ("puede_registrar_docente", "Puede registrar docentes"),
            ("puede_registrar_alumno", "Puede registrar alumnos"),
            ("puede_registrar_grupo", "Puede registrar grupos"),
            ("puede_registrar_asignatura", "Puede registrar asignaturas"),
            ("puede_asignar_calificaciones", "Puede asignar calificaciones"),
            ("puede_consultar_materias", "Puede consultar materias"),
            ("puede_consultar_calificaciones", "Puede consultar calificaciones"),
        ]

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="grupos")

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name="asignaturas")

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="calificaciones")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="calificaciones")
    calificacion = models.FloatField()

    def __str__(self):
        return f"{self.calificacion} - {self.alumno} en {self.asignatura}"
