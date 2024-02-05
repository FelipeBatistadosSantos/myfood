# Generated by Django 5.0.1 on 2024-02-05 17:09

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
            name='Cidade',
            fields=[
                ('codigo_uf', models.IntegerField()),
                ('codigo_ibge', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('evento', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=100)),
                ('outra_restricao', models.CharField(default='', max_length=30, verbose_name='outra_restricao')),
            ],
        ),
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
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('nascimento', models.DateField(null=True)),
                ('sobre', models.TextField(default='', verbose_name='sobre')),
                ('profissao', models.CharField(max_length=50, verbose_name='profissao')),
                ('hobbie', models.CharField(max_length=50, verbose_name='hobbie')),
                ('idioma', models.CharField(choices=[('nenhuma', 'Nenhum'), ('ingles', 'Inglês'), ('espanhol', 'Espanhol'), ('italiano', 'Italiano'), ('alemão', 'Alemão'), ('outro', 'Outro')], max_length=30, verbose_name='idioma')),
                ('comidaf', models.CharField(max_length=50, verbose_name='comida')),
                ('bebida', models.CharField(max_length=50, verbose_name='bebida')),
                ('restricao', models.CharField(choices=[('nenhum', 'Nenhum'), ('gluten', 'Glúten'), ('lactose', 'Lactose'), ('vegano', 'Vegano'), ('vegetariano', 'Vegetariano'), ('outros', 'Outros')], max_length=30, verbose_name='restricao')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='angeline.cidade')),
                ('usuario', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='angeline.estado')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='angeline.estado'),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estilo', models.CharField(choices=[('janta', 'Janta'), ('almoco', 'Almoço'), ('city_tour_gastronomico', 'City Tour Gastronômico'), ('harmonizacao', 'Harmonização'), ('workshop_gastronomico', 'Workshop Gastronômico'), ('aula_pratica', 'Aula prática de Cozinha'), ('outro', 'Outro')], default='', max_length=30, verbose_name='Estilo de Evento')),
                ('tema', models.CharField(default='Sem tema', max_length=255, verbose_name='Tema da experiência')),
                ('fotos', models.ImageField(blank=True, max_length=255, null=True, upload_to='evento_fotos/', verbose_name='Fotos do Evento')),
                ('descricao', models.TextField(verbose_name='Descrição da experiência')),
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
                ('host', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100, verbose_name='Nome da Empresa/Marca/Apelido')),
                ('motivo', models.TextField(verbose_name='Motivo para ser um host')),
                ('area_gastronomia', models.CharField(choices=[('profissional', 'Profissional'), ('amador', 'Amante da Gastronomia')], max_length=20, verbose_name='Profissional da Área ou Amante da Gastronomia')),
                ('servicos', models.TextField(verbose_name='Serviços Disponíveis')),
                ('frequencia_servicos', models.CharField(choices=[('diaria', 'Diariamente'), ('semanal', 'Semanalmente'), ('mensal', 'Mensalmente'), ('ocasional', 'Ocasionalmente')], max_length=20, verbose_name='Frequência de Disponibilização de Serviços')),
                ('local_servico', models.CharField(max_length=100, verbose_name='Local de Serviço')),
                ('descricao_local', models.TextField(verbose_name='Descrição do Local de Serviço')),
                ('usuario', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
