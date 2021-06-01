import datetime
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post', default=None)
    main_img = models.ImageField(upload_to='article-images/')

    def was_published_recently(self):
        return self.pub_date >=(timezone.now() - datetime.timedelta(days = 7))

    def __str__(self):
        return self.article_title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя авторя', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)
    date_comment = models.DateTimeField('Дата создания комментария', auto_now_add=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'