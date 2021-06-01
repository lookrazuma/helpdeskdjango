from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, Textarea, CharField, DateInput, DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView

class ContactList(ListView):
    paginate_by = 2
    model = Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = {'title','host_name','dept','task', 'author'}
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите кратко суть возникшей проблемы'
            }),
            "host_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите hostname вашего компьютера, например, A01-001-001'
            }),
            "dept": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отдел работы'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи'
            }),
        }

class TaskContactorForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'title','host_name','dept','task', 'author', 'status_task', 'comment'}
        widgets = {   
            'title' : forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'host_name': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'dept': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'task': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'author': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'status_task': forms.Select(),
            'comment': forms.TextInput(attrs={'class':'form-control'}),
        } 


class Task_statusForm(ModelForm):
    class Meta:
        model = Task
        fields = {'status_task'}
        widgets = {
            "status_task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите статус'
            })
        }


def __init__(self, max_length=None, min_length=None, strip=True, empty_value='', *args, **kwargs):


    super(CharField, self).__init__(*args, **kwargs)
      # attrs is passed to Field -> error


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        widgets = {  
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        } 

class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['host_name', 'dept']
        widgets = {
            'host_name': forms.TextInput(attrs={'class':'form-control'}),
            'dept': forms.TextInput(attrs={'class':'form-control'}),
        }
