# Sistema-escolar

# Guía para configurar una base de datos MySQL en tu aplicación

Esta guía te llevará a través de los pasos necesarios para configurar una base de datos MySQL en tu aplicación y ejecutar migraciones utilizando un framework como Django.

## Paso 1: Instalación de MySQL

Si aún no tienes MySQL instalado en tu sistema, necesitarás hacerlo. Puedes descargar e instalar MySQL desde el [sitio oficial de MySQL](https://dev.mysql.com/downloads/).

## Paso 2: Crear una base de datos y un usuario en MySQL

Una vez que hayas instalado MySQL, puedes crear una nueva base de datos y un usuario que tenga permisos para acceder a esa base de datos. Puedes hacerlo utilizando el cliente de MySQL o cualquier interfaz gráfica de usuario que prefieras.

```sql
CREATE DATABASE nombre_basedatos;
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON nombre_basedatos.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

Recuerda reemplazar `nombre_basedatos`, `usuario`, y `contraseña` con los valores que desees.

## Paso 3: Configurar la base de datos en tu aplicación

En tu aplicación, generalmente necesitarás configurar la conexión a la base de datos en un archivo de configuración, como `settings.py` si estás utilizando Django. Aquí hay un ejemplo de cómo puedes configurar la base de datos MySQL en Django:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_basedatos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Nuevamente, asegúrate de reemplazar `nombre_basedatos`, `usuario`, y `contraseña` con los valores que has configurado en MySQL.

## Paso 4: Preparar migraciones

Antes de ejecutar las migraciones, necesitas crearlas. Si estás utilizando Django, puedes generar las migraciones ejecutando el siguiente comando en la terminal:

```bash
python manage.py makemigrations
```

## Paso 5: Ejecutar migraciones

Una vez que hayas preparado las migraciones, puedes aplicarlas a la base de datos ejecutando el siguiente comando:

```bash
python manage.py migrate
```

Esto creará todas las tablas necesarias en tu base de datos MySQL según las definiciones de modelos en tu aplicación.

¡Eso es todo! Ahora tienes una base de datos MySQL configurada y lista para usar en tu aplicación.

## Paso 6: Agregar Usuarios
Esto creará usuarios para poder utilizar el sistema:
```bash
python manage.py crear_usuario
```