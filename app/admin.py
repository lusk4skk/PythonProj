from django.contrib import admin
from app.models import Categoria, Produto, Compra, Avaliacao

# Register your models here.
admin.site.register(Categoria)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade", "preco", "categoria", "imagem")
    search_fields = ("nome",)
    list_filter = ("categoria", "preco")


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "produto_nome", "quantidade", "valor_total", "data")
    search_fields = ("usuario__username", "produto_nome")
    list_filter = ("data",)


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "produto", "nota", "data")
    search_fields = ("usuario__username", "produto__nome")
    list_filter = ("nota", "data")
    readonly_fields = ("data",)
