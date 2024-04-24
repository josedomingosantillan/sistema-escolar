from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ubam.forms import DocenteForm, AlumnoForm, GrupoForm, AsignaturaForm, CalificacionForm
from ubam.models import Docente, Alumno, Grupo, Asignatura, Calificacion


@login_required
def menu_principal(request):
    return render(request, 'menu_principal.html')


@login_required
def ver_docentes(request):
    docentes = Docente.objects.all()
    return render(request, '../templates/docente/ver_docentes.html', {'docentes': docentes})


@login_required
def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_docentes')
    else:
        form = DocenteForm()
    return render(request, '../templates/docente/crear_docente.html', {'form': form})


@login_required
def detalle_docente(request, docente_id):
    docente = Docente.objects.get(pk=docente_id)
    return render(request, '../templates/docente/detalle_docente.html', {'docente': docente})


@login_required
def editar_docente(request, docente_id):
    docente = Docente.objects.get(pk=docente_id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('detalle_docente', docente_id=docente_id)
    else:
        form = DocenteForm(instance=docente)
    return render(request, '../templates/docente/editar_docente.html', {'form': form, 'docente': docente})


@login_required
def eliminar_docente(request, docente_id):
    docente = Docente.objects.get(pk=docente_id)
    docente.delete()
    return redirect('ver_docentes')


@login_required
def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, '../templates/alumno/ver_alumno.html', {'alumnos': alumnos})


@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_alumnos')
    else:
        form = AlumnoForm()
    return render(request, '../templates/alumno/crear_alumno.html', {'form': form})


@login_required
def detalle_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    return render(request, '../templates/alumno/detalle_alumno.html', {'alumno': alumno})


@login_required
def editar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('detalle_alumno', alumno_id=alumno_id)
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, '../templates/alumno/editar_alumno.html', {'form': form, 'alumno': alumno})


@login_required
def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    alumno.delete()
    return redirect('ver_alumnos')


@login_required
def ver_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, './grupo/ver_grupo.html', {'grupos': grupos})


@login_required
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_grupos')
    else:
        form = GrupoForm()
    return render(request, './grupo/crear_grupo.html', {'form': form})


@login_required
def detalle_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    return render(request, './grupo/detalle_grupo.html', {'grupo': grupo})


@login_required
def editar_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('detalle_grupo', grupo_id=pk)
    else:
        form = GrupoForm(instance=grupo)
    return render(request, './grupo/editar_grupo.html', {'form': form})


@login_required
def eliminar_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    grupo.delete()
    return redirect('ver_grupos')


@login_required
def ver_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, './asignatura/ver_asignatura.html', {'asignaturas': asignaturas})


@login_required
def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, './asignatura/crear_asignatura.html', {'form': form})


@login_required
def detalle_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    return render(request, './asignatura/detalle_asignatura.html', {'asignatura': asignatura})


@login_required
def editar_asignatura(request, pk=None):
    if pk:
        asignatura = get_object_or_404(Asignatura, pk=pk)
    else:
        asignatura = Asignatura()

    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('detalle_asignatura', pk=pk)
    else:
        form = AsignaturaForm(instance=asignatura)

    return render(request, './asignatura/editar_asignatura.html', {'form': form})


@login_required
def eliminar_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    asignatura.delete()
    return redirect('ver_asignaturas')


@login_required
def ver_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, './calificacion/ver_calificacion.html', {'calificaciones': calificaciones})


@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, './calificacion/crear_calificacion.html', {'form': form})


@login_required
def detalle_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    return render(request, './calificacion/detalle_calificacion.html', {'calificacion': calificacion})


@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_calificacion', pk=pk)
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, './calificacion/editar_calificacion.html', {'form': form})


@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    calificacion.delete()
    return redirect('ver_calificaciones')
