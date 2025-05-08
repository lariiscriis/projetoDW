from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from app.models import Usuario, Produto
from app.forms import formUsuario, formProduto
# Create your views here.

def exibirUsuarios(request):
    usuarios = Usuario.objects.all().values()
    return render(request, "usuarios.html", {'listUsuarios': usuarios})

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def addUsuario(request):
    formUser = formUsuario(request.POST or None)
    if request.POST:
        if formUser.is_valid():
            formUser.save()
            return redirect("exibirUsuarios")
        
    return render(request, "add-usuario.html", {'form':formUser})

def excluirUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect("exibirUsuarios")

def editarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    formUser = formUsuario(request.POST or None, instance=usuario)

    if request.POST:
        if formUser.is_valid():
            formUser.save()
            return redirect("exibirUsuarios")
        
    return render(request, "editar-usuario.html", {'form': formUser})

def cadastrarProduto(request):
    if request.method == 'POST':
        formProduct = formProduto(request.POST, request.FILES)
        if formProduct.is_valid():
            formProduct.save()
            return redirect("listarProdutos")
        
    return render(request, "cadastrar-produto.html", {'form':formProduto})


def listarProdutos(request):
    produtos = Produto.objects.all().values()
    return render(request, "listar-produtos.html", {'listProdutos': produtos})

def excluirProduto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    produto.delete()
    return redirect("listarProdutos")

def editarProduto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    formProd = formProduto(request.POST or None, instance=produto)

    if request.POST:
        if formProd.is_valid():
            formProd.save()
            return redirect("listarProdutos")
        
    return render(request, "editar-produto.html", {'form': formProd})

def cardsProdutos(request):
    produtos = Produto.objects.all().values()
    return render(request, "cards-produtos.html", {'listProdutos': produtos})