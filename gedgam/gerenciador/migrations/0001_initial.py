# Generated by Django 3.1.1 on 2020-09-12 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano_lancamento', models.IntegerField()),
                ('produtora', models.CharField(max_length=50)),
                ('plataforma', models.CharField(choices=[('PC', 'PC'), ('XB', 'Xbox One'), ('PS', 'Play Station 4'), ('NS', 'Nintendo Switch')], max_length=20)),
                ('zerado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('O', 'Não se aplica')], max_length=1)),
                ('data_zeramento', models.DateField(null=True)),
                ('comentarios', models.TextField()),
            ],
        ),
    ]
