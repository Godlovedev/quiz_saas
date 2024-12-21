from django.urls import path
from accounts import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.ConnexionView.as_view(), name="login")
]
