from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """ 
    Класс формы комментрариев
    """
    class Meta:
        model = Comment # Объявление используемой в форме модели
        fields = [ # Поля, берущиеся из модели для формы
            'comment_text'
        ]