from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from app.models import Usuario
from app.forms import formUsuario
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


