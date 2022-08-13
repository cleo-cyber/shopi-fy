from django.contrib import admin
from shop.models import Product

# Register your models here.
class ShopAdmin(admin.AdminSite):
    site_header='Shop Admin Area'

shop_site=ShopAdmin(name='ShopAdmin')

shop_site.register(Product)