from django import forms
from app.models import Categoria, Contato, Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  

class FormUsuario(UserCreationForm):
    error_messages = {
        'password_mismatch': 'As duas senhas não conferem.',
    }

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmar senha',
        }
        error_messages = {
            'username': {
                'unique': 'Já existe um usuário com esse nome. Escolha outro nome ou entre com a conta existente.',
                'required': 'Informe um nome de usuário.',
            },
            'email': {
                'invalid': 'Informe um e-mail válido.',
            },
        }

class FormEditarUsuario(forms.ModelForm): 
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Nome',
            'email': 'E-mail'
        }

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem', 'quantidade', 'preco', 'categoria']
