# Generated by Django 2.0.3 on 2018-05-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0025_auto_20180505_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmanager',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
