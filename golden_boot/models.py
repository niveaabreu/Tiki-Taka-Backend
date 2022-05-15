from django.db import models

# Create your models here.
class Golden_Boot(models.Model):
    first_name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    club=models.TextField(default=" ",null=True)
    goals=models.TextField(default=" ",null=True)
    image=models.TextField(default=" ",null=True)
    country=models.TextField(default=" ",null=True)
    matches=models.TextField(default=" ",null=True)
    def __str__(self):
        return (self.title)
