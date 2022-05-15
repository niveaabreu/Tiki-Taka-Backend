from django.db import models
# Create your models here.
class Squads(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id = models.BigIntegerField(serialize=True,null=True)
    name=models.CharField(max_length=200,null=True)
    image=models.TextField(default=" ",null=True)
    age = models.TextField(default=" ",null=True)
    shirtNumber = models.TextField(default=" ",null=True)
    def __str__(self):
        return (self.title)
