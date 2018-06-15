from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings


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

Restaurant_Choice = (
    ('dhaba', 'DHABA'),
    ('cafe', 'CAFE'),
    ('fast_food', 'FAST FOOD'),
    ('destination_restaurant', 'DESTINATION RESTAURANT'),
    ('Street_food', 'street food'),
)

# left side to be used in templates

Menu_Choice = (
    ('starters', 'Starters'),
    ('main courses', 'Main Courses'),
    ('Light meals', 'Light Meals'),
    ('snacks', 'Snacks'),
    ('Drinks','Drinks'),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=40, blank=False)
    logo = models.ImageField(blank=True)
    category = models.CharField(max_length=40, choices=Restaurant_Choice, blank=False, default=None)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    area = models.CharField(max_length=30,choices=Area_Choice,default='janipur')
    address = models.CharField(max_length=40, blank=False)
    location = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=False)
    category = models.CharField(max_length=20,choices=Menu_Choice, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.CharField(max_length=80, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.restaurant)+"="+"("+str(self.name)+")"


class CartManager(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=10, default=0)
    payment = models.CharField(max_length=20, default='COD')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    etc_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.order_id)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    cartmanager = models.ForeignKey(CartManager, on_delete=models.CASCADE,null=True)
    add_time = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2,  default=0)
    etc_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.item)

