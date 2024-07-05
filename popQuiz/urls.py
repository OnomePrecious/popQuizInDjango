from django.urls import path
from . import views

urlpatterns = [
    path('popquiz', views.quiz_questions),
    path('popquiz/viewAll', views.list_of_questions),
    path('popquiz/createQuiz', views.create_quiz),
]
