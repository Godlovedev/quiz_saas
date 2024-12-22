from django.shortcuts import render
from django.views import View
from quiz.models import Quiz, Question

# Create your views here.
class HomeView(View):
    def get(self, *args, **kwargs):

        return render(self.request, "home.html")

class QuizView(View):
    def get(self, *args, **kwargs):

        quizs = Quiz.objects.select_related("creator").all()

        return render(self.request, "quiz_list.html", {"quizs":quizs})


class QuizRunnigView(View):
    def get(self, *args, **kwargs):
        quiz_id = self.kwargs.get("id")

        quiz = Quiz.objects.prefetch_related("question__choice").get(id=quiz_id)

        # questions = quiz.question.all()

        return render(self.request, "quiz_running.html", {"quiz":quiz})