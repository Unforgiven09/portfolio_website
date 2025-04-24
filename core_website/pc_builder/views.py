from django.shortcuts import render, redirect, get_object_or_404

from main.models import Products
from .forms import PartsForm


def index(request):
    context = {
        'title': 'PC builder'
    }
    return render(request, 'pc_builder/index.html', context)


def part_info_update(request, product_id):
    prod = get_object_or_404(Products, id=product_id)
    parts_instance = getattr(prod, 'parts', None)

    if request.method == 'POST':
        form = PartsForm(request.POST, instance=parts_instance, product=prod)
        if form.is_valid():
            part = form.save(commit=False)
            part.product = prod
            part.save()
            return redirect('admin_products')
    else:
        form = PartsForm(instance=parts_instance, product=prod)

    context = {
        'title': f'Change product {prod.name}',
        'form': form,
    }
    return render(request, 'pc_builder/part_info_update.html', context)