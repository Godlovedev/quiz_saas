from django.urls import path
from quiz import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("quiz-list/", views.QuizView.as_view(), name="quiz-list"),
    path("quiz-list/<int:id>/", views.QuizRunnigView.as_view(), name="quiz-running"),
    path("quiz-list/<str:id>/user-result/", views.UserResultView.as_view(), name="result"),
    path("create/", views.CreateQuizView.as_view(), name="create-quiz"),
    path("panel/", views.PanelView.as_view(), name="panel"),
    path("view-quiz/<int:id>/", views.ViewQuizView.as_view(), name="view-quiz"),
    path("delete-quiz/<int:id>/", views.DeleteQuizView.as_view(), name="delete-quiz"),
    path("view-quiz/<int:id>/add-question/", views.AddQuestionView.as_view(), name="add-question")
]
