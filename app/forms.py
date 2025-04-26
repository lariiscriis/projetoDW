from django import forms 
from app.models import Usuario, Produto

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
        fields = ('nomeProduto', 'descricaoProduto', 'precoProduto', 'imagemProduto', 'qtdeEstoque')

        widgets = {
            'nomeProduto' : forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'nome do produto'}),
            'descricaoProduto': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'descrição' }),
            'precoProduto': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Preço'}),
            'imagemProduto': forms.FileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'descrição' }),
            'qtdeEstoque': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Produto em estoque' })
            # erro nos fields, resolver depois
        }