from datetime import datetime
from django.db import models
from usuarios.models import Usuario

class Produto(models.Model):
    CATEGORIAS  = [
        ('eletronicos', 'Eletrônicos'),
        ('televisao', 'Televisão'),
        ('computador', 'Computador'),
        ('celular', 'Celular'),
        ('audio_video', 'Áudio e Vídeo'),
    ]

    name = models.CharField(verbose_name='nome do produto', max_length=200)
    email = models.CharField(verbose_name='email', max_length=200)
    price = models.IntegerField()
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    description = models.TextField(default='Sem Descrição')
    data_produto = models.DateTimeField(default=datetime.now)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    categoria = models.CharField(
        verbose_name='categoria',
        max_length=100,
        choices=CATEGORIAS,
        default='eletronicos'
    )