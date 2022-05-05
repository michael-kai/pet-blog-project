from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class LoginTest(forms.Form):
    name = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput({'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('article', 'name', 'body')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'msg')
