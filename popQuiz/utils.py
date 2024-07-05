import random

from .models import Question


def generate_question(questions):
    all_questions = list(Question.objects.all())
    random_questions = random.sample(all_questions, questions)
    quiz_questions = []

    for question in random_questions:
        quiz_questions.append({
            'question_text': question.question_text,
            'option': [],
            'answers': question.answer
        })

        return quiz_questions
