from  django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
     path('create/', views.order_create, name='order_create'),
     path('all-orders/', views.all_orders, name='all_orders'),
     path('all-user-orders/<int:user_id>/', views.all_user_orders, name='all_user_orders'),
     path('order-info/<int:order_id>/', views.order_info, name='order_info'),
     path('order/<int:order_id>/word/', views.order_word, name='order_word'),
]