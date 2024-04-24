from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from ubam.models import Grupo, Alumno, Docente, Asignatura, Calificacion


class Command(BaseCommand):
    content_type_grupo = ContentType.objects.get_for_model(Grupo)
    content_type_alumno = ContentType.objects.get_for_model(Alumno)
    content_type_docente = ContentType.objects.get_for_model(Docente)
    content_type_asignatura = ContentType.objects.get_for_model(Asignatura)
    content_type_calificacion = ContentType.objects.get_for_model(Calificacion)
    help = 'Asigna permisos a grupos de usuarios'

    def handle(self, *args, **options):
        # Obtener o crear los permisos personalizados
        content_type_grupo = ContentType.objects.get_for_model(Grupo)

        permiso_administrar_grupos = Permission.objects.create(
            codename='puede_administrar_grupos',
            name='Puede administrar grupos',
            content_type=content_type_grupo
        )

        permiso_registrar_alumnos = Permission.objects.create(
            codename='puede_registrar_alumnos',
            name='Puede registrar alumnos',
            content_type=content_type_grupo
        )

        permiso_registrar_docentes = Permission.objects.create(
            codename='puede_registrar_docentes',
            name='Puede registrar docentes',
            content_type=content_type_grupo
        )

        permiso_asignar_calificaciones = Permission.objects.create(
            codename='puede_asignar_calificaciones',
            name='Puede asignar calificaciones',
            content_type=content_type_grupo
        )

        permiso_consultar_materias_calificaciones = Permission.objects.create(
            codename='puede_consultar_materias_calificaciones',
            name='Puede consultar sus materias y calificaciones',
            content_type=content_type_grupo
        )

        # Obtener o crear los grupos correspondientes
        grupo_administrador, _ = Group.objects.get_or_create(name='Administrador')
        grupo_docente, _ = Group.objects.get_or_create(name='Docente')
        grupo_alumno, _ = Group.objects.get_or_create(name='Alumno')

        # Asignar permisos a los grupos
        grupo_administrador.permissions.add(
            permiso_administrar_grupos,
            permiso_registrar_alumnos,
            permiso_registrar_docentes,
            permiso_asignar_calificaciones,
            permiso_consultar_materias_calificaciones
        )

        grupo_docente.permissions.add(
            permiso_registrar_alumnos,
            permiso_asignar_calificaciones
        )

        grupo_alumno.permissions.add(
            permiso_consultar_materias_calificaciones
        )

        self.stdout.write(self.style.SUCCESS('Permisos asignados a los grupos correctamente'))
