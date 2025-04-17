from  django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
     path('create/', views.order_create, name='order_create'),
     path('all-orders/', views.all_orders, name='all_orders'),
]