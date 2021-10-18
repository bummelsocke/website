from django.shortcuts import render
from .models import Wein

def products(request):
    return render(request, 'products/products.html')

def wein(request):
    queryset = Wein.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/wein.html', context)

def braende(request):
    return render(request, 'products/braende.html')

def spirituosen(request):
    return render(request, 'products/spirituosen.html')

def likoere(request):
    return render(request, 'products/likoere.html')

def sonstiges(request):
    return render(request, 'products/sonstiges.html')
