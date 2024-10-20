from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import AnimalForm, AyudaForm
from django.shortcuts import get_object_or_404, redirect
from .models import Animal
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    animales = Animal.objects.all()
    if request.method == 'POST':
        if 'formAnimal' in request.POST:
            form_animal = AnimalForm(request.POST)
            if form_animal.is_valid():
                form_animal.save()
                return redirect('dashboard')
        elif 'formAyuda' in request.POST:
            form_ayuda = AyudaForm(request.POST)
            if form_ayuda.is_valid():
                form_ayuda.save()
                return redirect('dashboard')
    else:
        form_animal = AnimalForm()
        form_ayuda = AyudaForm()

    return render(request, 'dashboard.html', {
        'animales': animales,
        'form_animal': form_animal,
        'form_ayuda': form_ayuda
    })
    

def eliminarAnimal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    animal.delete()
    return redirect('dashboard')

##iniciar sesion
def iniciarSesion(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')  # Utiliza get() para evitar errores
        constrasena = request.POST.get('contrasena')
        user = authenticate(username=usuario, password=constrasena)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'index.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'index.html', {'error': 'Credenciales inválidas'})


##cerrar sesion
def CerrarSesion(request):
    logout(request)
    return redirect('index') 