from django.shortcuts import render, redirect
from django.http import HttpResponse
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from firebase_config import db


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        clave = request.POST.get('clave')

        # Leer todos los usuarios
        usuarios_snap = db.child("usuarios").get()
        usuarios = usuarios_snap.val() or {}

        usuario_valido = None
        for key, data in usuarios.items():
            if data.get('username') == username and data.get('clave') == clave:
                usuario_valido = data
                break

        if usuario_valido:
            request.session['usuario'] = usuario_valido.get('username')
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Usuario o clave incorrectos',
            })

    return render(request, 'login.html')


def dashboard_view(request):
    usuario = request.session.get('usuario', 'Invitado')
    return render(request, 'dashboard.html', {'usuario': usuario})


def test_firebase(request):
    data = {
        "nombre": "Prueba",
        "apellido": "Usuario",
        "username": "prueba1",
        "email": "prueba@example.com",
        "clave": "12345",
    }
    db.child("usuarios").push(data)
    usuarios = db.child("usuarios").get().val()
    return HttpResponse(f"Usuarios en Firebase: {usuarios}")

def lista_usuarios(request):
    usuarios_snap = db.child("usuarios").get()
    usuarios = []

    data = usuarios_snap.val() or {}
    for key, value in data.items():
        value['id'] = key   # guardamos la clave de Firebase para editar/borrar
        usuarios.append(value)

    return render(request, 'usuarios_lista.html', {'usuarios': usuarios})
def crear_usuario(request):
    if request.method == 'POST':
        data = {
            'nombre': request.POST.get('nombre'),
            'apellido': request.POST.get('apellido'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'clave': request.POST.get('clave'),
        }
        db.child('usuarios').push(data)
        return redirect('lista_usuarios')

    return render(request, 'usuario_form.html')
def editar_usuario(request, user_id):
    usuario = db.child('usuarios').child(user_id).get().val()
    if not usuario:
        return redirect('lista_usuarios')

    if request.method == 'POST':
        data = {
            'nombre': request.POST.get('nombre'),
            'apellido': request.POST.get('apellido'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'clave': request.POST.get('clave'),
        }
        db.child('usuarios').child(user_id).update(data)
        return redirect('lista_usuarios')

    usuario['id'] = user_id
    return render(request, 'usuario_form.html', {'usuario': usuario})


def eliminar_usuario(request, user_id):
    db.child('usuarios').child(user_id).remove()
    return redirect('lista_usuarios')
