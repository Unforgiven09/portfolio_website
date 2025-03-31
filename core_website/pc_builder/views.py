from django.shortcuts import render

def index(request):
    context = {
        'title': 'PC builder'
    }
    return render(request, 'pc_builder/index.html', context)
