# Generated by Django 2.0.3 on 2018-04-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180415_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='area',
            field=models.CharField(choices=[('janipur', 'janipur'), ('disco road', 'disco road'), ('Talli morh', 'Talli morh'), ('New Plot', 'New Plot'), ('Ptoli', 'Ptoli'), ('Lower Roop Nagar', 'Lower Roop Nagar'), ('upper roop Nagar', 'Upper Roop Nagar'), ('Old Janipur', 'Old janipur'), ('gandhinagar', 'GandhiNagar'), ('Trikuta Nagar', 'Trikuta Nagar'), ('Amphalaa', 'Amphalla'), ('rehari', 'Rehari')], default=None, max_length=20),
        ),
    ]
