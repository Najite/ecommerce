from django.shortcuts import render, get_object_or_404
from.models import Product
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products':products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'home/detail.html', {'product':product, 'cart_product_form': cart_product_form})



    
    