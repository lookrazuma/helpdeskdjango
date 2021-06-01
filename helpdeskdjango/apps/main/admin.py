from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Task, status
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.template.defaultfilters import truncatechars

#admin.site.register(Task)
admin.site.register(status)

 
from ckeditor.widgets import CKEditorWidget
from django import forms


class MyAdminSite(AdminSite):
    
     def get_urls(self):
         from django.urls import path
         urls = super().get_urls()
         urls += [
             path('my_view/', self.admin_view(self.my_view))
         ]
         return urls

     def my_view(self, request):
         return HttpResponse("Hello!")

admin_site = MyAdminSite()





class TaskAdminForm(forms.ModelForm):
    task = forms.CharField(label='Описание', widget=CKEditorWidget())
    
    class Meta:
        model = Task 
        fields = '__all__'


# Функция для быстрого действия, выполняет проставления статусов "Выполнено"
def make_new(modeladmin, request, queryset):
        queryset.update(status_task='Заявка отправлена')
make_new.short_description = "Проставить статус 'Новая заявка' дня выбранных задач"
make_new.allowed_permissions = ('change',)


# Функция для быстрого действия, выполняет проставления статусов "Выполнено"
def make_read(modeladmin, request, queryset):
        queryset.update(status_task='Заявка прочитана')
make_read.short_description = "Проставить статус 'Прочитано' дня выбранных задач"
make_read.allowed_permissions = ('change',)


# Функция для быстрого действия, выполняет проставления статусов "Выполнено"
def make_in_progress(modeladmin, request, queryset):
        queryset.update(status_task='Исполнитель назначен')
make_in_progress.short_description = "Проставить статус 'Назначен исполнитель' дня выбранных задач"
make_in_progress.allowed_permissions = ('change',)


# Функция для быстрого действия, выполняет проставления статусов "Выполнено"
def make_completed(modeladmin, request, queryset):
        queryset.update(status_task='Заявка выполнена')
make_completed.short_description = "Проставить статус 'Выполнено' дня выбранных задач"
make_completed.allowed_permissions = ('change',)


# Функция для быстрого действия, выполняет проставления статусов "Выполнено"
def make_rejection(modeladmin, request, queryset):
        queryset.update(status_task='Заявка отклонена')
make_rejection.short_description = "Проставить статус 'Отклонено' дня выбранных задач"
make_rejection.allowed_permissions = ('change',)



@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):    
    pass


    list_display = ('id','status_task_colored', 'create_date', 'title', 'author','host_name', 'task', 'contractor', 'status_task', 'in_progress_time')
    
    list_editable = ('status_task', 'contractor')
    list_display_links = ('title', 'task')
    list_filter = ('status_task', 'author',)
    search_fields = ['title', 'task', 'status_task', 'id']
    save_as = True
    actions_on_top = True
    form = TaskAdminForm
    actions = [make_new, make_read, make_in_progress, make_completed, make_rejection]
    fieldsets = (
        ('Информация от заявителя', {
            'fields': ('title','author', 'host_name', 'task', 'dept')
        }),
        ('Контроль заявки', {
            # 'classes': ('collapse',),
            'fields': ('contractor', 'status_task', 'num_for_chart', 'comment')
        }),
    )
    # readonly_fields= ('author',)

    def get_fields(self, request, obj=None):
        exist_task = ['title', 'host_name', 'task', ['contractor','status_task',]]
        if not obj:
            exist_task.append('author')
        return exist_task

    def status_task_colored(self, obj):
        colors = {
            'Заявка отправлена': ' ',
            'Заявка прочитана': 'orange',
            'Исполнитель назначен': 'red',
            'Заявка выполнена': 'green',
            'Заявка отклонена': 'black',
        }
        return format_html(
            '<div style="background:{};">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</div>',
            colors[obj.status_task],
            obj.status_task,
        )
