# Create your models here.
from django.db import models



class Register(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Email

class Login(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Email