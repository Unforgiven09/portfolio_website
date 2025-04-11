from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("product/<slug:product_slug>/", views.product, name="product"),
    path("category/<slug:category_slug>/", views.category, name="category"),
    path("add-category/", views.add_category, name="add_category"),
    path("add-product/", views.add_product, name="add_product"),
    path("add-banner/", views.add_banner, name="add_banner_add"),
    path("add-banner/<slug:banner_slug>/", views.add_banner, name="add_banner"),
    path("all-banners/", views.all_banners, name="all_banners"),
]
