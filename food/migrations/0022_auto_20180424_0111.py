# Generated by Django 2.0.3 on 2018-04-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0021_cartmanager_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmanager',
            name='session',
        ),
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.CharField(max_length=500, null=True),
        ),
    ]