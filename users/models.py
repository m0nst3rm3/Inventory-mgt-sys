from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class SignUpForm(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    username = models.CharField(max_length=15)
