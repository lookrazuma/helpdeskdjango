# Generated by Django 3.1.3 on 2021-06-09 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('can_mark_returned', 'Set Task as returned'),), 'verbose_name': 'Задачу', 'verbose_name_plural': 'Задачи'},
        ),
    ]
