# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import generate_question

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


class QuizQuestions(APIView):
    def get(self, request):
        serializer = QuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.data['title']
        description = serializer.data['description']
        author = serializer.data['author']
        question = get_object_or_404(Quiz)
        question = generate_question(question)
        Question.objects.create(
            title=title, description=description,
            author=author,
            question_text=question

        )
        return Response(question, status=status.HTTP_200_OK)


# @api_view()
# def quiz_questions():
#     quizzes = Quiz.objects.all()
#     serializer = QuizSerializer(quizzes, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#

@api_view()
def list_of_questions(request):
    user = request.user
    questions = get_object_or_404(Question, user=user.id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @staff_member_required
# def create_quiz(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         author = request.admin
#         quiz = Quiz.objects.create(title=title, description=description, author=author)
#         serializer = QuizSerializer(quiz, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
