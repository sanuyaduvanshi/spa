from django.db import models
from beautyapp.models import Services

# Create your models here.
class Guest(models.Model):
    gname = models.CharField(max_length=50)
    mobile=models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

def __str__(self):
    return self.firstame

class Addstaff(models.Model):
    name = models.CharField(max_length=250)
    mobileno=models.CharField(max_length=12)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)


def __str__(self):
    return self.name
