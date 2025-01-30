# Create your models here.
from django.db import models


class person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()


class pen(models.Model):
    color = models.CharField(max_length=200)
    quantity = models.IntegerField()
