# Generated by Django 3.1.3 on 2021-05-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_img',
            field=models.ImageField(upload_to='article-images/'),
        ),
    ]
