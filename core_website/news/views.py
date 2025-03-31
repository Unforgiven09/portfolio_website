from django.shortcuts import render

def index(request):
    context = {
        'title': 'News'
    }
    return render(request, 'news/index.html', context)
