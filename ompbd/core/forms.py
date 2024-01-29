from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User # Comes from Django
        fields = ('username', 'email', 'password1', 'password2') # Fields that we want users to fillout