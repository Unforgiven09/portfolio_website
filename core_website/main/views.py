from django.shortcuts import render


def index(request):
    context = {
        'title': 'CORE: computers and components'
    }
    return render(request, 'main/index.html', context)





