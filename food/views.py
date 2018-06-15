from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from food.models import Restaurant, Menu, Cart
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from food.forms import CartForm
from django.core.exceptions import ObjectDoesNotExist
from food.models import CartManager
from ordermanage.models import OrdersDone, OrderManager
from twilio.rest import Client
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.forms import ContactUsForm
from paypal.standard.forms import PayPalPaymentsForm


def home(request):
    my_cart = Cart.objects.filter(user=request.user)
    return render(request, 'food/base.html', {'my_cart':my_cart})


def restaurants_list_view(request):

    if request.method == "POST":
        search = request.POST['search']
        queryset_list = Restaurant.objects.filter(name__icontains=search).order_by("name") or \
                        Restaurant.objects.filter(address__icontains=search).order_by("name") or\
                        Restaurant.objects.filter(category__icontains=search).order_by("name")

        paginator = Paginator(queryset_list, 4)
        page = request.GET.get('page')
        queryset_list = paginator.get_page(page)

        context = {
            'restaurants_list': queryset_list,
            'page': search,

        }
        return render(request, "food/searched_restaurants.html", context)

    else:

        if request.user.is_authenticated:
            queryset_list = Restaurant.objects.all().order_by("name") and Restaurant.objects.all().order_by("-rating")
            paginator = Paginator(queryset_list, 4)
            page = request.GET.get('page')
            queryset_list = paginator.get_page(page)

            area = request.user.profile.area
            queryset_list_mine = Restaurant.objects.filter(area=area).order_by("name")

            paginator_mine = Paginator(queryset_list_mine, 4)
            page_mine = request.GET.get('page')
            queryset_list_mine = paginator_mine.get_page(page_mine)

            my_cart = Cart.objects.filter(user=request.user)
            all_list = Restaurant.objects.all()
            contact = ContactUsForm
            context = {'restaurants_list': queryset_list,
                       'mine_restaurant_list': queryset_list_mine,
                       'my_cart':my_cart,
                       'all_list': all_list,
                       'form':contact
                       }

            return render(request, "food/restaurants_list.html", context)

        else:
            queryset_list = Restaurant.objects.all().order_by("name") and Restaurant.objects.all().order_by("-rating")
            paginator = Paginator(queryset_list, 4)
            page = request.GET.get('page')
            queryset_list = paginator.get_page(page)
            all_list = Restaurant.objects.all()
            contact = ContactUsForm
            context = {
                'restaurants_list': queryset_list,
                'all_list': all_list,
                'form': contact
            }

            return render(request, "food/restaurants_list.html", context)


def advanced_search_view(request):
    if request.method == 'POST':
        category = request.POST['optradio']
        area = request.POST['area']
        queryset_list1 = Restaurant.objects.filter(category__icontains =category, area__icontains=area)

        paginator_mine = Paginator(queryset_list1, 4)
        page_mine = request.GET.get('page')
        queryset_list1 = paginator_mine.get_page(page_mine)

        context = {'restaurant_list1': queryset_list1,

        }
        return render(request, "food/advanced_search.html", context)


def my_restaurant_list(request):
    if request.method == 'POST':
        search = request.POST['search']
        area = request.user.profile.area

        queryset_list_mine = Restaurant.objects.filter(name__icontains=search, area=area).order_by("name")

        paginator_mine = Paginator(queryset_list_mine, 4)
        page_mine = request.GET.get('page')
        queryset_list_mine = paginator_mine.get_page(page_mine)
        context = {
                   'mine_restaurant_list': queryset_list_mine,
                    'page': search,
        }
        return render(request, "food/my_restaurants_list.html", context)
    else:
        return redirect('/food/restaurants')


def restaurant_detail_view(request, pk):
    restaurant_instance = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'food/restaurant_detail.html', {'restaurant': restaurant_instance})


