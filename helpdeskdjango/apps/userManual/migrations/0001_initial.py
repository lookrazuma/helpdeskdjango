# Generated by Django 3.1.3 on 2021-06-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userManual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('img_main', models.ImageField(blank=True, upload_to='userManual/', verbose_name='Главное изображение')),
                ('url', models.SlugField(blank=True, max_length=160)),
                ('date_publiched', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации руководства')),
                ('relevancy', models.BooleanField(default=False, verbose_name='Актуальность')),
            ],
            options={
                'verbose_name': 'Руководство пользователя',
                'verbose_name_plural': 'Руководства пользователя',
                'managed': True,
            },
        ),
    ]
