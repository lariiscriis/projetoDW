from django import forms 
from app.models import Usuario
from app.models import Produto

class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')
        
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'nome'}),
            'email': forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder': 'email'}),
            'senha': forms.TextInput(attrs={'class': 'form-control mb-3', 'type': 'password', 'placeholder': 'senha'}),

        }

class formProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nomeProduto', 'descricaoProduto', 'precoProduto', 'imagemProduto', 'qtdeProduto')

        widgets = {
            'nomeProduto' : forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'nome do produto'}),
            'descricaoProduto': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'descrição' }),
            'precoProduto': forms.DecimalField(attrs={'class': 'form-control mb-3', 'placeholder': 'preço',  'max_value': '100', 'min_value':'0' }),
            'imagemProduto': forms.ImageField(attrs={'class': 'form-control mb-3', 'placeholder': 'descrição' }),
            'qtdeProduto': forms.IntegerField(attrs={'class': 'form-control mb-3', 'placeholder': 'Produto em estoque' })
            # erro nos fields, resolver depois
        }