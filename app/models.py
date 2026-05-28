from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/')
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    produto_nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.produto_nome}'

class Avaliacao(models.Model):
    NOTAS = [(i, f'{i} estrela{"s" if i > 1 else ""}') for i in range(1, 6)]

    compra = models.OneToOneField(
        Compra,
        on_delete=models.CASCADE,
        related_name='avaliacao'
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='avaliacoes'
    )
    nota = models.IntegerField(
        choices=NOTAS,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.produto.nome if self.produto else "?"} ({self.nota}star)'

    @property
    def estrelas(self):
        return '★' * self.nota + '☆' * (5 - self.nota)
