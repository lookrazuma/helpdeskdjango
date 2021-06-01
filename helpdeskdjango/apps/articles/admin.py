from django.contrib import admin

from .models import Article, Comment


admin.site.register(Comment) 
from ckeditor.widgets import CKEditorWidget # Импортирую библиотеку CKEditor, добавляющую редактироемое поле с декоратором safe
from django import forms

class ArticleAdminForm(forms.ModelForm):
    """ 
        Класс кастомных форм, добавляю поле для декорированного текста 
    """
    article_text = forms.CharField(label='Описание', widget=CKEditorWidget())
    
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article) # используем специальный декоратор для работы с отображаемой админкой
class ArticleAdmin(admin.ModelAdmin):
    """
        Класс кастомной админки
    """    
    pass


    list_display = ('article_title', 'pub_date') # Определяет, какие поля будут отображаться в окне предпросмотра
    list_display_links = ('article_title', 'pub_date') # Определяет поля-ссылки по которым можно перейти к детальному просмотру модели
    list_filter = ('article_title',) # Определяет поля, по которым можно проводить фильтрацию
    form = ArticleAdminForm # Объявляю формы, используемые в этой модельке