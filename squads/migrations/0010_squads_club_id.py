# Generated by Django 3.1.7 on 2022-05-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0009_auto_20220511_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='squads',
            name='club_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
