# Generated by Django 3.1.1 on 2020-09-05 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ibge', models.IntegerField()),
                ('ibge7', models.IntegerField()),
                ('uf', models.CharField(max_length=2)),
                ('municipio', models.CharField(max_length=128)),
                ('regiao', models.CharField(max_length=15)),
                ('populacao_2010', models.IntegerField(null=True)),
                ('capital', models.BooleanField()),
                ('validacao', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mapeamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Público'), (2, 'Não público'), (3, 'Sem confirmação')])),
                ('data_inicial', models.DateField()),
                ('link_do', models.URLField()),
                ('tipo_arquivo', models.IntegerField(choices=[(1, 'PDF Texto'), (2, 'PDF imagem'), (3, 'DOCX'), (4, 'HTML'), (5, 'TXT'), (6, 'Outro formato')])),
                ('navegacao', models.FloatField(blank=True, null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.municipio')),
            ],
        ),
    ]
