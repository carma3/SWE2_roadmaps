from django import forms
from .models import AppUser, Class
from django.contrib.auth.forms import UserCreationForm

# forms.py handles form validation and structure and can be called
# from an html file so we don't have to manually make the forms in there

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = AppUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']

class CreateClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ["class_name", "class_desc", "class_student"]