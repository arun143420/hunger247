# Generated by Django 2.0.3 on 2018-04-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_auto_20180417_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmanager',
            name='session',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
