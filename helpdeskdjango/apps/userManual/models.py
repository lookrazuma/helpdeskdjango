from django.db import models
from datetime import date
# Создаю 
class userManual(models.Model):

    name = models.CharField('Название', max_length = 150,)

    img_main = models.ImageField("Главное изображение", upload_to='userManual/', blank=True)
    description_main = models.TextField('Основное описание')

    url = models.SlugField(max_length=160, blank=True)
    date_publiched = models.DateTimeField('Дата публикации руководства', auto_now_add=True)
    relevancy = models.BooleanField('Актуальность', default=False)

    img_two = models.ImageField("Изображение №2", upload_to='userManual/', blank=True)
    description_two = models.TextField('Описание №2', blank=True, null=True)
    
    img_three = models.ImageField("Изображение №3", upload_to='userManual/', blank=True)
    description_three = models.TextField('Описание №3', blank=True, null=True)
    
    img_four = models.ImageField("Изображение №4", upload_to='userManual/', blank=True)
    description_four = models.TextField('Описание №4', blank=True, null=True)

    img_five = models.ImageField("Изображение №5", upload_to='userManual/', blank=True)
    description_five = models.TextField('Описание №5', blank=True, null=True)

    img_six = models.ImageField("Изображение №6", upload_to='userManual/', blank=True)
    description_six = models.TextField('Описание №6', blank=True, null=True)

    img_seven = models.ImageField("Изображение №7", upload_to='userManual/', blank=True)
    description_seven = models.TextField('Описание №7', blank=True, null=True)

    img_eight = models.ImageField("Изображение №8", upload_to='userManual/', blank=True)
    description_eight = models.TextField('Описание №8', blank=True, null=True)

    img_nine = models.ImageField("Изображение №9", upload_to='userManual/', blank=True)
    description_nine = models.TextField('Описание №9', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Руководство пользователя'
        verbose_name_plural = 'Руководства пользователя'
    