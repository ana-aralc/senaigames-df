from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse ("<h1>JoeAlô senai games!</h1>")
    # request - requisição
    # template - html, entre outros
    # context - objetos (python, python com banco de dados)
    return render(request,'marketplace/index.html')