@login_required
def add_to_cart(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        etc_cost = request.POST.get("cost", None)
        cart = Cart()
        cart.user = request.user
        cart.item = menu
        cart.item_price = menu.price
        cart.etc_price = etc_cost
        cart.save()

        return JsonResponse({'user': cart.user.username})

    else:
        return HttpResponse("request Must be post")


@login_required
def cart_view(request):

        query_set = Cart.objects.filter(user=request.user)
        cart_count = Cart.objects.filter(user=request.user).count()
        context = {
            'cart_list': query_set,
            'cart_count':cart_count,
        }
        return render(request, 'food/cart.html', context)


@login_required
def delete_from_cart(request, pk):
    item = get_object_or_404(Cart, pk=pk)
    item.delete()
    messages.success(request, "Item Removed From Cart")
    return redirect('/food/cart/')


@login_required
def order_confirm_view(request):
    if request.method == 'POST':
        order_no = request.POST['order']
        payment = request.POST['payment']
        total = request.POST['total_amount']
        etc = request.POST['etc_amount']
        sub_total = request.POST['sub_total_amount']

        checkout = CartManager()
        checkout.order_id = order_no
        checkout.user = request.user
        checkout.sub_total = sub_total
        checkout.payment = payment
        checkout.etc_price = etc
        checkout.total = total

        checkout.save()

        for order in Cart.objects.filter(user=request.user):
            order_done = OrdersDone()
            order_done.user = order.user
            order_done.item = order.item
            order_done.cartmanager = checkout
            order_done.item_price = order.item_price
            order_done.etc_price = order.etc_price
            order.cartmanager = checkout
            order.save()

            order_done.save()
        Cart.objects.filter(user=request.user).delete()

        context = {
            'order_no': order_no,
            'total': sub_total
        }
        account_sid = "ACfcdc76a71768bba5a8fa1695dece27c9"
        auth_token = "f6683c048cee22a89dcf20e4009caca8"

        client = Client(account_sid, auth_token)
        number = request.user.profile.phone
        num = "+91"+number
        # client.api.account.messages.create(to=num, from_="+18305005658", body="Hello"+request.user.first_name+"!!"+
        # "Your order has placed Successfully under"
        # "the order number"+order_no+" ."+"You"

        # " need to pay"+total+".")

        if payment == 'COD':
            return render(request, 'food/confirm_order.html', context)

        elif payment == 'Paytm':
            return render(request, 'food/paypal_order.html', context)

        else:
            x = int(order_no)
            paypal_dict = {
                "business": settings.PAYPAL_RECEIVER_EMAIL,
                "amount": sub_total,
                "item_name": x,
                "invoice": x,
                #"notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
                "return": request.build_absolute_uri(reverse('food:paypal_cnf')),
                "cancel_return": request.build_absolute_uri(reverse('food:paypal_not_cnf')),
                # "custom": "premium_plan",

            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            context = {"form": form}
            return render(request, "food/paypal_order.html", context)

    else:
        return redirect('/food/restaurants')


@login_required
def paypal_cnf(request):
    if request.method == 'GET':
        if CartManager.objects.exists():
            my_order = CartManager.objects.filter(payment = "credit/debit").order_by("-order_time")[0:1] and CartManager.objects.filter(user =request.user).order_by("-order_time")[0:1]
            return render(request, 'food/cnf_paypal.html', {'order': my_order})


@login_required
def clear_cart(request):
    if request.method == 'POST':
        Cart.objects.filter(user=request.user).delete()
        return redirect('/food/cart/')
    else:
        return redirect('/food/cart/')


@login_required
def cart(request):
    query = Cart.objects.filter(user=request.user)
    return render(request,'food/base.html',{'list':query})


def contact_view(request):
    if request.method == 'POST':
        contact = ContactUsForm(request.POST)
        if contact.is_valid():
            con = contact.save(commit=False)
            con.user = request.user
            con.save()
            messages.success(request, "Your Feedback has been submitted")
            return redirect('/food/restaurants')
        else:
            return redirect('/food/restaurants/')
    else:
        return redirect('/food/restaurants')

@login_required
def my_orders_view(request):
    orders = OrderManager.objects.filter(user= request.user).order_by("-delivery_time")
    return render(request,'food/my_orders.html',{'all_orders':orders})

@login_required
def my_order_deatil(request,pk):
    order = get_object_or_404(OrderManager,pk=pk)
    return render(request, 'food/my_orders_detail.html', {'cnf_order': order})