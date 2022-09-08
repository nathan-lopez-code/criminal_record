from django import template


register = template.Library()

@register.filter
def initials(name):
    ini = name[0].upper()
    return ini


@register.filter
def integer(floats):
    return int(floats)


@register.filter
def round1(floats):
    return round(floats, 1)
