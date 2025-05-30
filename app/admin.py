from django.contrib import admin
from .models import Usuario, Produto, Categoria
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")

admin.site.register(Usuario, UsuarioAdmin)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nomeProduto', 'descricaoProduto', 'precoProduto', 'imagemProduto', 'qtdeEstoque', 'categoria')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)