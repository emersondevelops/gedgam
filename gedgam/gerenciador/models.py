from django.db import models


class Game(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(blank=True, null=True)
    produtora = models.CharField(max_length=50, blank=True, null=True)
    PLATAFORMA = (
        ('PC', 'PC'),
        ('XB', 'Xbox One'),
        ('PS', 'Play Station 4'),
        ('NS', 'Nintendo Switch')
    )
    plataforma = models.CharField(max_length=20, choices=PLATAFORMA)
    ZERADO = (
        ('S', 'Sim'),
        ('N', 'Não'),
        ('O', 'Não se aplica'),
    )
    zerado = models.CharField(max_length=1, choices=ZERADO)
    data_zeramento = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
