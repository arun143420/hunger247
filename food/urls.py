from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'food'

urlpatterns = [


    url(r'restaurants$', views.restaurants_list_view, name='restaurants_list'),
    url(r'restaurants/advanced$', views.advanced_search_view, name='advanced_list'),
    url(r'^restaurants/my$', views.my_restaurant_list, name='my_restaurant_list'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.restaurant_detail_view, name='restaurant-detail'),
    url(r'^menu/(?P<pk>[0-9]+)/add/$', views.add_to_cart,name='add-cart'),
    url(r'^cart/$', views.cart_view, name='my_cart'),
    url(r'^cart/(?P<pk>[0-9]+)/delete/$', views.delete_from_cart, name='delete-cart'),
    url(r'^order/confirm/$', views.order_confirm_view, name='order_confirm'),
    url(r'^clear/cart/$', views.clear_cart, name='delete-all-cart'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^my-orders/$', views.my_orders_view, name='my_orders'),
    url(r'^my-orders/(?P<pk>[0-9]+)/$', views.my_order_deatil, name='my_orders_detail'),
    url(r'^cart/order/paypal/confirm/$', views.paypal_cnf, name='paypal_cnf'),



]