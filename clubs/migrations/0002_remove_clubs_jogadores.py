# Generated by Django 3.1.7 on 2022-05-10 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='jogadores',
        ),
    ]
