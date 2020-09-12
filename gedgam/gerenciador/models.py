from django.db import models


class Game(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(blank=True, null=True)
    produtora = models.CharField(max_length=50, blank=True, null=True)
    PLATAFORMA = (
        ('--', '--'),
        ('PC', 'PC'),
        ('Xbox One', 'Xbox One'),
        ('Play Station 4', 'Play Station 4'),
        ('Nintendo Switch', 'Nintendo Switch'),
        ('Outra', 'Outra')
    )
    plataforma = models.CharField(
        max_length=20, choices=PLATAFORMA, default='--')
    ZERADO = (
        ('--', '--'),
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não se aplica', 'Não se aplica'),
    )
    zerado = models.CharField(max_length=20, choices=ZERADO, default='--')
    data_zeramento = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to="images/")
