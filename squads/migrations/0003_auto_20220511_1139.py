# Generated by Django 3.1.7 on 2022-05-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_squads_club_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squads',
            name='club_id',
            field=models.IntegerField(),
        ),
    ]
