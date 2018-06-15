from django.contrib import admin
from food.models import Restaurant, Menu, Cart, CartManager

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(CartManager)


