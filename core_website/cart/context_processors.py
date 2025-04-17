from .cart import Cart


def cart_nav(request):
    return {'len': Cart(request).__len__()}