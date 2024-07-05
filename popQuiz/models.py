from django.conf import settings
from django.db import models


# create your models here.
#
#
#
class Quiz(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    QUESTION_TYPE = [
        ('MEDIUM', 'FILL IN THE BLANK'),
        ('HARD', 'CODING EXERCISE'),
        ('EASY', 'TRUE/FALSE'),

    ]

    question_type = models.CharField(max_length=1, choices=QUESTION_TYPE, default='General science')

    def __str__(self):
        return f"{self.title}{self.description}{self.created_at}"


class Question(models.Model):
    # question_type = models.CharField(max_length=1, choices=QUESTION_TYPE, default='EASY')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} - {self.answer_text}"
