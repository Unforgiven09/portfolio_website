from django.contrib import admin
from .models import Category, Products, Banner, CommentToProduct, ProductImage

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Banner)
admin.site.register(CommentToProduct)
admin.site.register(ProductImage)