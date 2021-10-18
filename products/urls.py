from django.urls import include, path

from . import views
from products.views import wein

urlpatterns = [
        path('', views.products, name='products'),
        path('wein/', views.wein, name='wein'),

        path('braende/', views.braende, name='braende'),
        path('spirituosen/', views.spirituosen, name='spirituosen'),
        path('likoere/', views.likoere, name='likoere'),
        path('sonstiges/', views.sonstiges, name='sonstiges'),
]
