from .models import Category


def categories_processor(request):
    return {'cats': Category.objects.all()}