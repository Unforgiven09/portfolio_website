from django import template

register = template.Library()

@register.filter
def format100(value):
    try:
        return "{:.2f}".format(int(value) / 100)
    except (ValueError, TypeError):
        return value

        # {% load custom_filters %}
        # {{ value|format100 }}