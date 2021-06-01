from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm

#Форма регистрации пользователей
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField( required = True)

    field_order = ['username','email','password','password']

