from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'ordermanage'

urlpatterns = [


    url(r'^orders/$', views.order_list_view, name='order-list'),
    url(r'orders/(?P<pk>[0-9]+)/detail/$', views.order_detail_view, name='order-detail'),
    url(r'orders/(?P<pk>[0-9]+)/confirm/$',views.order_list_update_view, name='order-list-update'),
    url(r'confirm-orders/$', views.confirm_orders, name='order-confirm-list'),
    url(r'confirm-orders/(?P<pk>[0-9]+)/$', views.confirm_order_detail, name='confirm-order'),
    url(r'restaurants/orders/$', views.resturants_orders, name='order'),






]