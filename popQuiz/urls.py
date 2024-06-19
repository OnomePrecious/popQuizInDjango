from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.quiz_questions),
    path('accounts/viewAll', views.list_of_questions),
    path('accounts/createQuiz', views.create_quiz),
]
