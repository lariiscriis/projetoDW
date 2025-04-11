from django import forms 
from app.models import Usuario

class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')
        
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'nome'}),
            'email': forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder': 'email'}),
            'senha': forms.TextInput(attrs={'class': 'form-control mb-3', 'type': 'password', 'placeholder': 'senha'}),

        }