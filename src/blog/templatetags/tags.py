from django import template
from datetime import datetime, date, timedelta

register = template.Library()


@register.simple_tag
def get_today(request):
    return datetime.today().strftime("%d %B %Y")


@register.simple_tag
def get_tomorrow(request):
    return (date.today() + timedelta(days=1)).strftime("%d %B %Y")


@register.simple_tag
def get_j2(request):
    return (date.today() + timedelta(days=2)).strftime("%d %B %Y")
