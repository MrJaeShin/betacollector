from django.shortcuts import redirect, render
from .models import Betta, Feeding
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bettas_index(request):
    bettas = Betta.objects.all()
    return render(request, 'bettas/index.html', {'bettas': bettas})

def bettas_detail(request, betta_id):
    betta = Betta.objects.get(id=betta_id)
    feeding_form = FeedingForm()
    return render(request, 'bettas/detail.html', { 'betta': betta, 'feeding_form': feeding_form })

def add_feeding(request, betta_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.betta_id = betta_id
        new_feeding.save()
    return redirect('detail', betta_id=betta_id)


class BettaCreate(CreateView):
    model = Betta
    fields = '__all__'

class BettaUpdate(UpdateView):
    model = Betta
    fields = ['breed', 'description', 'age']

class BettaDelete(DeleteView):
    model = Betta
    success_url = '/bettas/'

