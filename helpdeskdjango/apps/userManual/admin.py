from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import userManual
# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django import forms

# admin.site.register(userManual)
class userManualAdminForm(forms.ModelForm):
    description_main = forms.CharField(label='Основное описание', widget=CKEditorWidget())
    description_two = forms.CharField(label='Описание №2', widget=CKEditorWidget())
    # description_three = forms.CharField(label='Описание №3', widget=CKEditorWidget())
    # description_four = forms.CharField(label='Описание №4', widget=CKEditorWidget())
    # description_five = forms.CharField(label='Описание №5', widget=CKEditorWidget())    
    # description_six = forms.CharField(label='Описание №6', widget=CKEditorWidget())
    # description_seven = forms.CharField(label='Описание №7', widget=CKEditorWidget())
    # description_eight = forms.CharField(label='Описание №8', widget=CKEditorWidget())
    # description_nine = forms.CharField(label='Описание №9', widget=CKEditorWidget())
    
    
    
    class Meta:
        model = userManual
        fields = '__all__'

@admin.register(userManual)
class userManualAdmin(ImportExportModelAdmin):    
    pass


    list_display = ('date_publiched', 'name', 'img_main', 'relevancy',)
    list_editable = ('relevancy',)
    list_display_links = ('name', 'date_publiched')
    list_filter = ('name', 'date_publiched',)
    save_as = True
    actions_on_top = True
    form = userManualAdminForm
    # actions = [make_new, make_read, make_in_progress, make_completed, make_rejection]
    fieldsets = (
        ('Основная информация', {
            'fields': ('name','img_main','description_main','relevancy',)
        }),
        ('Дополнительная информация, добавляет 3 поля', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'img_two', 'description_two', 
                'img_three', 'description_three',
                'img_four', 'description_four',)
        }),
        ('Ещё дополнительная информация, добавляет еще 4 поля', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'img_five', 'description_five',
                'img_seven', 'description_six',
                'img_eight', 'description_eight',
                'img_nine', 'description_nine',)
        }),
    )
    # readonly_fields= ('author',)
