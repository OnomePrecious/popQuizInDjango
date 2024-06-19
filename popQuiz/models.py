from django.db import models


# create your models here.
#
#
#


class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100)


class Admin(models.Model):
    admin_id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100)

