from django.contrib import admin
from shop.models import Product,ShippingAddress,Order,OrderItem,Customer

# Register your models here.
class ShopAdmin(admin.AdminSite):
    site_header='Shop Admin Area'

shop_site=ShopAdmin(name='ShopAdmin')

shop_site.register(Product)
shop_site.register(ShippingAddress)
shop_site.register(Order)
shop_site.register(OrderItem)
shop_site.register(Customer)