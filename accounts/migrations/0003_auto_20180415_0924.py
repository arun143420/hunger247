# Generated by Django 2.0.3 on 2018-04-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_tc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tc',
            field=models.BooleanField(),
        ),
    ]
