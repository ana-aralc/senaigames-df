from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Membro
from marketplace.models import Genero

# Create your views here.
def index(request):
    # return HttpResponse ("<h1>JoeAlô senai games!</h1>")
    # request - requisição
    # template - html, entre outros
    # context - objetos (python, python com banco de dados)
    return render(request,'marketplace/index.html')

def autentica_membro(request):
    """
    dados = {
        1:{"nome":"Visual Novel"},
        2:{"nome":"Plataforma"},
        3:{"nome":"Acao"},
        4:{"nome":"Acao"},
    }
    """
    dados = Membro.objects.all()
    generos = Genero.objects.all()
    return render(request,'marketplace/sou_membro.html', {'cards':dados, 'generos':generos})






