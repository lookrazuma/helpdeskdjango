from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import userManual
# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django import forms

# admin.site.register(userManual)
class userManualAdminForm(forms.ModelForm):
    description_main = forms.CharField(label='dfgs', widget=CKEditorWidget())
    
    
    
    class Meta:
        model = userManual
        fields = '__all__'

@admin.register(userManual)
class userManualAdmin(ImportExportModelAdmin):    
    pass


    form = userManualAdminForm

    # readonly_fields= ('author',)
