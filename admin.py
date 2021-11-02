from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import *

# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','number','locality','state','city','zipcode']




@admin.register(Restaurant)
class RestaurantModelAdmin(admin.ModelAdmin):
    list_display = ['id','username','Restaurant_name','locality','state','city','zipcode','Restaurant_category','Restaurant_image']

@admin.register(Restauranttype)
class RestauranttypeModelAdmin(admin.ModelAdmin):
    list_display = ['id','Restaurant_type','Restauranttype_image']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','selling_price','disc_price','category','Restro_name','zipcode','product_image']

@admin.register(cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','customer_info','product','product_info','quantity','order_date','status']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.id])
        return format_html('<a href="{}">{}</a>',link, obj.customer.name)
    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.id])
        return format_html('<a href="{}">{}</a>',link, obj.product.title)
