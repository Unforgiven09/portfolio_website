from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Products
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    update = request.POST.get('update', 'False') == 'True'
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=update)
        messages.success(request, f"{product.name} added to cart.")
        return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))
    return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))


@require_POST
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.add(product, quantity=-1, update_quantity=True)
    messages.info(request, f"{product.name} removed from cart.")
    return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    messages.info(request, f"{product.name} removed from cart.")
    return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))


def cart_detail(request):
    cart = Cart(request)
    context = {'title': 'Your cart', 'cart': cart}
    return render(request, 'cart/detail.html', context)


@require_POST
def add_multiple(request):
    product_ids = request.POST.get("product_ids", "").split(",")
    cart = Cart(request)

    for pid in product_ids:
        if pid.isdigit():
            product = get_object_or_404(Products, id=int(pid))
            cart.add(product=product, quantity=1, update_quantity=False)
            messages.success(request, f"{product.name} added to cart.")

    return redirect("cart:cart_detail")