from rest_framework import serializers

from .models import User, Quiz,Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'author']

        class Meta:
            model = Question
            fields = ['id', 'quiz', 'question_text']

            class Meta:
                model = Answer
                fields = ['id', 'question', 'answer_text', 'is_correct']