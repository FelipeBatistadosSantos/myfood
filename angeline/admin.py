from django.contrib import admin
from .models import CustomUser, Host, Cidade, Estado, Evento

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Host)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Evento)