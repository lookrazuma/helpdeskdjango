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
    """
    Форма подачи заявки
    """
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

    """
    Редактирование заявки исполнителем
    """
    authorr = forms.CharField( # Переопределяем значения поля с внешним ключем
        label='Автор',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control disabled', 'readonly':''}),
    )


    class Meta:
        model = Task
        fields = {'title','host_name','dept','task', 'status_task', 'comment'}
        widgets = {   
            'title' : forms.TextInput(attrs={'class':'form-control disabled', 'id':'disabledTextInput', 'readonly':'',}),
            'host_name': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'dept': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'task': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            # 'author': forms.TextInput(attrs={'class':'form-control disabled', 'readonly':''}),
            'status_task': forms.Select(attrs={'class':'form-control',}),
            'comment': forms.TextInput(attrs={'class':'form-control'}),
        } 

    def __init__(self, *args, **kwargs):
        super(TaskContactorForm, self).__init__(*args, **kwargs)
        self.initial['authorr'] = self.instance.author
    def save(self, commit=True):
        instance = super(TaskContactorForm, self).save(commit=False)
        cleaned_authorr = self.cleaned_data['authorr']
        
        return instance
 




class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления стандартной модели пользователя
    """
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
    """
    Форма обновления кастомных добавочных полей
    """
    class Meta:
        model = Profile
        fields = ['host_name', 'dept', 'photo']
        widgets = {
            'host_name': forms.TextInput(attrs={'class':'form-control'}),
            'dept': forms.TextInput(attrs={'class':'form-control'}),
        }
