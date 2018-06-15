# Generated by Django 2.0.3 on 2018-05-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_auto_20180428_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session',
        ),
        migrations.AddField(
            model_name='cart',
            name='etc_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='cartmanager',
            name='etc_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
