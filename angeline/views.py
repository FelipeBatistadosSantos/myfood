from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from .models import CustomUser, CompleteCadastro,Host, Evento
from .forms import CustomUserCreationForm, CustomUserLoginForm, CompleteCadastroForm, HostForm, EventoForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .utils import filtrar_cidades
from django.db import models
from .models import Cidades
import json
from django.views import View


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
    perfil_usuario, created = CompleteCadastro.objects.get_or_create(usuario=request.user)

    eventos = Evento.objects.all()

    return render(request, 'angeline/home.html', {'eventos': eventos, 'perfil_usuario':perfil_usuario,'form_preenchido': not created})


@login_required
def host(request):
    user = request.user

    if Host.objects.filter(usuario=user).exists():
        return redirect('angeline:perfil_host')
    else:
        return redirect('angeline:editar_host')
    

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


@login_required
def evento(request):
    perfil_usuario, created = CompleteCadastro.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.host = request.user
            evento.save()
            return redirect('angeline:home') 
    else:
        form = EventoForm()

    eventos = Evento.objects.all()

    return render(request, 'angeline/evento.html', {'form': form, 'perfil_usuario': perfil_usuario, 'eventos':eventos})




def specific_page(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    context = {
        'evento': evento,
    }

    return render(request, 'angeline/specific_page.html', context)



@login_required
def editar_host(request):
    host, created = Host.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()

            request.session['host_nome_empresa'] = host.nome_empresa
            request.session['host_motivo'] = host.motivo
            request.session['host_get_area_gastronomia_display'] = host.area_gastronomia
            request.session['host_servicos'] = host.servicos
            request.session['host_get_frequencia_servicos_display'] = host.frequencia_servicos
            request.session['host_local_servico'] = host.local_servico
            request.session['host_descricao_local'] = host.descricao_local

            messages.success(request, 'Informações do host atualizadas com sucesso!')
            return render(request, 'angeline/host.html', {'form': form, 'host': host, 'form_preenchido': not created})
    else:
        form = HostForm(instance=host)
    return render(request, 'angeline/editar_host.html', {'form': form, 'host': host, 'form_preenchido': not created})

@login_required
def perfil_host(request):
    host, created = Host.objects.get_or_create(usuario=request.user)

    if 'edit' in request.GET:
        return redirect('angeline:editar_host')

    if request.method == 'POST':
        form = HostForm(request.POST, request.FILES, instance=host)
        if form.is_valid():
            form.save()

            if created:
                return redirect('angeline:perfil_host')
    else:
        form = HostForm(instance=host)

    return render(request, 'angeline/host.html', {'form': form, 'host': host, 'form_preenchido': not created})


def host_servico(request):
    hoster = Host.objects.get()
    
    context = {
        'host' : hoster
    }
    
    return render(request, 'angeline/host_servico.html', context)
    

def agendamento(request):
    return render(request, 'angeline/agendamento.html')


def editar_evento(request):
    return render(request, 'angeline/editar_evento.html')

    return render(request, 'angeline/home.html')


def filtrar_cidades_view(request):
    if request.method == 'POST':
        filtro = request.POST.get('filtro')
        if len(filtro) > 2:
            resultados = Cidades.objects.filter(
                models.Q(nome__icontains=filtro) |
                models.Q(evento__icontains=filtro) |
                models.Q(nacionalidade__icontains=filtro)
            )
            print(resultados)
            return render(request, 'angeline/resultado.html', {'resultados': resultados, 'filtro': filtro})
        else:
            return render(request, 'angeline/resultado.html', {'resultados': [], 'filtro': filtro})

    return render(request, 'angeline/filtrar_cidades.html')
