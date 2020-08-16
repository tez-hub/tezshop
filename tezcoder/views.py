from django.shortcuts import render
from .models import Clothes, Shoes, Watch, Cap

# Create your views here.

def index(request):
    clothes = Clothes.objects.all()
    shoes = Shoes.objects.all()
    watch = Watch.objects.all()
    cap = Cap.objects.all()
    
    return render(request, 'tezcoder/index.html', {'clothes': clothes, 'shoes': shoes, 'watch': watch, 'cap': cap})



    

def cart(request):
    return render(request, 'tezcoder/cart.html')