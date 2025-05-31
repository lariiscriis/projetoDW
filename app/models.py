from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField()
    senha = models.CharField(max_length = 16)
    CEP = models.CharField(max_length = 8,  null=True)
    logradouro = models.CharField(max_length = 100,  null=True)
    bairro = models.CharField(max_length = 100,  null=True)
    localidade = models.CharField(max_length = 100,  null=True)
    estado = models.CharField(max_length = 100,  null=True)
    numero_residencia = models.IntegerField(null=True)

    # def __str__(self):
    #     return f"{self.nome} ({self.email})"

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome}"

class Produto(models.Model):
    nomeProduto = models.CharField(max_length = 200)
    descricaoProduto = models.TextField()
    precoProduto = models.DecimalField(max_digits=10, decimal_places=2)
    imagemProduto = models.ImageField(upload_to='imagens/')
    qtdeEstoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    
class Venda(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cartao = models.CharField(max_length = 200)
    validade = models.CharField(max_length = 200)
    cvv = models.CharField(max_length = 200)
    data_compra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cliente.nome} comprou {self.produto.nomeProduto}"