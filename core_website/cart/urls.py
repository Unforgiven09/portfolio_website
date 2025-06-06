from  django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add-multiple/', views.add_multiple, name='add_multiple'),
]