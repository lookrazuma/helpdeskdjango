from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse 
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver


class status(models.Model):
    status_name = models.CharField('Название статуса', max_length = 50,)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    


class Task(models.Model):
    
    STATUS_NEW = 'Заявка отправлена'
    STATUS_READ = 'Заявка прочитана'
    STATUS_IN_PROGRESS = 'Исполнитель назначен'
    STATUS_COMPLETED = 'Заявка выполнена'
    STATUS_REJECTION = 'Заявка отклонена'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Заявка отправлена'),
        (STATUS_READ, 'Заявка прочитана'),
        (STATUS_IN_PROGRESS, 'Исполнитель назначен'),
        (STATUS_COMPLETED, 'Заявка выполнена'),
        (STATUS_REJECTION, 'Заявка отклонена')
    )
    num_for_chart = models.IntegerField("Значение для диаграммы", default="1")
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    title = models.CharField('Название', max_length = 50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='task_user_type')
    host_name = models.CharField('Хост компьютера', max_length = 50, default='')
    contractor = models.ForeignKey(User, 
    on_delete=models.SET_NULL, # При удалении исполнителя не удаляется задача
    default=None, 
    null=True,  
    blank=True, 
    related_name='task_contractor_type',
    limit_choices_to={'is_staff': True},
    help_text=('Укажите исполнителя и поменяйте статус на "Исполнитель назначен"'),

    )
    dept = models.CharField('Отдел работы', max_length = 50, default='')
    task = models.TextField('Описание') 
    comment = models.TextField('Коментарий от исполнителя', default='')
    status_task = models.CharField(
        'Статус заказа', 
        max_length = 50, 
        choices = STATUS_CHOICES, 
        default = STATUS_NEW,
        help_text=('Указывайте только актуальные статусы'),
        )
    in_progress_time = models.DateTimeField('Время последнего изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
        permissions = (("can_mark_returned", "Set book as returned"),)


    def get_absolute_url(self):
        return reverse("task_details_url", kwargs={"task_id": self.pk})

    def get_update_url(self):
        return reverse("task_update_url", kwargs={"task_id": self.pk})

class Profile(models.Model):
    # CASCADE means if the user is deleted the profile is deleted
    # However, If the profile is deleted, the user is not deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    host_name = models.CharField('Хост компьютера', max_length = 50, default='', blank=True, null=True)
    dept = models.CharField('Отдел работы', max_length = 50, default='', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"user_id": self.user.pk})
    
    def get_update_url(self):
        return reverse("profile_update_url", kwargs={"user_id": self.user.pk})


