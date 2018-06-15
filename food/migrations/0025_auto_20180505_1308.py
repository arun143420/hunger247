# Generated by Django 2.0.3 on 2018-05-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0024_auto_20180504_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='longitude',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
