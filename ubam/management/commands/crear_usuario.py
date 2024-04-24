from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = 'Crea un nuevo usuario'

    def handle(self, *args, **options):
        username = input("Ingrese el nombre de usuario: ")
        email = input("Ingrese el correo electrónico: ")
        password = input("Ingrese la contraseña: ")

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password)

        # Determinar el rol del usuario (docente, alumno, etc.)
        role = input("Ingrese el rol del usuario (docente, alumno, administrador.): ")

        # Obtener o crear el grupo correspondiente al rol
        group, _ = Group.objects.get_or_create(name=role)

        # Asignar al usuario al grupo
        user.groups.add(group)

        self.stdout.write(self.style.SUCCESS('Usuario creado exitosamente'))
