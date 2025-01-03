from django.forms import ModelForm
from quiz.models import Payment, Quiz, Question, Choice


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

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'surname', 'email', 'phone_number', 'address', 'city', 'country', 'state', 'zip_code']