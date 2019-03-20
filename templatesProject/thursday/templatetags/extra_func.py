from django import template
register = template.Library()


def cut(value, arg):
    return value.replace(arg, "")


def lower(value):
    return  value.lower()


register.filter('cut', cut)
register.filter('lower', lower)


@register.simple_tag(name='minustwo')
def minus_two(value):
    return int(value)-2


# register.tag('minustwo', minus_two)

