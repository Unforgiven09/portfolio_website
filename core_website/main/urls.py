from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
    path("category/<slug:category_slug>/", views.category, name="category"),
    path("add-category/", views.add_category, name="add_category_new"),
    path("add-category/<slug:category_slug>/", views.add_category, name="add_category"),
    path("add-product/", views.add_product, name="add_product_new"),
    path("add-product/<slug:product_slug>/", views.add_product, name="add_product"),
    path("add-banner/", views.add_banner, name="add_banner_new"),
    path("add-banner/<slug:banner_slug>/", views.add_banner, name="add_banner"),
    path("admin-banners/", views.admin_banners, name="admin_banners"),
    path("all-categories/", views.all_categories, name="all_categories"),
    path("admin-categories/", views.admin_categories, name="admin_categories"),
    path("admin-products/", views.admin_products, name="admin_products"),
    path("admin-panel/", views.admin_panel, name="admin_panel"),
]
