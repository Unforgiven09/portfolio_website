from django import forms
from .models import Category, Products, ProductImage, CommentToProduct, Banner


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ('slug',)


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        exclude = ('uploaded_at', 'thumbnail', 'product', )


class CommentToProductForm(forms.ModelForm):
    class Meta:
        model = CommentToProduct
        exclude = ('published_date', 'user', 'product',)


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        exclude = ('created_date', 'user', 'slug')