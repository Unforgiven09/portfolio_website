from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderStatusUpdateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                cart.clear()
                return render(request, 'order/created.html', {'title': 'Order created', 'order': order})
        else:
            messages.info(request, "Invalid form.")
            return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))
    else:
        form = OrderCreateForm()
        return render(request, 'order/create.html', {'title': 'Order creation', 'cart': cart, 'form': form})


def all_orders(request):
    orders = Order.objects.all()
    context = {
        'title': f'All orders',
        'orders': orders
    }
    return render(request, 'order/all_orders.html', context)


def order_info(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderStatusUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
    else:
        form = OrderStatusUpdateForm(instance=order)

    context = {
        'title': f'Order #{order.id}',
        'order': order,
        'form': form
    }
    return render(request, 'order/order_info.html', context)
