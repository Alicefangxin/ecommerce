from django.shortcuts import render
from .models import Product, Category, Customer, Order
from django.http import JsonResponse


def create_order(request):
    customer_id = request.POST.get('customer_id')
    product_id = request.POST.get('product_id')
    customer = Customer.objects.get(id=customer_id)
    product = Product.objects.get(id=product_id)
    order = Order.objects.create(customer=customer, product=product)
    return JsonResponse({'message': 'Order created successfully!'})


def shopping_cart(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'store/shopping_cart.html', {'orders': orders})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'store/customer_list.html', {'customers': customers})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'store/order_list.html', {'orders': orders})


def homepage(request):
    customer = Customer.objects.get(id=3)
    products = Product.objects.all()
    return render(request, 'store/homepage.html', {'customer': customer, 'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_detail.html', {'product': product})


def order_form(request, customer_id, product_id):
    customer = Customer.objects.get(id=customer_id)
    product = Product.objects.get(id=product_id)
    order = Order(customer=customer, product=product)
    order.save()
    return render(request, 'store/order_form.html', {'order': order})


def submit_order(request, customer_id, product_id):
    customer = Customer.objects.get(id=customer_id)
    product = Product.objects.get(id=product_id)
    order = Order.objects.create(customer=customer, product=product)
    return render(request, 'store/submit_order.html', {'order': order})


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return JsonResponse({'status': 'success'})
