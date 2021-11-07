from django.db import models

# Create your models here.
class Regi(models.Model):
    username = models.CharField(max_length=15)
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname =models.CharField(max_length=20)
    
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    email = models.CharField(max_length=20)
    password= models.CharField(max_length=10)
    def __str__(self):
        return self.firstname


