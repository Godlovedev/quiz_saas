from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserConnexion(forms.Form):
    
    username = forms.CharField(required=True)

    password = forms.CharField(required=True)