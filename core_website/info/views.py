from django.shortcuts import render


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'info/contacts.html', context)


def about(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'info/about.html', context)


def delivery_payment(request):
    context = {
        'title': 'Delivery and payment information'
    }
    return render(request, 'info/delivery_payment.html', context)


def promotions(request):
    context = {
        'title': 'Promotions'
    }
    return render(request, 'info/promotions.html', context)


def return_policy(request):
    context = {
        'title': 'Return policy'
    }
    return render(request, 'info/return_policy.html', context)


def partnership(request):
    context = {
        'title': 'Partnership'
    }
    return render(request, 'info/partnership.html', context)


def vacancies(request):
    context = {
        'title': 'Vacancies'
    }
    return render(request, 'info/vacancies.html', context)
