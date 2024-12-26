from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()

""" Fonction pour remettre le nombre de quiz journalier fait par l'utilisateur a 0 """
@shared_task
def refactoring_user_limit_quiz():
    users = User.objects.all()
    for user in users:
        user.quiz_taken_today = 0
        user.save()