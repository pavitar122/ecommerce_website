from django.shortcuts import render, redirect
from django.http import JsonResponse
from ecommerceapp.models import Contact, Product, Order
from math import ceil
import json

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    category1_products = all_products.filter(category='Watch')
    category2_products = all_products.filter(category='Glass')


    return render(request, "index.html",  
        {'category1_products': category1_products,
        'category2_products': category2_products,})

def contact(request):
    if request.method=="POST":
        name =  request.POST['name']
        email =  request.POST['email']
        desc =  request.POST['desc']
        phone =  request.POST['phone']

        entry = Contact(name=name,email=email,desc=desc,phone=phone)
        entry.save()
        return redirect("/")
    return render(request, "contact.html")

def copy(request):
    all_products = Product.objects.all()
    category1_products = all_products.filter(category='Watch')
    category2_products = all_products.filter(category='Glass')

    return render(request, "pratice.html",
        {'category1_products': category1_products,
        'category2_products': category2_products,})


def cart(request):
    return render(request, "cart.html")

def checkout(request):
    if request.method=="POST":
        name =  request.POST['name']
        phone =  request.POST['phone']
        address =  request.POST['address']
        pin =  request.POST['pin']
        email = request.POST['email']
        product = request.POST['itemsJson']
        entry = Order(name=name,phone=phone,address=address,pin=pin, email=email, product=product)
        entry.save()
        return redirect("/")
    return render(request, "checkout.html")