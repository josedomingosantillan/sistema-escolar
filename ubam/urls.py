"""
URL configuration for ubam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from ubam.views import menu_principal, detalle_docente, editar_docente, crear_docente, eliminar_docente, ver_docentes, \
    ver_alumnos, crear_alumno, detalle_alumno, editar_alumno, eliminar_alumno, ver_grupos, crear_grupo, editar_grupo, \
    eliminar_grupo, detalle_grupo, ver_asignaturas, crear_asignatura, detalle_asignatura, eliminar_asignatura, \
    editar_asignatura, ver_calificaciones, crear_calificacion, detalle_calificacion, eliminar_calificacion, \
    editar_calificacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('menu-principal/', menu_principal, name='menu_principal'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('docentes/', ver_docentes, name='ver_docentes'),
    path('registrar/docente/', crear_docente, name='crear_docente'),
    path('docentes/<int:docente_id>/', detalle_docente, name='detalle_docente'),
    path('docentes/<int:docente_id>/editar/', editar_docente, name='editar_docente'),
    path('docentes/<int:docente_id>/eliminar/', eliminar_docente, name='eliminar_docente'),
    path('alumnos/', ver_alumnos, name='ver_alumnos'),
    path('registrar/alumno/', crear_alumno, name='crear_alumno'),
    path('alumnos/<int:alumno_id>/', detalle_alumno, name='detalle_alumno'),
    path('alumnos/<int:alumno_id>/editar/', editar_alumno, name='editar_alumno'),
    path('alumnos/<int:alumno_id>/eliminar/', eliminar_alumno, name='eliminar_alumno'),
    path('grupos/', ver_grupos, name='ver_grupos'),
    path('registrar/grupo/', crear_grupo, name='crear_grupo'),
    path('grupo/<int:grupo_id>/', detalle_grupo, name='detalle_grupo'),
    path('grupo/<int:pk>/', editar_grupo, name='editar_grupo'),
    path('grupo/eliminar/<int:pk>/', eliminar_grupo, name='eliminar_grupo'),
    path('asignaturas/', ver_asignaturas, name='ver_asignaturas'),
    path('asignaturas/crear/', crear_asignatura, name='crear_asignatura'),
    path('asignaturas/<int:pk>/', detalle_asignatura, name='detalle_asignatura'),
    path('asignatura/<int:pk>/', editar_asignatura, name='editar_asignatura'),
    path('asignaturas/<int:pk>/eliminar/', eliminar_asignatura, name='eliminar_asignatura'),
    path('calificaciones/', ver_calificaciones, name='ver_calificaciones'),
    path('calificaciones/crear/', crear_calificacion, name='crear_calificacion'),
    path('calificaciones/<int:pk>/', detalle_calificacion, name='detalle_calificacion'),
    path('calificaciones/<int:pk>/editar/', editar_calificacion, name='editar_calificacion'),
    path('calificaciones/<int:pk>/eliminar/', eliminar_calificacion, name='eliminar_calificacion'),
]
