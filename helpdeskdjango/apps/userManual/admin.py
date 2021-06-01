from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import userManual
# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django import forms

# admin.site.register(userManual)
class userManualAdminForm(forms.ModelForm):
    description_main = forms.CharField(label='dfgs', widget=CKEditorWidget())
    description_two = forms.CharField(label='Описание №2', widget=CKEditorWidget())
    
    
    
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
    )
    # readonly_fields= ('author',)
