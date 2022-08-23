from math import prod
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import generic
from .models import Product
from musicapp.forms import ProductForm

# Create your views here.


# ===== DISPLAY METHODS ===== #


class ShopView(generic.ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        context = Product.objects.all()
        print(context)
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
            product.price = request.POST.get('price')
            product.save()

            return redirect('shop')
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
