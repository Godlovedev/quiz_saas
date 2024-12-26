from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import UserForm, UserConnexion
from django.contrib.auth import login, authenticate, logout

# Create your views here.

# sing up view
class RegisterView(View):
    context = {}

    def get(self, *args, **kwargs):
        form = UserForm()

        self.context = {
            "form": form
        }

        return render(self.request, "sing_up.html", self.context)

    def post(self, *args, **kwargs):

        form = UserForm(self.request.POST)

        if form.is_valid():

            form.save()
            
        return redirect("login")


# Connexion view
class ConnexionView(View):
    def get(self, *args, **kwargs):
        
        form = UserConnexion()

        return render(self.request, "login.html", {"form": form})

    def post(self, *args, **kwargs):

        form = UserConnexion(self.request.POST)
        
        message = ""

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:

                login(self.request, user)

                return redirect("quiz-list")            
            else:
                message = "une erreur s'est produite !"

        return redirect("quiz-list")


# decconnection view
class DeconnecxionView(View):
    def get(self, *args, **kwargs):

        logout(self.request)

        return redirect("login")