# Generated by Django 3.1.3 on 2021-05-14 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_merge_20210515_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
            preserve_default=False,
        ),
    ]