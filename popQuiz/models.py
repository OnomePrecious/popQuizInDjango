from django.db import models

from popQuiz.admin import Admin


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
    author = models.ForeignKey(Admin, on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
