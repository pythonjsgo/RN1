from django import template

register = template.Library()

@register.filter
def last_items(value, count = 3):
    return value[len(value)-count:]

@register.filter
def selection_from_last_items(value, first = 1, second = 3):
    value.reverse()
    return value[first, second]

@register.filter
def selection_by_num(value, number):
    value.reverse()
    return value[number]


