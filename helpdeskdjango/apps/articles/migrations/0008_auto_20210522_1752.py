# Generated by Django 3.1.3 on 2021-05-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210522_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_img',
            field=models.ImageField(upload_to='media_cdn/article-images/'),
        ),
    ]
