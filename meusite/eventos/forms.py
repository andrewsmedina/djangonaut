from django import forms
from eventos.models import Evento

class FaleConoscoForm(forms.Form):
    mensagem = forms.CharField()
    email = forms.EmailField()

class EventoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Evento
