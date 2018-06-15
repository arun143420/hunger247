from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from food.models import Menu,CartManager


class OrdersDone(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    cartmanager = models.ForeignKey(CartManager, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    etc_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.item)


class OrderManager(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    delivery_time = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=10, default=0)
    payment = models.CharField(max_length=20,  )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)
    etc_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.order_id)


class OrdersConfirm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, blank=True, null=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    cartmanager = models.ForeignKey(OrderManager, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    etc_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.item)
