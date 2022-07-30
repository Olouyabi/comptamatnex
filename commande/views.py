from itertools import product
import json
import datetime
from django.shortcuts import get_object_or_404, render
from commande.models import*
from commande.utils import  cookie_cart, cart_data, guest_order
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def store(request, version=None):
    data = cart_data(request)
    cartItems = data['cartItems']
  
    versions = VersionLivre.objects.all()
    livres = Product.objects.all()
    if version:
        version = get_object_or_404(VersionLivre, slug=version)
        livres = livres.filter(name=version)
    context = {
        'versions':versions,
        'version':version,
        'livres':livres,
        'cartItems': cartItems,
        'navbar':'store',
    }
    return render(request, 'store/store.html', context)


def panier(request):
    data = cart_data(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'navbar':'store',
    }
    return render(request, 'store/cart.html', context)


def validation(request):
    data = cart_data(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'navbar':'store',
    }
    return render(request, 'store/checkout.html', context)


def mouvement_article(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
   
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif  action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    # return JsonResponse('article est ajouté', safe=False)


# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
def process_order(request):
    order_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    else:
        customer, order = guest_order(request, data)

    total = float(data['form']['total'].replace(',', '.'))
    order.order_id = order_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            pays=data['shipping']['pays'],
            ville=data['shipping']['ville'],
            adresse=data['shipping']['adresse'],
            telephone=data['shipping']['telephone'],
        )
    # return JsonResponse('Payement effectué', safe=False)
