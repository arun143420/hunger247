# Generated by Django 2.0.3 on 2018-04-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180415_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tc',
            field=models.BooleanField(default=False),
        ),
    ]
