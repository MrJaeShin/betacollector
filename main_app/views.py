from django.shortcuts import render
from .models import Betta

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bettas_index(request):
    bettas = Betta.objects.all()
    return render(request, 'bettas/index.html', {'bettas': bettas})

def bettas_detail(request, betta_id):
    betta = Betta.objects.get(id=betta_id)
    return render(request, 'bettas/detail.html', {'betta': betta})