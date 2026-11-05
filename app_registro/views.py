from django.shortcuts import render, redirect
from .forms import CompetidorForm
from .models import Competidor

def inicio(request):
    return render(request, 'app_registro/inicio.html')


def registro(request):

    if request.method == 'POST':
        form = CompetidorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('competidores')

    else:
        form = CompetidorForm()

    return render(request, 'app_registro/registro.html', {
        'form': form
    })


def competidores(request):
    lista_competidores = Competidor.objects.all()

    return render(request, 'app_registro/competidores.html', {
        'competidores': lista_competidores
    })