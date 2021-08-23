from django.shortcuts import redirect, render
from .models import Betta
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from .models import Betta, Toy
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BettaCreate(CreateView):
    model = Betta
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BettaUpdate(LoginRequiredMixin, UpdateView):
    model = Betta
    fields = ['breed', 'description', 'age']

class BettaDelete(LoginRequiredMixin, DeleteView):
    model = Betta
    success_url = '/bettas/'

@login_required
def bettas_index(request):
    bettas = Betta.objects.filter(user = request.user)
    return render(request, 'bettas/index.html', {'bettas': bettas})

@login_required
def bettas_detail(request, betta_id):
    betta = Betta.objects.get(id=betta_id)
    toys_betta_doesnt_have = Toy.objects.exclude(id__in = betta.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'bettas/detail.html', { 
        'betta': betta, 
        'feeding_form': feeding_form,
        'toys': toys_betta_doesnt_have
        })

@login_required
def add_feeding(request, betta_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.betta_id = betta_id
        new_feeding.save()
    return redirect('detail', betta_id=betta_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, betta_id, toy_id):
  Betta.objects.get(id=betta_id).toys.add(toy_id)
  return redirect('detail', betta_id=betta_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  