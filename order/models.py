from django.db import models
from shop.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField(default='enter your address here')
    contact = models.PositiveIntegerField(default= '+234')
    email = models.EmailField()
    flutterwave_id = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE )
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)
    
    def __str__(self):
        return self.price
    
    def get_cost(self): 
        return self.price * self.quantity
    
    
    
    
