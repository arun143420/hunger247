from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


Area_Choice = (
    ('janipur', 'janipur'),
    ('disco road', 'disco road'),
    ('Talli morh', 'Talli morh'),
    ('New Plot', 'New Plot'),
    ('Ptoli', 'Ptoli'),
    ('Lower Roop Nagar', 'Lower Roop Nagar'),
    ('upper roop Nagar', 'Upper Roop Nagar'),
    ('Old Janipur', 'Old janipur'),
    ('gandhinagar','GandhiNagar'),
    ('Trikuta Nagar','Trikuta Nagar'),
    ('Amphalaa','Amphalla'),
    ('rehari','Rehari'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,unique=True,primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=False)
    area = models.CharField(max_length=20, choices=Area_Choice, default='None')
    address = models.CharField(max_length=40, blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    land_mark = models.CharField(max_length=30, blank=False)
    tc = models.BooleanField(blank=False, default=False)
    longitude = models.FloatField(max_length=30,null=True)
    latitude = models.FloatField(max_length=30, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ContactUs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=40, blank=False)
    Comment_and_Suggestion = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.user)