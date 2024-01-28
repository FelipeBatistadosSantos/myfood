from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from .models import CustomUser, CompleteCadastro
from .forms import CustomUserCreationForm, CustomUserLoginForm, CompleteCadastroForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .utils import filtrar_cidades
from django.db import models
from .models import Cidade


def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cadastro realizado com sucesso. Faça o login.')
            return redirect('angeline:login')
        else:
            messages.error(request, 'Erro no cadastro. Por favor, corrija os erros abaixo.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register/cadastro.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'register/login.html'
    authentication_form = CustomUserLoginForm


class CustomLogoutView(LogoutView):
    next_page = 'main:base'



def home(request):
    return render(request, 'angeline/home.html')


def host(request):
    return render(request, 'angeline/host.html')





@login_required
def perfil(request):
    perfil_usuario, created = CompleteCadastro.objects.get_or_create(usuario=request.user)

    if 'edit' in request.GET:
        return redirect('angeline:editar_perfil')

    if request.method == 'POST':
        form = CompleteCadastroForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            
            if created:
                return redirect('angeline:perfil')
    else:
        form = CompleteCadastroForm(instance=perfil_usuario)

    return render(request, 'angeline/perfil.html', {'form': form, 'perfil_usuario': perfil_usuario, 'form_preenchido': not created})


@login_required
def editar_perfil(request):
    perfil_usuario, created = CompleteCadastro.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = CompleteCadastroForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            return redirect('angeline:perfil')  
    else:
        form = CompleteCadastroForm(instance=perfil_usuario)

    return render(request, 'angeline/editar_perfil.html', {'form': form, 'perfil_usuario': perfil_usuario})



def testeFeed(request):
    lista = {'nome':'Jardinagem', }

    return render(request, 'angeline/home.html')


def filtrar_cidades_view(request):
    if request.method == 'POST':
        filtro = request.POST.get('filtro')
        if len(filtro) > 2:
            resultados = Cidade.objects.filter(
                models.Q(nome__icontains=filtro) |
                models.Q(evento__icontains=filtro) |
                models.Q(nacionalidade__icontains=filtro)
            )
            return render(request, 'angeline/resultado.html', {'resultados': resultados, 'filtro': filtro})
        else:
            return render(request, 'angeline/resultado.html', {'resultados': [], 'filtro': filtro})

    return render(request, 'angeline/filtrar_cidades.html')
