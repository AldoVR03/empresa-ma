from django.shortcuts import render, redirect
from .forms import ClienteForm

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ClienteForm 
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import LoginForm  # Asegúrate de importar el formulario adecuado desde tu aplicación


@login_required  # Esto asegura que solo usuarios autenticados pueden acceder a esta vista
def ver_cotizacion(request):
    # Lógica para mostrar la página de ver_cotizacion.html
    # Puedes agregar cualquier lógica adicional aquí según tus necesidades
    return render(request, 'ver_cotizacion.html')



def login_view(request):
    if request.method == 'POST':
        print("hola-test")
        form = LoginForm(request, data=request.POST)
        print("hola2")
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            print("hola3")
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')

            # Redirigir a la vista de ver_cotizacion en caso de inicio de sesión exitoso
            return redirect('ver_cotizacion')
        else:
            messages.error(request, 'Error al iniciar sesión. Verifique sus credenciales.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

    
def registro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
    else:
        form = ClienteForm()

    return render(request, 'registro.html', {'form': form})

def cotizacion(request):
    return render(request, 'cotizacion.html')

def empleados(request):
    return render(request, 'empleados.html')

def inventario(request):
    return render(request, 'inventario.html')

def ver_cotizacion(request):
    return render(request, 'ver_cotizacion.html')