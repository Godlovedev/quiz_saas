from django.forms import ModelForm
from quiz.models import Quiz, Question, Choice


""" formulaire pour des quiz """

class QuizForm(ModelForm):

    class Meta:
        model = Quiz
        fields = ("title", "description", "creator")


""" formulaire des questions """

class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ("text",)


""" formulaire pour les choix des differente questions """
class ChoiceForm(ModelForm):

    class Meta:
        model = Choice
        fields = ("text",)