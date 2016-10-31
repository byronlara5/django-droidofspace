from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def get_photo(entry):
    #check to see if an entryphoto exists
    if entry.entryphoto_set.all():
        return entry.entryphoto_set.all()[0].photo