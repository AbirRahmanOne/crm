from django.shortcuts import render
from .models import *

from django.http import HttpResponse


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_order = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    context = {'orders': orders, 'customers': customers,
               'total_order': total_order, 'pending': pending,
               'delivered': delivered
               }
    return render(request, 'accounts/dashboard.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()

    context = {'customer': customer, 'orders': orders,'total_order':total_order}

    return render(request, 'accounts/customer.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})
