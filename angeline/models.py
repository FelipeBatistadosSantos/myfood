from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.db import models
from django.utils import timezone
from localflavor.br.models import BRPostalCodeField, BRCPFField
from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('O endereço de e-mail deve ser fornecido')
        
        if not password:
            raise ValueError('A senha deve ser fornecida')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    password = models.TextField(verbose_name='password')

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class Estado(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome


class Cidade(models.Model):
    codigo_uf = models.IntegerField()
    codigo_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.nome

    
    def has_perm(self, perm, obj=None):
        return True
    
class CompleteCadastro(models.Model):

    IDIOMA_CHOICES = [
        ('nenhuma', 'Nenhum'),
        ('ingles', 'Inglês'),
        ('espanhol', 'Espanhol'),
        ('italiano', 'Italiano'),
        ('alemão', 'Alemão'),
        ('outro', 'Outro')
    ]

    RESTRICAO_CHOICES = [
        ('nenhum', 'Nenhum'),
        ('gluten', 'Glúten'),
        ('lactose', 'Lactose'),
        ('vegano', 'Vegano'),
        ('vegetariano', 'Vegetariano'),
        ('carneporco', 'Carne de porco'),
        ('diabetes', 'Diabetes'),
        ('nozes', 'Nozes'),
        ('frutosmar','Frutos do mar'),
        ('soja', 'Soja'),
        ('kosher', 'Kosher'),
        ('halal', 'Halal'),
        ('outros', 'Outros')
    ]

    CIDADE_CHOICES =[
        ('blumenau', 'Blumenau')
    ]

    ESTADO_CHOICES = [
        ('sc', 'SC')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    cep = BRPostalCodeField()
    cpf = BRCPFField()
    foto = models.ImageField('foto-perfil', upload_to='media/', blank=True, null=True)
    cidade = models.CharField('cidade', choices=CIDADE_CHOICES, default='Blumenau', max_length=20)
    estado = models.CharField('estado', choices=ESTADO_CHOICES, default='SC',  max_length=20)
    telefone = PhoneNumberField(unique=True, null=False, blank=False)
    nascimento = models.DateField(null=True)
    sobre = models.TextField('sobre', default='', max_length=359)
    profissao = models.CharField('profissao',max_length=50)
    hobbie = models.CharField('hobbie', max_length=50)
    idioma = models.CharField('idioma', choices=IDIOMA_CHOICES, max_length=30, default='Nenhum')
    comidaf = models.CharField('comida', max_length=50)
    bebida = models.CharField('bebida',max_length=50)
    restricao = models.CharField('restricao', choices=RESTRICAO_CHOICES, max_length=30, default='Nenhum')


    def is_complete(self):
        if self.foto and self.cep and self.cpf and self.cidade and self.estado and self.telefone and self.nascimento and self.profissao and self.hobbie and self.idioma and self.comidaf and self.bebida and self.restricao:
            return True
        else:
            return False

    


class Host(models.Model):
    PROFISSIONAL = 'profissional'
    AMADOR = 'amador'
    AREA_GASTRONOMIA_CHOICES = [
        (PROFISSIONAL, 'Profissional'),
        (AMADOR, 'Amante da Gastronomia'),
    ]

    FREQUENCIA_CHOICES = [
        ('diaria', 'Diariamente'),
        ('semanal', 'Semanalmente'),
        ('mensal', 'Mensalmente'),
        ('ocasional', 'Ocasionalmente'),
    ]

    foto = models.ImageField('Foto host', upload_to='media/', blank=True, null=True, max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    nome_empresa = models.CharField('Nome da Empresa/Marca/Apelido', max_length=100)
    motivo = models.TextField('Motivo para ser um host', max_length=100)
    area_gastronomia = models.CharField('Profissional da Área ou Amante da Gastronomia', max_length=20, choices=AREA_GASTRONOMIA_CHOICES, default='Amante da Gastronomia')
    servicos = models.TextField('Serviços Disponíveis')
    frequencia_servicos = models.CharField('Frequência de Disponibilização de Serviços', max_length=20, choices=FREQUENCIA_CHOICES, default='Diariamente')
    local_servico = models.CharField('Local de Serviço', max_length=100)
    descricao_local = models.TextField('Descrição do Local de Serviço')
    email_corp = models.EmailField('Email corporativo', max_length=100)

    def __str__(self):
        return self.nome_empresa

        



class Evento(models.Model):

    def default_data():
        return timezone.now().date()

    def default_horario():
        return timezone.now().time()
    
    RESTRICAO_CHOICES = [
        ('nenhum', 'Nenhum'),
        ('gluten', 'Glúten'),
        ('lactose', 'Lactose'),
        ('vegano', 'Vegano'),
        ('vegetariano', 'Vegetariano'),
        ('carneporco', 'Carne de porco'),
        ('diabetes', 'Diabetes'),
        ('nozes', 'Nozes'),
        ('frutosmar','Frutos do mar'),
        ('soja', 'Soja'),
        ('kosher', 'Kosher'),
        ('halal', 'Halal'),
        ('outros', 'Outros')
    ]

    ESTILO_CHOICES = [
            ('janta', 'Janta'),
            ('almoco', 'Almoço'),
            ('city tour gastronomico', 'City Tour Gastronômico'),
            ('harmonizacao', 'Harmonização'),
            ('workshop gastronomico', 'Workshop Gastronômico'),
            ('aula pratica', 'Aula prática de Cozinha'),
            ('outro', 'Outro'),
        ]

    id = models.AutoField(primary_key=True)
    estilo = models.CharField('Estilo de Evento', max_length=30, choices=ESTILO_CHOICES, default='')
    tema = models.CharField('Tema da experiência', max_length=255, default='Sem tema')
    fotos = models.ImageField('Fotos do Evento', upload_to='media/', blank=False, null=True, max_length=255)
    host = models.ForeignKey(Host, on_delete=models.PROTECT, default='')
    descricao = models.TextField('Descrição da experiência', max_length=518)
    cardapio = models.TextField('Cardápio', blank=True, null=True)
    inclui_bebidas = models.BooleanField('Inclui Bebidas?', default=False)
    bebidas_oferecidas = models.CharField('Bebidas Oferecidas', max_length=255, blank=True, null=True)
    convidado_pode_trazer = models.BooleanField('Convidado pode trazer bebidas?', default=False)
    max_convidados = models.PositiveIntegerField('Máximo de Convidados', default=1)
    local = models.CharField('Local', max_length=255, default='Minha casa')
    data = models.DateField('Data', default=default_data)
    horario = models.TimeField('Horário', default=default_horario)
    valor_host = models.DecimalField('Valor Host', max_digits=10, decimal_places=2, default=10.0)
    valor_manutencao_site = models.DecimalField('Valor Manutenção do Site (%)', max_digits=5, decimal_places=2, default=0)
    vagas_disponiveis = models.PositiveIntegerField('Vagas Disponíveis', editable=False, default=0)
    restricao = models.CharField('restricao', choices=RESTRICAO_CHOICES, max_length=30, default='Nenhum')


    def save(self, *args, **kwargs):
        if self.pk is None:
            self.vagas_disponiveis = self.max_convidados
        super().save(*args, **kwargs)

    def valor_total_evento(self):
        return self.valor_host + (self.valor_host * (self.valor_manutencao_site / 100))

    def __str__(self):
        return f'{self.estilo} - {self.tema} por {self.host.username} em {self.local} em {self.data} às {self.horario}'
        

class Reserva(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    quantidade_pessoas = models.PositiveIntegerField(default=1)
    nomes_pessoas = models.CharField(max_length=255)
    data_agendamento = models.DateTimeField(auto_now_add=True)
