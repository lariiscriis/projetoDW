from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField()
    senha = models.CharField(max_length = 16)

class Produto(models.Model):
    nomeProduto = models.CharField(max_length = 200)
    descricaoProduto = models.TextField()
    precoProduto = models.DecimalField(max_digits=10, decimal_places=2)
    imagemProduto = models.ImageField(upload_to='imagens/')
    qtdeEstoque = models.IntegerField()
    
    