# Generated by Django 3.1.3 on 2021-05-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManual', '0003_auto_20210509_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanual',
            name='relevancy',
            field=models.BooleanField(default=False, verbose_name='Актуальность'),
        ),
    ]