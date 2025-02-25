# boxeo/views.py

from django.shortcuts import render
from .models import Boxeador

def buscar_boxeadores(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        boxeadores = Boxeador.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultado.html', {'boxeadores': boxeadores})
    return render(request, 'buscar.html')

def detalle_boxeador(request, boxeador_id):
    boxeador = Boxeador.objects.get(id=boxeador_id)
    return render(request, 'resultado.html', {'boxeador': boxeador})