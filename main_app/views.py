from django.shortcuts import render
from .models import Betta
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class BettaCreate(CreateView):
    model = Betta
    fields = '__all__'

class BettaUpdate(UpdateView):
    model = Betta
    fields = ['breed', 'description', 'age']

class BettaDelete(DeleteView):
    model = Betta
    success_url = '/bettas/'