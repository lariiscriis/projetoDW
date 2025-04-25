from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name = "app"),
    path('usuarios', views.exibirUsuarios , name = "exibirUsuarios"),
    path('add-usuario', views.addUsuario, name="addUsuario"),
    path('excluir-usuario/<int:id_usuario>', views.excluirUsuario, name="excluirUsuario" ),
    path('editar-usuario/<int:id_usuario>', views.editarUsuario, name="editarUsuario")
]
