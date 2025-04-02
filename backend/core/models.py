from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 100)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)