from django.db import models
from datetime import date
# Создаю 
class userManual(models.Model):

    name = models.CharField('Название', max_length = 150,)

    img_main = models.ImageField("Главное изображение", upload_to='userManual/', blank=True, null=True)
    description_main = models.TextField('main_desc', default=False)

    date_publiched = models.DateTimeField('Дата публикации руководства', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Руководство пользователя'
        verbose_name_plural = 'Руководства пользователя'
    