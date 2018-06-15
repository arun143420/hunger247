# Generated by Django 2.0.3 on 2018-04-11 08:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('starters', 'Starters'), ('main courses', 'Main Courses'), ('Light meals', 'Light Meals'), ('snacks', 'Snacks'), ('Drinks', 'Drinks')], default=None, max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('category', models.CharField(choices=[('dhaba', 'DHABA'), ('cafe', 'CAFE'), ('fast_food', 'FAST FOOD'), ('destination_restaurant', 'DESTINATION RESTAURANT')], default=None, max_length=40)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Restaurant'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Menu'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]