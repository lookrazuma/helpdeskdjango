# Generated by Django 3.1.3 on 2021-05-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210522_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_img',
            field=models.ImageField(upload_to='article-images/'),
        ),
    ]