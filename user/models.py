from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = models.CharField('username', max_length=30, unique=True)
    password = models.CharField('password', max_length=128)