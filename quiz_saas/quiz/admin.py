from django.contrib import admin
from quiz.models import Quiz, Question, Choice, UserResult

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserResult)