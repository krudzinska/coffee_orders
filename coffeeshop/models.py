from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    offer = models.TextField()

