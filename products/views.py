from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Wein, Braende, Spirituosen, Likoere, Sonstiges

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

class braende(ListView):
    paginate_by = 12;
    model = Braende
    queryset = Braende.objects.all()
    template_name = 'products/braende.html'

class braende_detail(DetailView):
    model = Braende
    context_object_name = 'object'
    template_name = 'products/braendedetail.html'

class spirituosen(ListView):
    paginate_by = 12;
    model = Spirituosen
    queryset = Spirituosen.objects.all()
    template_name = 'products/spirituosen.html'

class spirituosen_detail(DetailView):
    model = Spirituosen
    context_object_name = 'object'
    template_name = 'products/spirituosendetail.html'

class likoere(ListView):
    paginate_by = 12;
    model = Likoere
    queryset = Likoere.objects.all()
    template_name = 'products/likoere.html'

class likoere_detail(DetailView):
    model = Likoere
    context_object_name = 'object'
    template_name = 'products/likoeredetail.html'

class sonstiges(ListView):
    paginate_by = 12;
    model = Sonstiges
    queryset = Sonstiges.objects.all()
    template_name = 'products/sonstiges.html'

class sonstiges_detail(DetailView):
    model = Sonstiges
    context_object_name = 'object'
    template_name = 'products/sonstigesdetail.html'




