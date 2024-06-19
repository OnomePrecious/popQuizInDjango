# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


# Create your views here.
@api_view()
def quiz_questions(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def list_of_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@staff_member_required
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.admin
        quiz = Quiz.objects.create(title=title, description=description, author=author)
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)