from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories '
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=30)
    category= models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    description = models.TextField(default='enter a description here')
    image = models.ImageField(upload_to='media/product')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    