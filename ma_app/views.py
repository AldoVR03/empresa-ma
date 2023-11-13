from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def cotizacion(request):
    return render(request, 'cotizacion.html')

def empleados(request):
    return render(request, 'empleados.html')

def inventario(request):
    return render(request, 'inventario.html')

def ver_cotizacion(request):
    return render(request, 'ver_cotizacion.html')