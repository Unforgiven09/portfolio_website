from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category, ProductImage, Banner
from .forms import CategoryForm, ProductForm, ProductImageForm, CommentToProductForm, BannerForm


def index(request):
    products = Products.objects.filter(is_available=True)
    banners = Banner.objects.filter(is_published=True)
    context = {
        'title': 'CORE: computers and components',
        'products': products,
        'banners': banners,
    }
    return render(request, 'main/index.html', context)


def product(request, product_slug):
    prod = Products.objects.filter(slug=product_slug)
    context = {
        'title': f'Product: {prod}',
        'product': prod
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
def add_category(request, category_slug=None):
    if category_slug is None:
        title = 'Add new category'
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = CategoryForm()
    else:
        category_to_change = get_object_or_404(Category, slug=category_slug)
        title = f'Change banner: {category_to_change.name}'
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category_to_change)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = CategoryForm(instance=category_to_change)
    context = {'title': title, 'form': form}
    return render(request, "main/add_category.html", context)


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = ProductForm()
    context = {'title': 'Add product', 'form': form}
    return render(request, "main/add_product.html", context)


@login_required
def add_banner(request, banner_slug=None):
    if banner_slug is None:
        title = 'Add new banner'
        if request.method == 'POST':
            form = BannerForm(request.POST, request.FILES)
            if form.is_valid():
                banner = form.save(commit=False)
                banner.user = request.user
                banner.save()
                return redirect('index')
        else:
            form = BannerForm()
    else:
        banner_to_change = get_object_or_404(Banner, slug=banner_slug)
        title = f'Change banner: {banner_to_change.name}'
        if request.method == 'POST':
            form = BannerForm(request.POST, request.FILES, instance=banner_to_change)
            if form.is_valid():
                banner = form.save(commit=False)
                banner.user = request.user
                banner.save()
                return redirect('index')
        else:
            form = BannerForm(instance=banner_to_change)
    context = {'title': title, 'form': form}
    return render(request, "main/add_banner.html", context)


def admin_banners(request):
    banners = Banner.objects.all()
    context = {
        'title': 'All banners',
        'banners': banners,
    }
    return render(request, 'main/admin_banners.html', context)


def all_categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'All categories',
        'categories': categories,
    }
    return render(request, 'main/all_categories.html', context)


def admin_categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'All categories',
        'categories': categories,
    }
    return render(request, 'main/admin_categories.html', context)


def admin_panel(request):
    context = {
        'title': 'Admin panel',
    }
    return render(request, 'main/admin_panel.html', context)