from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery_payment/', views.delivery_payment, name='delivery_payment'),
    path('promotions/', views.promotions, name='promotions'),
    path('return_policy/', views.return_policy, name='return_policy'),
    path('partnership/', views.partnership, name='partnership'),
    path('vacancies/', views.vacancies, name='vacancies'),
]
