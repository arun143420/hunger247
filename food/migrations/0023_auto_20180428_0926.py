# Generated by Django 2.0.3 on 2018-04-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0022_auto_20180424_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]
