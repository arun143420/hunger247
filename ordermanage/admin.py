from django.contrib import admin
from ordermanage.models import OrdersDone,OrderManager,OrdersConfirm

admin.site.register(OrdersDone)
admin.site.register(OrderManager)
admin.site.register(OrdersConfirm)
