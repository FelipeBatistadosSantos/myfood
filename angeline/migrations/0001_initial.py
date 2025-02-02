# Generated by Django 5.0.1 on 2024-03-02 16:35

import angeline.models
import django.db.models.deletion
import localflavor.br.models
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password', models.TextField(verbose_name='password')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CompleteCadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9)),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='foto-perfil')),
                ('cidade', models.CharField(choices=[('blumenau', 'Blumenau')], default='Blumenau', max_length=20, verbose_name='cidade')),
                ('estado', models.CharField(choices=[('sc', 'SC')], default='SC', max_length=20, verbose_name='estado')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('nascimento', models.DateField(null=True)),
                ('sobre', models.TextField(default='', max_length=359, verbose_name='sobre')),
                ('profissao', models.CharField(max_length=50, verbose_name='profissao')),
                ('hobbie', models.CharField(max_length=50, verbose_name='hobbie')),
                ('idioma', models.CharField(choices=[('nenhuma', 'Nenhum'), ('ingles', 'Inglês'), ('espanhol', 'Espanhol'), ('italiano', 'Italiano'), ('alemão', 'Alemão'), ('outro', 'Outro')], default='Nenhum', max_length=30, verbose_name='idioma')),
                ('comidaf', models.CharField(max_length=50, verbose_name='comida')),
                ('bebida', models.CharField(max_length=50, verbose_name='bebida')),
                ('restricao', models.CharField(choices=[('nenhum', 'Nenhum'), ('gluten', 'Glúten'), ('lactose', 'Lactose'), ('vegano', 'Vegano'), ('vegetariano', 'Vegetariano'), ('carneporco', 'Carne de porco'), ('diabetes', 'Diabetes'), ('nozes', 'Nozes'), ('frutosmar', 'Frutos do mar'), ('soja', 'Soja'), ('kosher', 'Kosher'), ('halal', 'Halal'), ('outros', 'Outros')], default='Nenhum', max_length=30, verbose_name='restricao')),
                ('usuario', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('codigo_uf', models.IntegerField()),
                ('codigo_ibge', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='angeline.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, max_length=255, null=True, upload_to='media/', verbose_name='Foto host')),
                ('nome_empresa', models.CharField(max_length=100, verbose_name='Nome da Empresa/Marca/Apelido')),
                ('motivo', models.TextField(max_length=100, verbose_name='Motivo para ser um host')),
                ('area_gastronomia', models.CharField(choices=[('profissional', 'Profissional'), ('amador', 'Amante da Gastronomia')], default='Amante da Gastronomia', max_length=20, verbose_name='Profissional da Área ou Amante da Gastronomia')),
                ('servicos', models.TextField(verbose_name='Serviços Disponíveis')),
                ('frequencia_servicos', models.CharField(choices=[('diaria', 'Diariamente'), ('semanal', 'Semanalmente'), ('mensal', 'Mensalmente'), ('ocasional', 'Ocasionalmente')], default='Diariamente', max_length=20, verbose_name='Frequência de Disponibilização de Serviços')),
                ('local_servico', models.CharField(max_length=100, verbose_name='Local de Serviço')),
                ('descricao_local', models.TextField(verbose_name='Descrição do Local de Serviço')),
                ('email_corp', models.EmailField(max_length=100, verbose_name='Email corporativo')),
                ('usuario', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estilo', models.CharField(choices=[('janta', 'Janta'), ('almoco', 'Almoço'), ('city tour gastronomico', 'City Tour Gastronômico'), ('harmonizacao', 'Harmonização'), ('workshop gastronomico', 'Workshop Gastronômico'), ('aula pratica', 'Aula prática de Cozinha'), ('outro', 'Outro')], default='', max_length=30, verbose_name='Estilo de Evento')),
                ('tema', models.CharField(default='Sem tema', max_length=255, verbose_name='Tema da experiência')),
                ('fotos', models.ImageField(max_length=255, null=True, upload_to='media/', verbose_name='Fotos do Evento')),
                ('descricao', models.TextField(max_length=518, verbose_name='Descrição da experiência')),
                ('cardapio', models.TextField(blank=True, null=True, verbose_name='Cardápio')),
                ('inclui_bebidas', models.BooleanField(default=False, verbose_name='Inclui Bebidas?')),
                ('bebidas_oferecidas', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bebidas Oferecidas')),
                ('convidado_pode_trazer', models.BooleanField(default=False, verbose_name='Convidado pode trazer bebidas?')),
                ('max_convidados', models.PositiveIntegerField(default=1, verbose_name='Máximo de Convidados')),
                ('local', models.CharField(default='Minha casa', max_length=255, verbose_name='Local')),
                ('data', models.DateField(default=angeline.models.Evento.default_data, verbose_name='Data')),
                ('horario', models.TimeField(default=angeline.models.Evento.default_horario, verbose_name='Horário')),
                ('valor_host', models.DecimalField(decimal_places=2, default=10.0, max_digits=10, verbose_name='Valor Host')),
                ('valor_manutencao_site', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Valor Manutenção do Site (%)')),
                ('vagas_disponiveis', models.PositiveIntegerField(default=0, editable=False, verbose_name='Vagas Disponíveis')),
                ('restricao', models.CharField(choices=[('nenhum', 'Nenhum'), ('gluten', 'Glúten'), ('lactose', 'Lactose'), ('vegano', 'Vegano'), ('vegetariano', 'Vegetariano'), ('carneporco', 'Carne de porco'), ('diabetes', 'Diabetes'), ('nozes', 'Nozes'), ('frutosmar', 'Frutos do mar'), ('soja', 'Soja'), ('kosher', 'Kosher'), ('halal', 'Halal'), ('outros', 'Outros')], default='Nenhum', max_length=30, verbose_name='restricao')),
                ('host', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='angeline.host')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_pessoas', models.PositiveIntegerField(default=1)),
                ('nomes_pessoas', models.CharField(max_length=255)),
                ('data_agendamento', models.DateTimeField(auto_now_add=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angeline.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
