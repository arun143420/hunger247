# Generated by Django 2.0.3 on 2018-04-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20180411_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(to='food.Menu'),
        ),
    ]