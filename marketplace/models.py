from django.db import models

# Create your models here.
# Aqui eu vou programar o modelo
# Classes mapeadas com tabelas
# Persistência? - guardar daddos no banco de dados
# Orientação a objetos
# Classes ===> Tabelas
# localhost:8000/admin
# github
# https://github.com/romulodf-cesar/barbersites/tree/master/crm

# herança
class Membro(models.Model):
    email = models.CharField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    id = models.CharField(max_length=10, primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.nome