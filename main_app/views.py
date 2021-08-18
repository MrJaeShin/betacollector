from django.shortcuts import render

class Betta:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

bettas=[
    Betta('Rainbow', 'double tail', 'colorful angel', 1)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bettas_index(request):
    return render(request, 'bettas/index.html', {'bettas': bettas})

