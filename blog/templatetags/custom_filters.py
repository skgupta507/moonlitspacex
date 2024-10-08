from django import template

register = template.Library()


@register.filter
def cover_image(index):
    return f"images/cover{index}.jpg"


@register.filter
def has_more_than(arr, count):
    return len(arr) > count
