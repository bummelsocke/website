from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Wein

def products(request):
    return render(request, 'products/products.html')

class wein(ListView):
    paginate_by = 12
    model = Wein
    queryset = Wein.objects.all()
    template_name = 'products/wein.html'

class wein_detail(DetailView):
    model = Wein
    context_object_name = 'object'
    template_name = 'products/weindetail.html'

def braende(request):
    return render(request, 'products/braende.html')

def spirituosen(request):
    return render(request, 'products/spirituosen.html')

def likoere(request):
    return render(request, 'products/likoere.html')

def sonstiges(request):
    return render(request, 'products/sonstiges.html')

