from django import template
from django.template.defaultfilters import stringfilter
# from StatsSite.utils.constant import CONVERSION_LIST
from utils.constant import CONVERSION_LIST

register = template.Library()


@register.filter
@stringfilter
def transformatch(value):
    """Format the match in a good format"""
    return value.strip("[").strip("]").strip("'").replace("|", " - ")


@register.filter
@stringfilter
def transformchampionship(value):
    """Transform Championship in a good format"""
    for keys, values in CONVERSION_LIST.items():
        if value == values:
            return keys
