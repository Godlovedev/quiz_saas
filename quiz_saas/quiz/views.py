from django.shortcuts import render
from django.views import View
from quiz.models import Quiz, Question, UserResult
from quiz.utils import LoginRequiredMixin


# Create your views here.
class HomeView(View):
    def get(self, *args, **kwargs):

        return render(self.request, "home.html")

class QuizView(View):
    def get(self, *args, **kwargs):

        quizs = Quiz.objects.select_related("creator").all()

        return render(self.request, "quiz_list.html", {"quizs":quizs})


class QuizRunnigView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        quiz_id = self.kwargs.get("id")

        quiz = Quiz.objects.prefetch_related("question__choice").get(id=quiz_id)

        return render(self.request, "quiz_running.html", {"quiz":quiz})

    def post(self, *args, **kwargs):

        quiz_id = self.kwargs.get("id")

        quiz = Quiz.objects.prefetch_related("question__choice").get(id=quiz_id)
        
        questions_id = self.request.POST.getlist("questionid")
        self.request.user.quiz_taken_today += 1

        """
        recuperer les resultat du user et s'il n'existe pas les creer
        si elle existe on met le score a 0 pour ne pas que l'on incremente l'ancien score de 1
        """
        user_result, created = UserResult.objects.get_or_create(user=self.request.user, quiz=quiz)

        if created:
                self.request.user.total_quizzes_taken += 1

        self.request.user.save()

        user_result.score = 0

        # parcourrir tous les id dans la liste créée
        for question_id in questions_id:

            # reccuperer la question qui correspond a cet id
            question = quiz.question.get(id=question_id)

            # a partir de cet id recuperer l'id du choic du user
            # dans le post c'est envoyé ainsi "id_de_la_question": "id_de_la_reponse"
            choice_id = self.request.POST.get(question_id)

            # recuperation de la reponse a partir de l'id de la reponse du user
            choice = question.choice.get(id=choice_id)

            # verifier si le champ is_correct de la question est a true
            # si c'ést le cas cela signifie que lq reponse est juste
            if choice.is_correct == True:

                """
                incrementer le score de l'utilisateur de 1 si le a reponse est juste
                et le sauvegarder
                """
                user_result.score += 1

                user_result.save()

        return render(self.request, "quiz_running.html", {"quiz":quiz})