from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_premium = models.BooleanField(default=False)

    quiz_taken_today = models.IntegerField(default=0)

    total_quizzes_taken = models.IntegerField(default=0)

    profile_picture = models.ImageField(upload_to="images", null=True, blank=True)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username