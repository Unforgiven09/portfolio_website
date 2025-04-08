from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import UserInfo
from .forms import CustomUserChangeForm


@login_required
def profile(request):
    user_info = UserInfo.objects.all()
    context = {
        'title': 'Your profile',
        'user_info': user_info,
    }
    return render(request, 'user_info/profile.html', context)


class RegisterView(CreateView):
    template_name = 'user_info/register.html'
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
    return render(request, 'user_info/change_profile.html', context)