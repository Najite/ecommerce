import random
import math
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from order.models import Order
import requests
import json
import environ
from django.views.decorators.http import require_http_methods
from python_flutterwave import payment

payment.token ='FLWSECK_TEST-0ab780a5f4b1a4f8bb3c6daaed89255b-X'


env = environ.Env()
environ.Env.read_env()

# Create your views here.
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
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
            'email': 'emma@m.com',
            'phonenumber': 38212342233,
            'name':'emmanuel'
        }
        },
    
    
    
    url = 'https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return redirect(link)
    
    


@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status =request.GET.get('status', None)
    tx_ref =request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return HttpResponse('finished')
    
       
        