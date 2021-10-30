from django.contrib import admin
from products.models import Wein, Braende, Spirituosen, Likoere, Sonstiges

admin.site.register(Wein)
admin.site.register(Braende)
admin.site.register(Spirituosen)
admin.site.register(Likoere)
admin.site.register(Sonstiges)

