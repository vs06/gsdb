from django import forms
from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Campi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='nome')
    address = models.CharField(max_length=200, verbose_name='endereco')
    capacity = models.IntegerField(verbose_name='capacidade')
    
    def __str__(self):
        return self.name

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='nome')
    tune = models.CharField(max_length=10, verbose_name='tom')
    band = models.CharField(max_length=100, verbose_name='artista')
    lyrics = models.CharField(max_length=255, verbose_name='letra')
    link = models.URLField(max_length=255, verbose_name='link')
    obs = models.TextField(verbose_name='obs')
    datashow = models.CharField(max_length=1, verbose_name='datashow') 
    
    def __str__(self):
        return self.name

class Culto(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True, verbose_name='data')
    campi = models.ForeignKey(Campi, db_column='campi', blank=True, null=True, verbose_name='local',default=1)
    musicas = models.ManyToManyField(Musica)

    def __str__(self):
        return self.date.__str__()