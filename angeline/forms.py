from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, CompleteCadastro




class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Remover mensagens de validação padrão
        for field in self.fields.values():
            field.widget.attrs.pop("title", None)
            field.help_text = None

        # Adicionar placeholders se desejar
        self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
        self.fields['email'].widget.attrs['placeholder'] = 'Endereço de email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmação de senha'
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não coincidem.')

        return confirmar_senha


class ProdutoFilterForm(forms.Form):
    cidade = forms.CharField(required=False)

    
class CompleteCadastroForm(forms.ModelForm):
    class Meta:
        model = CompleteCadastro
        fields = ['nascimento','sobre','profissao','hobbie','idioma','comidaf','bebida','restricao', 'cpf','cep','cidade','estado','telefone']
