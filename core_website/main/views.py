from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Products, Category, ProductImage
from .forms import CatsForm


def index(request):
    products = Products.objects.filter(is_available=True)
    context = {
        'title': 'CORE: computers and components',
        'products': products
    }
    return render(request, 'main/index.html', context)


def product(request, product_slug):
    product = Products.objects.filter(slug=product_slug)
    context = {
        'title': f'Product: {product.name}',
        'product': product
    }
    return render(request, 'main/product.html', context)


def category(request, category_slug):
    cat = get_object_or_404(Category, slug=category_slug)
    products = Products.objects.filter(category=cat, is_available=True)
    context = {
        'title': f'Category: {cat.name}',
        'products': products,
        'category': cat,
    }
    return render(request, 'main/category.html', context)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CatsForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = CatsForm()
    context = {'title': 'Add category', 'form': form}
    return render(request, "main/add_category.html", context)