# Generated by Django 3.1.3 on 2021-05-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210515_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_img',
            field=models.ImageField(default='', upload_to=None),
            preserve_default=False,
        ),
    ]