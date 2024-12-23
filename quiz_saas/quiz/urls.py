from django.urls import path
from quiz import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("quiz-list/", views.QuizView.as_view(), name="quiz-list"),
    path("quiz-list/<int:id>/", views.QuizRunnigView.as_view(), name="quiz-running"),
    path("quiz-list/<str:id>/user-result/", views.UserResultView.as_view(), name="result")
]
