from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Topico(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class Room(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)
    adm = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    participantes = models.ManyToManyField(User, related_name='participantes', blank=True )
    criada = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-criada',]

    def __str__(self):
        return self.nome
    

class Mensagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    texto = models.TextField()
    enviada = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-enviada',]

    def __str__(self):
        return self.texto[0:20]




