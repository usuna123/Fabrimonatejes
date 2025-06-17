from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def inicio(request):
    return render(request, 'Inicio.html')

def Contrasena(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('correo')
        nueva_contrasena = request.POST.get('nueva_contrasena')

        try:
            usuario = User.objects.get(username=username, email=email)
            usuario.set_password(nueva_contrasena)
            usuario.save()
            messages.success(request, '¡Contraseña actualizada correctamente!')
            return redirect('inicio')  # O el nombre de tu login
        except User.DoesNotExist:
            messages.error(request, 'Usuario o correo no válidos.')

    return render(request, 'Contrasena.html', )
