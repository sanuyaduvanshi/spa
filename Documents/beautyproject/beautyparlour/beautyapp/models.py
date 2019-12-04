from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

def __str__(self):
    return self.firstame

class Citys(models.Model):
        name=models.CharField(max_length=50)

        def __str__(self):
            return self.name

class Services(models.Model):
        name=models.CharField(max_length=50)
        category=models.CharField(max_length=50)
        description=models.CharField(max_length=100)
        price=models.IntegerField()
        image=models.ImageField(upload_to='signup/images')


        def __str__(self):
            return self.name


class Gift(models.Model):
        name=models.CharField(max_length=50)
        email=models.CharField(max_length=50)
        mobile=models.IntegerField()
        address=models.CharField(max_length=200)
        message=models.CharField(max_length=500)
        price=models.IntegerField()


        def __str__(self):
            return self.name



class Appointment(models.Model):
    name=models.CharField(max_length=50)
    mobileno = models.IntegerField()
    # city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    date=models.DateField()
    time=models.TimeField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
    return self.services
