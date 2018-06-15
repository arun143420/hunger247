from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from food.models import CartManager
from django.contrib.auth.decorators import login_required
from ordermanage.models import OrdersDone,OrdersConfirm,OrderManager
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from datetime import date
from twilio.rest import Client


@login_required
def order_list_view(request):
    if request.user.is_superuser or request.user.is_staff:

        queryset = CartManager.objects.all().order_by("-order_time")
        return render(request, 'ordermanage/orders.html', {'orders_list': queryset})

    else:
        return redirect('/food/restaurants')


@login_required
def order_detail_view(request,pk):
    if request.user.is_superuser or request.user.is_staff:
        order = get_object_or_404(CartManager, pk=pk)
        return render(request, 'ordermanage/order_detail.html', {'order': order})

    else:
        return redirect('/food/restaurants')

@login_required
def order_list_update_view(request,pk):
    order = get_object_or_404(CartManager,pk=pk)
    if request.method =="POST":
        if request.user.is_superuser or request.user.is_staff:

            status = request.POST['status']
            order_manager = OrderManager()
            order_manager.user = order.user
            order_manager.order_id = order.order_id
            order_manager.payment = order.payment
            order_manager.sub_total = order.sub_total
            order_manager.total = order.total
            order_manager.etc_price = order.etc_price

            account_sid = "ACfcdc76a71768bba5a8fa1695dece27c9"
            auth_token = "f6683c048cee22a89dcf20e4009caca8"

            client = Client(account_sid, auth_token)
            number = order_manager.user.profile.phone
            num = "+91" + number
            if status == "true":
                order_manager.status = True
                order_manager.save()
                #client.api.account.messages.create(to=num, from_="+18305005658",
                                                   #body="Hello your order is successfully delivered")
            elif status == "false":
                order_manager.status = False
                order_manager.save()
                #client.api.account.messages.create(to=num, from_="+18305005658",
                                                   #body="Hello your order is un-successfully delivered")

            for orders in OrdersDone.objects.filter(cartmanager=order):
                order_cnf = OrdersConfirm()
                order_cnf.user = orders.user
                order_cnf.item = orders.item
                order_cnf.etc_price = orders.etc_price
                order_cnf.item_price = orders.item_price
                order_cnf.cartmanager = order_manager
                order_cnf.save()

            order.delete()
            return redirect('/ordermanage/orders/')
        else:
            return redirect('/food/restaurants')
    else:
        return redirect('/ordermanage/orders/')

@login_required
def confirm_orders(request):
    if not request.user.is_superuser:
        return redirect('/food/restaurants')
    else:
        queryset = OrderManager.objects.all().order_by("-delivery_time")
        return render(request, 'ordermanage/confirm_orders.html', {'orders_list': queryset})


@login_required
def confirm_order_detail(request,pk):
    if not request.user.is_superuser:
        return redirect('/food/restaurants')
    else:
        order = get_object_or_404(OrderManager, pk=pk)
        return render(request, 'ordermanage/confirm_order_detail.html', {'cnf_order':order})


@login_required
def resturants_orders(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            restaurant = request.POST['restaurant'].strip()
            month = request.POST['month']
            year = request.POST['year']
            list = OrdersConfirm.objects.filter(add_time__month=month, add_time__year=year)
            context = {
                'list': list,
                'rest_name':restaurant,

            }
            return render(request,'food/rest_pay_post.html', context)
        else:

            list = OrdersConfirm.objects.all()
            return render(request, 'ordermanage/restaurants_pay.html', {'list': list})

    else:
        return redirect('/food/restaurants')