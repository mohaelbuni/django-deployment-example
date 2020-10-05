from django import template


register = template.Library()


@register.filter(name='cutx')
def cutx(value, arg):
    return value.replace(arg, '')

