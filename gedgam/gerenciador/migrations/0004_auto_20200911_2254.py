# Generated by Django 3.1.1 on 2020-09-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0003_auto_20200911_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ano_lancamento',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='comentarios',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='data_zeramento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='produtora',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
