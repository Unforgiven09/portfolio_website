from django.shortcuts import render


def index(request):
    context = {
        'title': 'CORE: computers and components'
    }
    return render(request, 'main/index.html', context)


def news(request):
    context = {
        'title': 'News'
    }
    return render(request, 'main/news.html', context)


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
