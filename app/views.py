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