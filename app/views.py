from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from app.models import Usuario, Produto
from app.forms import formUsuario, formProduto, formLogin
# Create your views here.

def exibirUsuarios(request):
    if not request.session.get("email"):
        return redirect("app")

    usuarios = Usuario.objects.all().values()
    return render(request, "usuarios.html", {'listUsuarios': usuarios})

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def login(request):
    frmLogin = formLogin(request.POST or None)
    if request.POST:
        if frmLogin.is_valid():
            _email = frmLogin.cleaned_data.get('email')
            _senha = frmLogin.cleaned_data.get('senha')
            try:
                userLogin = Usuario.objects.get(email=_email,senha= _senha)
                if userLogin is not None:
                    request.session.set_expiry(timedelta(seconds=600))
                   
                    request.session['email'] = _email
                    tempo_sessao = timedelta(seconds=600)
                    tempo_sessao_segundos = tempo_sessao.total_seconds()
                    request.session['tempo_sessao_segundos '] =  tempo_sessao_segundos
                    return redirect("dashboard")
            except Usuario.DoesNotExist:
                return render(request, "login.html")
    return render(request, "login.html", {'form': frmLogin})


def dashboard(request):
    _email = request.session.get("email")
    tempo_sessao = request.session.get("tempo_sessao_segundos")
    if _email is None:
            return render(request, "index.html")
    if tempo_sessao and tempo_sessao > timedelta(seconds=600) :
        return render(request, "index.html")
    else:
        return render(request, "dashboard.html", {'email' : _email})

        
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
    if not request.session.get("email"):
        return redirect("app")

    if request.method == 'POST':
        formProduct = formProduto(request.POST, request.FILES)
        if formProduct.is_valid():
            formProduct.save()
            return redirect("listarProdutos")
        
    return render(request, "cadastrar-produto.html", {'form':formProduto})


def listarProdutos(request):
    if not request.session.get("email"):
        return redirect("app")

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