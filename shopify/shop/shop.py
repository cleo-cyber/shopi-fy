from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import generic
from .models import Product
from musicapp.forms import ProductForm
from django.http import JsonResponse
import json
# Create your views here.


# ===== DISPLAY METHODS ===== #


class ShopView(generic.ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        context = Product.objects.all()
        return context


class AdminProductList(generic.ListView):
    template_name = 'shop/productlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        context = Product.objects.all()
        return context

#  ==== ADD PRODUCTS === #


def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        product = Product()
        if form.is_valid():
            product.product_image = request.FILES['product_image']
            product.product_name=request.POST.get('product_name')
            product.price = request.POST.get('price')
            product.save()

            return redirect('productlist')
    return render(request, 'shop/addproducts/add_product.html', {'form': form})

# ==== EDIT PRODUCTS === #


def edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productlist')
    except:
        ValueError('Invalid Operation')
    return render(request, 'shop/updateproduct/updateproduct.html', {'product': product,
                                                                     'form': form})


def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('productlist')
    except:
        ValueError('Invalid Operation')

# === CART === #

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    productAction=data['productAction']
    print(productId)
    print(productAction)
    return JsonResponse('item was added',safe=False)