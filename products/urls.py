from django.urls import include, path
from . import views
from products.views import wein, wein_detail, braende, braende_detail, spirituosen, spirituosen_detail, likoere, likoere_detail, sonstiges, sonstiges_detail

urlpatterns = [
        path('', views.products, name='products'),
        path('wein/', views.wein.as_view(), name='wein'),
        path('wein/<int:pk>', views.wein_detail.as_view(), name='wein_detail'),
        path('braende/', views.braende.as_view(), name='braende'),
        path('braende/<int:pk>', views.braende_detail.as_view(), name='braende_detail'),
        path('spirituosen/', views.spirituosen.as_view(), name='spirituosen'),
        path('spirituosen/<int:pk>', views.spirituosen_detail.as_view(), name='spirituosen_detail'),
        path('likoere/', views.likoere.as_view(), name='likoere'),
        path('likoere/<int:pk>', views.likoere_detail.as_view(), name='likoere_detail'),
        path('sonstiges/', views.sonstiges.as_view(), name='sonstiges'),
        path('sonstiges/<int:pk>', views.sonstiges_detail.as_view(), name='sonstiges_detail'),
]
