# Generated by Django 2.0.3 on 2018-04-13 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0015_cartmanager_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(default=0, max_length=10)),
                ('item_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('payment', models.CharField(default='COD', max_length=20)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.Menu')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
