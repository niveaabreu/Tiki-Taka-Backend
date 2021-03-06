# Generated by Django 3.1.7 on 2022-05-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('emblema', models.TextField(default=' ', null=True)),
                ('cidade', models.TextField(default=' ', null=True)),
                ('socios', models.TextField(default=' ', null=True)),
                ('data_fundacao', models.TextField(default=' ', null=True)),
                ('pais', models.TextField(default=' ', null=True)),
                ('liga', models.TextField(default=' ', null=True)),
                ('treinador', models.TextField(default=' ', null=True)),
                ('valor', models.TextField(default=' ', null=True)),
                ('estadio_nome', models.TextField(default=' ', null=True)),
                ('estadio_foto', models.TextField(default=' ', null=True)),
                ('estadio_lotacao', models.TextField(default=' ', null=True)),
                ('colocacao', models.TextField(default=' ', null=True)),
                ('jogadores', models.TextField(default=' ', null=True)),
            ],
        ),
    ]
