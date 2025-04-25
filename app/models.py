from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField()
    senha = models.CharField(max_length = 16)

class Produto(models.Model):
    nomeProduto = models.CharField(max_length = 100)
    descricaoProduto = models.CharField(max_length = 200)
    precoProduto = models.DecimalField(max_value = 200)
    imagemProduto = models.ImageField(upload_to='imagens/')
    qtdeEstoque = models.IntegerField(max_value = 200)
    
    