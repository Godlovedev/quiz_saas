from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

# Create your models here.

User = get_user_model()

class Quiz(models.Model):
    """ 
    description: models for quiz
    author: Godlove
    """

    title = models.CharField(max_length=30)

    description = models.TextField(blank=True, null=True)
    
    creator = models.ForeignKey(User, related_name="quiz", on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)

    is_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("quiz-running", kwargs={"id": self.id})
    
    def get_result_url(self):
        return reverse("result", kwargs={"id":self.id})
    
    def get_view_url(self):
        return reverse("view-quiz", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("delete-quiz", kwargs={"id":self.id})


class Question(models.Model):
    """
    author: Godlove
    description: this is the question model
    """

    quiz = models.ForeignKey(Quiz, related_name="question", on_delete=models.CASCADE)
    
    text = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    


class Choice(models.Model):

    """
    author: Godlove
    description: Choice model definition
    """

    question = models.ForeignKey(Question, related_name="choice", on_delete=models.CASCADE)

    text = models.CharField(max_length=200)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserResult(models.Model):

    """
    author: Godlove
    description: result model for user
    """

    user = models.ForeignKey(User, related_name="result", on_delete=models.CASCADE)

    quiz = models.ForeignKey(Quiz, related_name= "result", on_delete=models.CASCADE)

    score = models.FloatField(default=0)

    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.id} - Score: {self.score}"