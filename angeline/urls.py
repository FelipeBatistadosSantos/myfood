from django.urls import path
from django.contrib.auth.views import LoginView
from .views import cadastro, CustomLoginView, home, host, perfil, CustomLogoutView, editar_perfil, filtrar_cidades_view

app_name = 'angeline'

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('home', home, name='home'),
    path('seja host', host, name='host'),
    path('perfil', perfil, name='perfil'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('filtrar-cidades/', filtrar_cidades_view, name='filtrar_cidades'),
    
]