from django.shortcuts import render, redirect, get_object_or_404
from .models import Parts
from main.models import Products
from .forms import PartsForm


def index(request):
    motherboards = Parts.objects.filter(product__category__name='Motherboard')
    GPUs = Parts.objects.filter(product__category__name='GPU')
    PSUs = Parts.objects.filter(product__category__name='PSU')
    processors = Parts.objects.filter(product__category__name='Processors')
    RAMs = Parts.objects.filter(product__category__name='RAM')
    SSDs = Parts.objects.filter(product__category__name='SSD')

    context = {
        'title': 'PC builder',
        'motherboards': motherboards,
        'GPUs': GPUs,
        'PSUs': PSUs,
        'processors': processors,
        'RAMs': RAMs,
        'SSDs': SSDs,

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