# Generated by Django 3.1.1 on 2020-09-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0005_auto_20200911_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ano_lancamento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]