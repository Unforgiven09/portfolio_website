from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
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
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/registration/', views.RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/change-profile/', views.change_profile, name='change_profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
