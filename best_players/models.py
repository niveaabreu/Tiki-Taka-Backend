from django.db import models

# Create your models here.
class Best_Player(models.Model):
    year=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    club=models.TextField(default=" ",null=True)
    value=models.TextField(default=" ",null=True)
    image=models.TextField(default=" ",null=True)
    country=models.TextField(default=" ",null=True)
    
    def __str__(self):
        return (self.title)
