from django.shortcuts import render, redirect
from django.urls import reverse
from.forms import QuantityProductForm
from cart.cart import Cart
from.models import OrderItem
from.tasks import order_created
import json
import requests
import math
import random
import environ
# Create your views here.
env = environ.Env()
environ.Env.read_env()

def order_create(request):
    cart = Cart(request)
    if request.method =='POST':
        form = QuantityProductForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            name = obj.first_name + ' ' + obj.last_name
            email = obj.email
            contact = obj.contact
            
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price = item['price'],
                                         quantity = item['quantity'],
                                         )
            cart.clear()
            #launch asynchronous task
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            total_cost = order.get_total_cost()
    
            auth_token = env('RAVE_SECRET_KEY')
            hed = {'Authorization': 'Bearer ' + auth_token}        
            data ={
                    'tx_ref':'' +str(math.floor(100000 + random.random() *900000)),
                    'amount': f'{total_cost}',
                    'currency': 'NGN',
                    'redirect_url':'http://127.0.0.1',
                    'payment_options':'card',
                    'customer': {
                        'email':email,
                        'phonenumber':int(contact),
                        'name':name
                    }
                    }
            
            url = 'https://api.flutterwave.com/v3/payments'
            response = requests.post(url, json=data, headers=hed)
            response=response.json()
            link=response['data']['link']
            return redirect(link)
    
        
    else:
        form = QuantityProductForm()
    return render(request, 'order/create.html', {'form':form, 'cart':cart})