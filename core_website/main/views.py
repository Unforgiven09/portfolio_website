from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import UserInfo
from .forms import CustomUserChangeForm


def index(request):
    context = {
        'title': 'CORE: computers and components'
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'main/contacts.html', context)


def about(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'main/about.html', context)


def delivery_payment(request):
    context = {
        'title': 'Delivery and payment information'
    }
    return render(request, 'main/delivery_payment.html', context)


def promotions(request):
    context = {
        'title': 'Promotions'
    }
    return render(request, 'main/promotions.html', context)


def return_policy(request):
    context = {
        'title': 'Return policy'
    }
    return render(request, 'main/return_policy.html', context)


def partnership(request):
    context = {
        'title': 'Partnership'
    }
    return render(request, 'main/partnership.html', context)


def vacancies(request):
    context = {
        'title': 'Vacancies'
    }
    return render(request, 'main/vacancies.html', context)


@login_required
def profile(request):
    user_info = UserInfo.objects.all()
    context = {
        'title': 'Your profile',
        'user_info': user_info,
    }
    return render(request, 'registration/profile.html', context)


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


@login_required
def change_profile(request):
    user_info = request.user.user_info
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user_info)
    context = {
        'title': 'Change profile',
        'form': form,
    }
    return render(request, 'registration/change_profile.html', context)