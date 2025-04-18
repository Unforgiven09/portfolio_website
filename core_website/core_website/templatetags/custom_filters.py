from django import template

# {% load custom_filters %}
register = template.Library()

@register.filter
def format100(value):  # {{ value|format100 }}
    try:
        return "{:.2f}".format(int(value) / 100)
    except (ValueError, TypeError):
        return value
