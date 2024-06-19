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


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()