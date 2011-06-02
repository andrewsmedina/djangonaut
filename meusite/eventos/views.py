from django.shortcuts import render_to_response
from eventos.forms import EventoForm

def hello(request):
    context = {
        'form': EventoForm()
    }
    return render_to_response('hello.html', context)
