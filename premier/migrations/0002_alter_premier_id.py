# Generated by Django 4.0.4 on 2022-05-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premier',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
