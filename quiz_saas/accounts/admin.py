from django.contrib import admin
from accounts.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_premium", "total_quizzes_taken", "quiz_taken_today")

admin.site.register(User, UserAdmin)