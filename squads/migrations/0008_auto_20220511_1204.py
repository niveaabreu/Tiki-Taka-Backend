# Generated by Django 3.1.7 on 2022-05-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0007_auto_20220511_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squads',
            name='club_id',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='squads',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
