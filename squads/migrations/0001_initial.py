# Generated by Django 3.1.7 on 2022-05-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squads',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.TextField(default=' ', null=True)),
                ('age', models.TextField(default=' ', null=True)),
                ('shirtNumber', models.TextField(default=' ', null=True)),
            ],
        ),
    ]
