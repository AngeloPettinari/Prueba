from django.shortcuts import render
from AppAirsoft.models import * 
from AppAirsoft.forms import *

# Creamos nuestras views

def vista_inicio(request):
    return render(request, "Airsoft\index.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["contrasenia"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "Airsoft/registro.html", {"formulario": formulario})

def vista_equipamiento(request):
    if request.method == "POST":
        formulario = EquipamientoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipamiento = Equipamiento(tipo_de_equipamiento = data["tipo_de_equipamiento"], precio = data["precio"], accesorios = data["accesorios"])
            equipamiento.save()
    formulario = EquipamientoForm()
    return render(request, "Airsoft/equipamiento.html", {"formulario": formulario})

def vista_replica(request):
    if request.method == "POST":
        formulario = ReplicaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            replica = Replica(nombre_replica = data["nombre_replica"], precio = data["precio"])
            replica.save()
    formulario = ReplicaForm()
    return render(request, "Airsoft/replica.html", {"formulario": formulario})

def vista_inicio_sesion(request):
    return render(request, "Airsoft/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "Airsoft/busqueda.html")

