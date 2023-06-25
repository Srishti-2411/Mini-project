

# Create your models here.
from django.db import models

class register(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=200)
    address = models.TextField()
    psw = models.CharField(max_length=10)
    pswr = models.CharField(max_length=10)
