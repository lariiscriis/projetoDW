from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name = "app"),
    path('usuarios', views.exibirUsuarios , name = "exibirUsuarios"),
    path('add-usuario', views.addUsuario, name="addUsuario")
    
]
