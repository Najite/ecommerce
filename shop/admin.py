from django.contrib import admin
from.models import Category, Product

# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created', 'updated']
    list_fiter = ['price', 'category', 'created', 'updated']
    prepopulated_fields = {'slug':('name',)}
    
